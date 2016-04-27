import os
import subprocess
import re
import sys
import fnmatch
import commands

from collections import defaultdict

from sourcefile import SourceFile

from optparse import OptionParser

lint_root = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(os.path.dirname(lint_root))


def git(command, *args):
    args = list(args)

    proc_kwargs = {"cwd": repo_root}
    command_line = ["git", command] + args

    try:
        return subprocess.check_output(command_line, **proc_kwargs)
    except subprocess.CalledProcessError:
        raise


def iter_files(flag=False):
    if not flag:
        for item in git("diff", "--name-status", "HEAD~1").strip().split("\n"):
            status = item.split("\t")
            if status[0].strip() != "D":
                yield status[1]
    else:
        os.chdir(repo_root)
        for pardir, subdir, files in os.walk(repo_root):
            for item in pardir + subdir + files:
                yield item
        os.chdir(lint_root)


def check_path_length(path):
    if len(path) + 1 > 150:
        return [("PATH LENGTH", "%s longer than maximum path length (%d > 150)" % (path, len(path) + 1), None)]
    return []


def check_filename_space(path):
    bname = os.path.basename(path)
    if re.compile(" ").search(bname):
        return [("FILENAME WHITESPACE", "Filename of %s contain white space" % path, None)]
    return []


def check_format(path):
    bname = os.path.basename(path)
    lints = {"python": ["pylint", "*.py"],
             "json": ["jsonlint", "*.json"],
             "xml": ["xmllint", "*.xml"]}

    for key in lints:
        if fnmatch.fnmatch(bname, lints[key][1]):
            returncode = commands.getstatusoutput("%s " % lints[key][0] + os.path.join(repo_root, path))
            if returncode != 0:
                return [("INVALID %s FORMAT" % key.upper(), "%s contain invalid %s format" % (path, key), None)]
    return []


def check_permission(path):
    bname = os.path.basename(path)
    if not re.compile('\.py$|\.sh$').search(bname):
        if os.access(os.path.join(repo_root, path), os.X_OK):
            return [("EXTERNAL EXECUTABLE PERMISSION", "%s contain external executable permission" % path, None)]
    return []


def parse_whitelist_file(filename):
    data = defaultdict(lambda:defaultdict(set))

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [item.strip() for item in line.split(":")]
            if len(parts) == 2:
                parts.append(None)
            else:
                parts[-1] = int(parts[-1])

            error_type, file_match, line_number = parts
            data[file_match][error_type].add(line_number)

    def inner(path, errors):
        whitelisted = [False for item in xrange(len(errors))]

        for file_match, whitelist_errors in data.iteritems():
            if fnmatch.fnmatch(path, file_match):
                for i, (error_type, msg, line) in enumerate(errors):
                    if "*" in whitelist_errors:
                        whitelisted[i] = True
                    elif error_type in whitelist_errors:
                        allowed_lines = whitelist_errors[error_type]
                        if None in allowed_lines or line in allowed_lines:
                            whitelisted[i] = True

        return [item for i, item in enumerate(errors) if not whitelisted[i]]
    return inner


_whitelist_fn = None
def whitelist_errors(path, errors):
    global _whitelist_fn

    if _whitelist_fn is None:
        _whitelist_fn = parse_whitelist_file(os.path.join(lint_root, "lint.whitelist"))
    return _whitelist_fn(path, errors)


class Regexp(object):
    pattern = None
    file_extensions = None
    error = None
    _re = None

    def __init__(self):
        self._re = re.compile(self.pattern)

    def applies(self, path):
        return (self.file_extensions is None or
                os.path.splitext(path)[1] in self.file_extensions)

    def search(self, line):
        return self._re.search(line)


class TrailingWhitespaceRegexp(Regexp):
    pattern = " $"
    error = "TRAILING WHITESPACE"


class TabsRegexp(Regexp):
    pattern = "^\t"
    error = "INDENT TABS"


class CRRegexp(Regexp):
    pattern = "\r$"
    error = "CR AT EOL"

regexps = [item() for item in
           [TrailingWhitespaceRegexp,
            TabsRegexp,
            CRRegexp]]


def check_regexp_line(path, f):
    errors = []

    applicable_regexps = [regexp for regexp in regexps if regexp.applies(path)]

    for i, line in enumerate(f):
        for regexp in applicable_regexps:
            if regexp.search(line):
                errors.append((regexp.error, "%s line %i" % (path, i+1), i+1))

    return errors


def check_parsed(path, f):
    source_file = SourceFile(repo_root, path, "/")

    errors = []
    if source_file.root is None:
        return [("PARSE-FAILED", "Unable to parse file %s" % path, None)]

    if source_file.testharness_nodes:
        if len(source_file.testharness_nodes) > 1:
            errors.append(("MULTIPLE-TESTHARNESS",
                           "%s more than one <script src='/resources/testharness.js'>" % path, None))
        elif not source_file.testharnessreport_nodes:
            errors.append(("MISSING-TESTHARNESSREPORT",
                            "%s missing <script src='/resources/testharnessreport.js'>" % path, None))

    if source_file.testharnessreport_nodes:
        if len(source_file.testharnessreport_nodes) > 1:
            errors.append(("MULTIPLE-TESTHARNESSREPORT",
                           "%s more than one <script src='/resources/testharnessreport.js'>" % path, None))
        elif not source_file.testharness_nodes:
            errors.append(("MISSING-TESTHARNESS",
                            "%s missing <script src='/resources/TESTHARNESS.js'>" % path, None))

    return errors


def output_errors(errors):
    for error_type, error, line_number in errors:
        print "%s: %s" % (error_type, error)


def output_error_count(error_count):
    if not error_count:
        return

    by_type = " ".join("%s: %d" % item for item in error_count.iteritems())
    count = sum(error_count.values())
    if count == 1:
        print "There was 1 error (%s)" % (by_type,)
    else:
        print "There were %d errors (%s)" % (count, by_type)


def main():
    error_count = defaultdict(int)

    parser = OptionParser()
    parser.add_option('-f', '--full', dest="full_option", action='store_true', default=False)
    options, args = parser.parse_args()

    def run_lint(path, fn, *args):
        errors = whitelist_errors(path, fn(path, *args))
        output_errors(errors)
        for error_type, error, line in errors:
            error_count[error_type] += 1

    for path in iter_files(options.full_option):
        abs_path = os.path.join(repo_root, path)
        if not os.path.exists(abs_path):
            continue
        for path_fn in file_path_lints:
            run_lint(path, path_fn)

        for format_fn in file_format_lints:
            run_lint(path, format_fn)

        for state_fn in file_state_lints:
            run_lint(path, state_fn)

        if not os.path.isdir(abs_path):
            if re.compile('\.html$|\.htm$|\.xhtml$|\.xhtm$').search(abs_path):
                with open(abs_path) as f:
                    for file_fn in file_content_lints:
                        run_lint(path, file_fn, f)
                        f.seek(0)

    output_error_count(error_count)
    return sum(error_count.itervalues())

file_path_lints = [check_path_length, check_filename_space]
file_content_lints = [check_regexp_line, check_parsed]
file_format_lints = [check_format]
file_state_lints = [check_permission]

if __name__ == "__main__":
    error_count = main()
    if error_count > 0:
        sys.exit(1)