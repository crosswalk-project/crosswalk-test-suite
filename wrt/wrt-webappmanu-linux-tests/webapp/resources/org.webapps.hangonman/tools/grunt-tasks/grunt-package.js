module.exports = function (grunt) {
  var path = require('path');
  var fs = require('fs');
  var async = require('async');
  var Zip = require('node-native-zip');

  /**
  * Create a zip file with a customisable filename.
  *
  * Deps: node-native-zip, async
  *
  * Format of the output filename is:
  *
  *   <appName>_<version>_git@<commitID>_YYYY-MM-DD_HHMMSS_<suffix>.zip
  *
  * The git, version and suffix parts are optional (see below for
  * configuration).
  *
  * Configuration options:
  *
  *   appName - the name of the application; used as the base filename
  *   files - glob of files to zip TODO allow array of globs
  *   suffix - zip file suffix (default 'zip')
  *   outDir - output directory to put the zipfile into
  *   version - application version
  *   stripPrefix - if dir has a folder hierarchy inside it, specify
  *                 the prefix to strip from all paths, to remove
  *                 the embedded folders (default = '')
  *   addGitCommitId - if the project is a git repo, this includes the
  *                    8 character variant of the last commit ID as
  *                    part of the filename, e.g.
  *                    app_git@81a131a2_2012-11-01_1151.zip
  *                    (default = false)
  *
  * Example configuration:
  *
  * grunt.initConfig({
  *   package: {
  *     wgt: {
  *       appName: 'app',
  *       suffix: 'wgt',
  *       version: '0.1.0',
  *       addGitCommitId: true,
  *       files: 'build/dist/**',
  *       stripPrefix: 'build/dist',
  *       outDir: 'build'
  *     }
  *   }
  * });
  *
  * In this example, we zip up the files matching build/dist/**.
  * Inside the zip file, the directory structure has the build/dist
  * prefix stripped, so our zipfile structure matches the structure
  * under the build/dist directory. The zipfile goes into the build/
  * directory. The output zipfile name also contains the latest
  * git commit ID and has the suffix .zip
  *
  * A pre-suffix is added if you pass an identifier string to this task
  * when calling it, e.g.
  *
  *   grunt package:TEST
  *
  * will produce an output file with name like
  *
  *   app_2012-11-01_1149_TEST.zip
  *
  * To do this as part of your own custom task, modify your
  * gruntfile like this:
  *
  * grunt.registerTask('pkg', 'create package', function (identifier) {
  *    // ...do other tasks here, e.g. minify and copy files for distribution...
  *
  *    var packageTask = (identifier ? 'package:' + identifier : 'package');
  *    grunt.task.run(packageTask);
  *  });
  *
  * then call it with pkg:TEST, where TEST is the string
  * you want to append to the output filename.
  */
  grunt.registerMultiTask('package', 'Zip files with custom zipfile name', function (identifier) {
    var appName = this.data.appName;
    var version = this.data.version;
    var files = this.data.files;
    var suffix = this.data.suffix || 'zip';
    var outDir = this.data.outDir || '.';
    var addGitCommitId = !!this.data.addGitCommitId;

    // this is removed from the path of each file as it is added to the zip
    var stripPrefix = this.data.stripPrefix || '';
    stripPrefix = new RegExp('^' + stripPrefix);

    if (!appName) {
      grunt.fatal('package task requires appName argument');
    }

    if (!version) {
      grunt.fatal('package task requires version argument (x.x.x)');
    }

    if (!files) {
      grunt.fatal('package task requires dir argument (directory to zip)');
    }

    files = grunt.file.expand(files);

    var done = this.async();

    var outFile = appName;

    // get the latest commit ID as an 8-character string;
    // if not a git repo, returns '' and logs an error;
    // receiver is a function with the signature receiver(err, result),
    // where err is null if no error occurred and result is the commit ID
    var gitCommitId = function (receiver) {
      grunt.util.spawn(
        {
          cmd: "git",
          args: ["log", "-n1", "--format=format:'%h'"]
        },

        function (err, result) {
          if (err) {
            receiver(true, '');
          }
          else {
            receiver(null, result.stdout.replace(/'/g, ''));
          }
        }
      );
    };

    var isFile = function (path) {
      if (!fs.existsSync(path) || fs.statSync(path).isDirectory()) {
        return false;
      }

      return true;
    };

    var packFiles = function (outfile, infiles, cb) {
      var zipfile = new Zip();
      var buffer;

      async.forEachSeries(
        infiles,
        function (file, next) {
          if (isFile(file)) {
            var filename = file.replace(stripPrefix, '');

            grunt.log.writeln('adding ' + file + ' to package as ' + filename);

            buffer = fs.readFileSync(file);

            zipfile.add(filename, buffer);

            next();
          }
          else {
            next();
          }
        },
        function (err, result) {
          grunt.log.writeln('\npackage written to:\n' + outfile);
          buffer = zipfile.toBuffer();
          fs.writeFile(outfile, buffer, cb);
        }
      );
    };

    var receiver = function (err, result) {
      if (version) {
        outFile += '_' + version;
      }

      if (result) {
        outFile += '_git@' + result;
      }

      outFile += '_' + grunt.template.today("yyyy-mm-dd_HHMMss");

      if (identifier) {
        outFile += '_' + identifier;
      }

      outFile += '.' + suffix.replace(/^\./, '');
      outFile = path.join(outDir, outFile);

      packFiles(outFile, files, done);
    };

    // append git commit ID to the package name
    if (addGitCommitId) {
      gitCommitId(receiver);
    }
    else {
      receiver(false, null);
    }
  });

};
