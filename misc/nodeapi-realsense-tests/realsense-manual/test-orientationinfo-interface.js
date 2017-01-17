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
  it('check OrientationInfo interface: orientType exist', function() {
    var trackInfo = person.trackInfo;
    var orient = trackInfo.orient;
    var orientType = orient.orientType;
    assert.ok(orientType != undefined);
  });
  it('check OrientationInfo interface: orientType type', function() {
    var trackInfo = person.trackInfo;
    var orient = trackInfo.orient;
    var orientType = orient.orientType;
    assert.equal(typeof(orientType), 'string');
  });
  it('check OrientationInfo interface: confidence exist', function() {
    var trackInfo = person.trackInfo;
    var orient = trackInfo.orient;
    var confidence = orient.confidence;
    assert.ok(confidence != undefined);
  });
  it('check OrientationInfo interface: confidence type', function() {
    var trackInfo = person.trackInfo;
    var orient = trackInfo.orient;
    var confidence = orient.confidence;
    assert.equal(typeof(confidence), 'number');
  });
});
