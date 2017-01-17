"use strict"
var emitter = require('events').EventEmitter;
const assert = require('assert');
var module = require('bindings')('realsense_pt');

function inherits(target, source) {
  for (var k in source.prototype) {
    target.prototype[k] = source.prototype[k];
  }
}

inherits(module.Instance, emitter);

  var PersonTrackingResult = null;
  var persons = null;
  var person =null;
  
    var instanceConfig = {
      skeleton: {enable: true, trackingArea: "upper-body"},
      tracking: {enable: true, enableSegmentation: true, enableFaceLandmarks: true, enableHeadPose: true, enableBlob: true, enablePersonOrientation: true, enableDetectionFromFar: true, detectMode: "auto"},
      lying: {enable: true},
      pose: {enable: true},
      face: {enable: true, policy: "standard", useMultiFrame: true},
      gesture: {enable: true},
      expression: {enable: true, enableAllExpressions: true}
    }
    var instance = new module.Instance(instanceConfig);
    instance.on('persontracked', function(result) {
      PersonTrackingResult = result;
      persons = PersonTrackingResult.persons;
      person = persons[0];
      console.log('-------');
      console.log(person);
      console.log('-------');
    });
    instance.start().then(function(){console.log('Start camera')});
