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
      skeleton: {
         enable: true
      },
      tracking: {
        enable: true
      },
      face: {
        enable: true
      },
      gesture: {
        enable: true
      },
      expression: {
        enable: true
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
  it('check personInfo interface: SkeletonData exist', function() {
    var skeletonInfo = person.skeletonInfo;
    assert.ok(skeletonInfo);
  });
  it('check personInfo interface: SkeletonData type', function() {
    var skeletonInfo = person.skeletonInfo;
    assert.ok(typeof(skeletonInfo) == 'object');
  });
  it('check personInfo interface: TrackingData exist', function() {
    var trackInfo = person.trackInfo;
    assert.ok(trackInfo);
  });
  it('check personInfo interface: TrackingData type', function() {
    var trackInfo = person.trackInfo;
    assert.ok(typeof(trackInfo) == 'object');
  });
  it('check personInfo interface: gestureInfo exist', function() {
    var gestureInfo = person.gestureInfo;
    assert.ok(gestureInfo);
  });
  it('check personInfo interface: gestureInfo type', function() {
    var gestureInfo = person.gestureInfo;
    assert.ok(typeof(gestureInfo) == 'object');
  });
  it('check personInfo interface: expressionInfo exist', function() {
    var expressInfo = person.expressionInfo;
    assert.ok(expressInfo);
  });
  it('check personInfo interface: expressInfo type', function() {
    var expressInfo = person.expressInfo;
    assert.ok(typeof(expressInfo) == 'object');
  });
  it('check personInfo interface: landmarkInfo exist', function() {
    var landmarkInfo = person.landmarkInfo;
    assert.ok(landmarkInfo);
  });
  it('check personInfo interface: landmarkInfo type', function() {
    var landmarkInfo = person.landmarkInfo;
    assert.ok(typeof(landmarkInfo) == 'object');
  });
  it('check personInfo interface: poseInfo exist', function() {
    var poseInfo = person.poseInfo;
    assert.ok(poseInfo);
  });
  it('check personInfo interface: poseInfo type', function() {
    var poseInfo = person.poseInfo;
    assert.ok(typeof(poseInfo) == 'object');
  });
});

