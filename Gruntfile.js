var files = ['ariane/static/js/main.js'];

module.exports = function(grunt) {

  grunt.initConfig({
    jshint: {
      files: ['Gruntfile.js'].concat(files).concat(['tests/jstests/tests.js']),
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
          src: files,
          instrumentedFiles: 'temp/',
          htmlReport: 'jsreport/html-coverage',
          lcovReport: 'jsreport/',
          linesThresholdPct: 100
        }
      },
      all: ['tests/jstests/index.html']
    },

    watch: {
      files: files,
      tasks: ['jshint', 'qunit'],
      options: {
        'atBegin': true,
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-qunit-istanbul');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['jshint', 'qunit']);

};
