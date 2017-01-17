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

describe('check PersonTrackingResult', function(done){
  var PersonTrackingResult = null;
  var persons = null;
  var person =null;
  
  before(function(done){
    var instanceConfig = {
      tracking: {
         enable: true,
         enableSegmentation: true,
         enableHeadPose: true,
         enableBlob: true,
         enablePersonOrientation: true,
         enableHeadBoundingBox: true,
         enableFaceLandmarks: true,
         enableDetectionFromFar: true,
         maxTrackedPerson: 1,
         detectMode: 'auto'
      }
    }
    var instance = new module.Instance(instanceConfig);
    instance.on('persontracked', function(result) {
      PersonTrackingResult = result;
      persons = PersonTrackingResult.persons;
      person = persons[0];
      done();
    });
    instance.start().then(function(){console.log('Start camera')});
    this.timeout(10000);
  })
  it('check PoseEulerAngles interface: yaw exist', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    var yaw = headPose.yaw;
    assert.ok(yaw);
  });
  it('check PoseEulerAngles interface: yaw type', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    var yaw = headPose.yaw;
    assert.ok(typeof(yaw), 'number');
  });
  it('check PoseEulerAngles interface: pitch exist', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    var pitch = headPose.pitch;
    assert.ok(pitch);
  });
  it('check PoseEulerAngles interface: pitch type', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    var pitch = headPose.pitch;
    assert.ok(typeof(pitch), 'number');
  });
  it('check PoseEulerAngles interface: roll exist', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    var roll = headPose.roll;
    assert.ok(roll);
  });
  it('check PoseEulerAngles interface: roll type', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    var roll = headPose.roll;
    assert.equal(typeof(roll), 'number');
  });
});
