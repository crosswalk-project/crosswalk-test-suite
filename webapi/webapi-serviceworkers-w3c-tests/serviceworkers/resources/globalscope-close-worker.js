importScripts("../../resources/testharness.js");
importScripts("../w3c/cache-storage/resources/test-helpers.js");

test(function() {
  assert_throws({name: 'InvalidAccessError'}, function() {
    self.close();
  });
}, "Check that ServiceWorkerGlobalScope.close() should throw an an 'InvalidAccessError' exception.");
