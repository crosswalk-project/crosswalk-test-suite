/*
Copyright (c) 2014 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Xia, Junchen <junchen.xia@intel.com>
*/

module.exports = function(grunt) {
  'use strict';

  grunt.initConfig({

    pkg: grunt.file.readJSON('package.json'),

    jsbeautifier: {
      all: ['../../**/*.{js,json}',
        '!../../**/{resources,testkit,common,w3c}/**/*.{js,json}'
      ],

      dirList: ['../../' + grunt.option('target') + '/**/*.{js,json}',
        '!../../' + grunt.option('target') + '/**/{resources,testkit,common,w3c}/**/*.{js,json}',
      ],

      options: {
        "indent_size": 2,
        "indent_char": " ",
        //Initial indentation level
        "indent_level": 0,
        "indent_with_tabs": false,
        //Preserve line-breaks
        "preserve_newlines": true,
        //Number of line-breaks to be preserved in one chunk
        "max_preserve_newlines": 3,
        //Enable jslint-stricter mode
        "jslint_happy": false,
        // [collapse|expand|end-expand]
        "brace_style": "collapse",
        // Preserve array indentation
        "keep_array_indentation": true,
        // Preserve array indentation
        "keep_function_indentation": false,
        "space_before_conditional": true,
        "break_chained_methods": false,
        "eval_code": false,
        "wrap_line_length": 0,
        "unescape_strings": false
      }
    },
    cssbeautifier: {
      all: ['../../**/*.css',
        '!../../**/{resources,testkit,common,w3c}/**/*.css',
      ],
      dirList: ['../../' + grunt.option('target') + '/**/*.css',
        '!../../' + grunt.option('target') + '/**/{resources,testkit,common,w3c}/**/*.css',
      ],

      options: {
        indent: '  ',
        // separate-line or end of line
        openbrace: 'end-of-line',
        autosemicolon: false
      }
    },
    // Styling HTML & XML files
    prettify: {
      options: {
        "indent_size": 2,
        "indent_char": " ",
        // keep, normal, separate
        "indent_scripts": "normal",
        // collapse, expand, end-expand
        "brace_style": "collapse",
        // Maximum characters allowed per line. Use `0` to disable.
        "max_char": 0,
        "unformatted": ["pre", "code"],
      },

      all: {
        expand: true,
        cwd: '../../',
        src: ['**/*.{html,xml}',
          '!**/{resources,common,testkit,w3c}/**/*.{html,xml}'
        ],
        dest: '../../'
      },

      dirList: {
        expand: true,
        cwd: '../../',
        src: [grunt.option('target') + '/**/*.{html,xml}',
          '!' + grunt.option('target') + '/**/{resources,common,testkit,w3c}/**/*.{html,xml}',
        ],
        dest: '../../'
      }

    }

  });

  grunt.loadNpmTasks('grunt-jsbeautifier');
  grunt.loadNpmTasks('grunt-cssbeautifier');
  grunt.loadNpmTasks('grunt-prettify');
  grunt.registerTask('all', ['jsbeautifier:all', 'cssbeautifier:all', 'prettify:all']);
  grunt.registerTask('dir', ['jsbeautifier:dirList', 'cssbeautifier:dirList', 'prettify:dirList']);
};
