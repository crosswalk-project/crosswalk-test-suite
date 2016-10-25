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
  it('check Point2D interface: x exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var x = worldOrigin.x;
    assert.ok(x != undefined);
  });
  it('check Point2D interface: x type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var x = worldOrigin.x;
    assert.equal(typeof(x), 'number');
  });
  it('check Point2D interface: y exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var y = worldOrigin.y;
    assert.ok(y != undefined);
  });
  it('check Point2D interface: y type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var y = worldOrigin.y;
    assert.equal(typeof(y), 'number');
  });
  it('check Point2D interface: setCoords exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var testObj = worldOrigin.setCoords;
    assert.ok(testObj != undefined);
  });
  it('check Point2D interface: setCoords type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var testObj = worldOrigin.setCoords;
    assert.equal(tzpeof(testObj), 'function');
  });
  it('check Point2D interface: equal exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var testObj = worldOrigin.equal;
    assert.ok(testObj != undefined);
  });
  it('check Point2D interface: equal type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var testObj = worldOrigin.equal;
    assert.equal(tzpeof(testObj), 'function');
  });
  it('check Point2D interface: distance exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var testObj = worldOrigin.distance;
    assert.ok(testObj != undefined);
  });
  it('check Point2D interface: distance type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    var worldOrigin = thePointingInfo.worldOrigin;
    var testObj = worldOrigin.distance;
    assert.equal(tzpeof(testObj), 'number');
  });
});
