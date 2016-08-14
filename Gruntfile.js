var main_file = 'ariane/static/js/main.js';

module.exports = function(grunt) {

  grunt.initConfig({

    jshint: {
      files: ['Gruntfile.js', main_file, 'tests/jstests/tests.js'],
      options: {
        globals: {
          jQuery: true
        }
      }
    },

    qunit: {
      options: {
        '--web-security': 'no',
        coverage: {
          disposeCollector: true,
          src: [main_file],
          instrumentedFiles: 'temp/',
          htmlReport: 'jsreport/html-coverage',
          lcovReport: 'jsreport/',
          linesThresholdPct: 100
        }
      },
      all: ['tests/jstests/index.html']
    },

    watch: {
      files: ['ariane/static/scss/main.scss', 'ariane/static/scss/components/*.scss'],
      tasks: ['sass'],
      options: {
        'atBegin': true,
      }
    },

    uglify: {
      compile_vendor: {
        files: {
          'ariane/static/js/vendor/compiled.js': [
            'node_modules/modernizr/modernizr.js',
            'node_modules/zepto/dist/zepto.min.js',
            'node_modules/zepto/src/fx.js',
            'node_modules/zepto/src/fx_methods.js',
            'node_modules/knockout/build/output/knockout-latest.js',
            'node_modules/reconnectingwebsocket/reconnecting-websocket.min.js'
          ]
        }
      }
    },

    sass: {
      dist: {
        options: {trace: true},
        files: {
          'ariane/static/css/main.css': 'ariane/static/scss/main.scss',
        }
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-qunit-istanbul');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-sass');


  grunt.registerTask('default', ['jshint', 'qunit']);

};
