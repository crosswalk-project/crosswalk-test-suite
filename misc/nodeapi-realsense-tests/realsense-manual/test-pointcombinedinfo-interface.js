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
  it('check PointCombinedInfo interface: rect exist', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var worldCoordinate = center.worldCoordinate;
    assert.ok(worldCoordinate);
  });
  it('check PointCombinedInfo interface: rect type', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var worldCoordinate = center.worldCoordinate;
    assert.equal(typeof(worldCoordinate), 'object');
  });
  it('check PointCombinedInfo interface: imageCoordinate exist', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var imageCoordinate = center.imageCoordinate;
    assert.ok(imageCoordinate);
  });
  it('check PointCombinedInfo interface: imageCoordinate type', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var imageCoordinate = center.imageCoordinate;
    assert.equal(typeof(imageCoordinate), 'object');
  });
  it('check PointCombinedInfo interface: worldConfidence exist', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var worldConfidence = center.worldConfidence;
    assert.ok(worldConfidence);
  });
  it('check PointCombinedInfo interface: worldConfidence type', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var worldConfidence = center.worldConfidence;
    assert.equal(typeof(worldConfidence), 'number');
  });
  it('check PointCombinedInfo interface: imageConfidence exist', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var imageConfidence = center.imageConfidence;
    assert.ok(imageConfidence);
  });
  it('check PointCombinedInfo interface: imageConfidence type', function() {
    var trackInfo = person.trackInfo;
    var center= trackInfo.center;
    var imageConfidence = center.imageConfidence;
    assert.equal(typeof(imageConfidence), 'number');
  });
});

