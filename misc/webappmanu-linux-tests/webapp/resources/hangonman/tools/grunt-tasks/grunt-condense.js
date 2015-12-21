/*
condense script and link tags to a single instance of each in the
specified HTML file; like grunt-usemin but less confusing and more dumb

example config:

condense: {
  dist: {
    file: 'build/app/index.html',
    script: 'js/all.js',
    stylesheet: 'css/all.css'
  }
}
*/
module.exports = function (grunt) {
  var fs = require('fs');

  grunt.registerMultiTask('condense', 'Condense script and link elements', function () {
    var stylesheet = this.data.stylesheet;
    var script = this.data.script;
    var file = this.data.file;

    var content = fs.readFileSync(file, 'utf8');

    // remove all link and script elements with a src
    content = content.replace(/<link.+?>/g, '');
    content = content.replace(/<script.*?src.*?.+?><\/script>/g, '');

    // add single <script> just before the closing </body>
    var html = '<script async="async" src="' + script.src + '"';

    if (script.attrs) {
      for (var k in script.attrs) {
        html += ' ' + k + '="' + script.attrs[k] + '"';
      }
    }

    html += '></script></body>';
    content = content.replace(/<\/body>/, html);

    // add a single <link> just above the closing </head>
    html = '<link rel="stylesheet" href="' + stylesheet + '"></head>';
    content = content.replace(/<\/head>/, html);

    // overwrite the original file
    fs.writeFileSync(file, content, 'utf8');
  });
};
