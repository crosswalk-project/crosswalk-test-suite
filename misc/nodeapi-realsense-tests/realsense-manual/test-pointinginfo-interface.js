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
  it('check PointingInfo interface: worldOrigin exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    assert.ok(worldOrigin != undefined);
  });
  it('check PointingInfo interface: worldOrigin type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    assert.equal(typeof(worldOrigin), 'object');
  });
  it('check PointingInfo interface: worldDirection exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldDirection = thePointingInfo.worldDirection;
    assert.ok(worldDirection != undefined);
  });
  it('check PointingInfo interface: worldDirection type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldDirection = thePointingInfo.worldDirection;
    assert.equal(typeof(worldDirection), 'object');
  });
  it('check PointingInfo interface: imageOrigin exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var imageOrigin = thePointingInfo.imageOrigin;
    assert.ok(imageOrigin != undefined);
  });
  it('check PointingInfo interface: imageOrigin type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var imageOrigin = thePointingInfo.imageOrigin;
    assert.equal(typeof(imageOrigin), 'object');
  });
  it('check PointingInfo interface: imageDirection exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var imageDirection = thePointingInfo.imageDirection;
    assert.ok(imageDirection != undefined);
  });
  it('check PointingInfo interface: imageDirection type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var imageDirection = thePointingInfo.imageDirection;
    assert.equal(typeof(imageDirection), 'object');
  });
  it('check PointingInfo interface: confidence exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var confidence = thePointingInfo.confidence;
    assert.ok(confidence != undefined);
  });
  it('check PointingInfo interface: confidence type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var confidence = thePointingInfo.confidence;
    assert.equal(typeof(confidence), 'number');
  });
  it('check PointingInfo interface: startTimeStamp exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var startTimeStamp = thePointingInfo.startTimeStamp;
    assert.ok(startTimeStamp != undefined);
  });
  it('check PointingInfo interface: startTimeStamp type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var startTimeStamp = thePointingInfo.startTimeStamp;
    assert.equal(typeof(startTimeStamp), 'number');
  });
});
