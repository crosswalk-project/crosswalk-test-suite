module.exports = function (grunt) {
  var connect = require('connect');

  // a server task which hogs the console until it's killed with Ctrl-c
  grunt.task.registerTask('simple_server', 'Run dist code on a server', function () {
    var port = grunt.config('simple_server.port') || 20202;
    var dir = grunt.config('simple_server.dir') || 'dist';
    var cb = grunt.config('simple_server.callback') || null;

    // tells grunt not to let this task complete
    this.async();

    var app = connect.createServer()
    app.use('/', connect.static(dir));

    app.listen(port);

    grunt.log.writeln('Client is available at http://localhost:' + port + '/');

    if (cb) {
      cb(grunt.config('simple_server'));
    }
  });

};
