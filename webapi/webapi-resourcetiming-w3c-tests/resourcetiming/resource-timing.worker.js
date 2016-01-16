importScripts("../resources/testharness.js");
importScripts("../resources/testharnessreport.js");

function cleanup() {
  performance.clearMarks();
  performance.clearMeasures();
}

function doTask() {
  var task;
  for(var i = 1; i <= 100; i++) {
    task = 1 * i;
  }
}

test(function() {
  cleanup();
  performance.mark("startMark");
  doTask();
  performance.mark("endMark");
  performance.measure("measure", "startMark", "endMark");
  var startMark = performance.getEntriesByName("startMark")[0];
  var endMark = performance.getEntriesByName("endMark")[0];
  var measure = performance.getEntriesByType("measure")[0];
  assert_equals(measure.name, "measure");
  assert_equals(measure.entryType, "measure");
  assert_equals(measure.startTime, startMark.startTime);
  assert_equals(performance.getEntriesByType("mark").length, 2);
  assert_equals(performance.getEntriesByType("measure").length, 1);
  performance.clearMarks("startMark");
  performance.clearMeasures("measure");
  assert_equals(performance.getEntriesByType("mark").length, 1);
  assert_equals(performance.getEntriesByType("measure").length, 0);
}, "Check that Performance timeline in Web Workers");

async_test(function(t) {
      var expectedResources = [ '/resources/testharness.js',
                                '/resources/testharnessreport.js' ];
      var resources = performance.getEntriesByType("resource");
      assert_equals(resources.length, expectedResources.length);
      for(var i=0; i< resources.length; i++) {
        assert_greater_than(resources[i].startTime, 0);
        assert_equals(resources[i].workerStart, 0);
        assert_greater_than(resources[i].responseEnd, resources[i].startTime);
      }
      performance.onresourcetimingbufferfull = t.step_func_done(function() {
        performance.clearResourceTimings();
        assert_equals(performance.getEntriesByType('resource').length, 0);
      });
      performance.setResourceTimingBufferSize(expectedResources.length);
}, "Check that Resource Timing in Web Workers");

done();
