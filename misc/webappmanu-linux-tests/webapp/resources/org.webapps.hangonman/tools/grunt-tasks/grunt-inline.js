/*
 * Inline a JS file at the end of an HTML file
 * (just before the closing </body> tag)
 *
 * Configure with grunt.initConfig(), e.g.
 *
 * grunt.initConfig({
 *   inline: {
 *     script: '<path to script file>',
 *     htmlFile: '<path to HTML file>'
 *   }
 * });
 */
module.exports = function (grunt) {
  var fs = require('fs');

  grunt.registerTask('inline', 'Append script to HTML file', function () {
    var script = grunt.config('inline.script');
    var htmlFile = grunt.config('inline.htmlFile');

    var js = fs.readFileSync(script, 'utf8');

    var html = fs.readFileSync(htmlFile, 'utf8');
    html = html.replace('</body>', '<script>' + js + '</script></body>');

    fs.writeFileSync(htmlFile, html);
  });
};
