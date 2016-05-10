## Introduction

We have a lint tool for catching common mistakes in test files. Now it can
check html, htm, xhtml, xhtm, json and xml files.
- You can run it manually by starting the `lint.py` executable from the root of your local
crosswalk-test-suite working directory like this:

```
./tools/lint/lint.py
```

The lint tool is also run automatically for every submitted pull request,
and reviewers will not merge branches with tests that have lint errors, so
you must either [fix all lint errors](#fixing-lint-errors), or you must
[white-list test files] (#updating-the-whitelist) to suppress the errors.

## Usage of lint tool

1. If check all crosswalk-test-suite:</br>
<code>
./tools/lint/lint.py
</code>
1. If check submitted pull request:</br>
<code>
./tools/lint/lint.py -p
</code>
1. If check specified folder, the specified folder must be relative path of
crosswalk-test-suite:</br>
<code>
./tools/lint/lint.py -d apptools/apptools-android-tests
</code>

## Setup Environment

1. Install jsonlint: `sudo apt-get install python-demjson`
1. Install xmllint: `sudo apt-get install libxml2-utils`
1. Install html5lib: `pip install html5lib`

## Fixing lint errors

You must fix any errors the lint tool reports, unless an error is for
something essential to a certain test or that for some other exceptional
reason shouldn't prevent the test from being merged. In those cases you can
[white-list test files](#updating-the-whiteslist) to suppress the errors.
Otherwise, use the details in this section to fix all errors reported.

* **CR AT EOL**: Test-file line ends with CR (U+000D) character; **fix**:
  reformat file so each line just has LF (U+000A) line ending (standard,
  cross-platform "Unix" line endings instead of, e.g., DOS line endings).

* **EARLY-TESTHARNESSREPORT**: Test file has an instance of
  `<script src='/resources/testharnessreport.js'>` prior to
  `<script src='/resources/testharness.js'>`; **fix**: flip the order.

* **INDENT TABS**: Test-file line starts with one or more tab characters;
  **fix**: use spaces to replace any tab characters at beginning of lines.

* **MISSING-TESTHARNESS**: Test file is missing an instance of
  `<script src='/resources/testharness.js'>`; **fix**: ensure each
  test file contains `<script src='/resources/testharness.js'>`.

* **MISSING-TESTHARNESSREPORT**: Test file is missing an instance of
  `<script src='/resources/testharnessreport.js'>`; **fix**: ensure each
  test file contains `<script src='/resources/testharnessreport.js'>`.

* **MULTIPLE-TESTHARNESS**: Test file with multiple instances of
  `<script src='/resources/testharness.js'>`; **fix**: ensure each test
  has only one `<script src='/resources/testharness.js'>` instance.

* **MULTIPLE-TESTHARNESSREPORT**: Test file with multiple instances of
  `<script src='/resources/testharnessreport.js'>`; **fix**: ensure each test
  has only one `<script src='/resources/testharnessreport.js'>` instance.

* **TRAILING WHITESPACE**: Test-file line has trailing whitespace; **fix**:
  remove trailing whitespace from all lines in the file.

* **UNNECESSARY EXECUTABLE PERMISSION**: Test file contains unnecessary executable permission; **fix**:
  remove unnecessary executable permission of the file.

* **INVALID JSON FORMAT**: Test file contains invalid json format; **fix**:
  errors from `jsonlint -v *.json`, update invalid json format of the file.

* **INVALID XML FORMAT**: Test file contains invalid xml format; **fix**:
  errors from `xmllint --noout *.xml`, update invalid xml format of the file.

## Updating the whitelist

Normally you must [fix all lint errors](#fixing-lint-errors). But in the
unusual case of error reports for things essential to certain tests or that
for other exceptional reasons shouldn't prevent a merge of a test, you can
update and commit the `lint.whitelist` file in the crosswalk-test-suite/tools/lint/
directory to suppress errors the lint tool would report for a test file.

To add a test file or directory to the whitelist, use the following format:

```
ERROR TYPE:file/name/pattern
```

For example, to whitelist the file `example/file.html` such that all
`TRAILING WHITESPACE` errors the lint tool would report for it are
suppressed, add the following line to the `lint.whitelist` file.

```
TRAILING WHITESPACE:example/file.html
```

To whitelist an entire directory rather than just one file, use the `*`
wildcard. For example, to whitelist the `example` directory such that all
`TRAILING WHITESPACE` errors the lint tool would report for any files in it
are suppressed, add the following line to the `lint.whitelist` file.

```
TRAILING WHITESPACE:example/*
```

If needed, you can also use the `*` wildcard to express other filename
patterns or directory-name patterns (just as you would when, e.g.,
executing shell commands from the command line).

Finally, to whitelist just one line in a file, use the following format:

```
ERROR TYPE:file/name/pattern:line_number
```

For example, to whitelist just line 128 of the file `example/file.html`
such that any `TRAILING WHITESPACE` error the lint tool would report for
that line is suppressed, add the following to the `lint.whitelist` file.

```
TRAILING WHITESPACE:example/file.html:128
```
