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
         trackingMode: 'following',
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
  it('check BoundingBox2DInfo interface: rect exist', function() {
    var trackInfo = person.trackInfo;
    var boundingBox = trackInfo.boundingBox;
    var rect = boundingBox.rect;
    assert.ok(rect);
  });
  it('check BoundingBox2DInfo interface: rect type', function() {
    var trackInfo = person.trackInfo;
    var boundingBox = trackInfo.boundingBox;
    var rect = boundingBox.rect;
    assert.equal(typeof(rect), 'object');
  });
  it('check BoundingBox2DInfo interface: confidence exist', function() {
    var trackInfo = person.trackInfo;
    var boundingBox = trackInfo.boundingBox;
    var confidence = boundingBox.confidence;
    assert.ok(confidence);
  });
  it('check BoundingBox2DInfo interface: confidence type', function() {
    var trackInfo = person.trackInfo;
    var boundingBox = trackInfo.boundingBox;
    var confidence = boundingBox.confidence;
    assert.equal(typeof(confidence), 'number');
  });
});

