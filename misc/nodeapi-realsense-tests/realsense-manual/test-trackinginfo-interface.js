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
  it('check TrackingData interface: id exist', function() {
    var trackInfo = person.trackInfo;
    var id = trackInfo.id;
    assert.ok(id != undefined);
  });
  it('check TrackingData interface: id type', function() {
    var trackInfo = person.trackInfo;
    var id = trackInfo.id;
    assert.equal(typeof(id), 'number');
  });
  it('check TrackingData interface: boundingBox exist', function() {
    var trackInfo = person.trackInfo;
    var boundingBox= trackInfo.boundingBox;
    assert.ok(boundingBox != undefined);
  });
  it('check TrackingData interface: boundingBox type', function() {
    var trackInfo = person.trackInfo;
    var boundingBox= trackInfo.boundingBox;
    assert.equal(typeof(boundingBox), 'object');
  });
  it('check TrackingData interface: center exist', function() {
    var trackInfo = person.trackInfo;
    var center = trackInfo.center;
    assert.ok(center != undefined);
  });
  it('check TrackingData interface: center type', function() {
    var trackInfo = person.trackInfo;
    var center = trackInfo.center;
    assert.equal(typeof(center), 'object');
  });
  it('check TrackingData interface: headBoundingBox exist', function() {
    var trackInfo = person.trackInfo;
    var headBoundingBox = trackInfo.headBoundingBox;
    assert.ok(headBoundingBox != undefined);
  });
  it('check TrackingData interface: headBoundingBox type', function() {
    var trackInfo = person.trackInfo;
    var headBoundingBox = trackInfo.headBoundingBox;
    assert.equal(typeof(headBoundingBox), 'object');
  });
  it('check TrackingData interface: segmentationMask exist', function() {
    var trackInfo = person.trackInfo;
    var segmentationMask = trackInfo.segmentationMask;
    assert.ok(segmentationMask != undefined);
  });
  it('check TrackingData interface: segmentationMask type', function() {
    var trackInfo = person.trackInfo;
    var segmentationMask = trackInfo.segmentationMask;
    assert.equal(typeof(segmentationMask), 'object');
  });
  it('check TrackingData interface: blobMask exist', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    assert.ok(blobMask != undefined);
  });
  it('check TrackingData interface: blobMask type', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    assert.equal(typeof(blobMask), 'object');
  });
  it('check TrackingData interface: headPose exist', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    assert.ok(headPose != undefined);
  });
  it('check TrackingData interface: headPose type', function() {
    var trackInfo = person.trackInfo;
    var headPose = trackInfo.headPose;
    assert.equal(typeof(headPose), 'object');
  });
  it('check TrackingData interface: orient exist', function() {
    var trackInfo = person.trackInfo;
    var orient = trackInfo.orient;
    assert.ok(orient != undefined);
  });
  it('check TrackingData interface: orient type', function() {
    var trackInfo = person.trackInfo;
    var orient = trackInfo.orient;
    assert.equal(typeof(orient), 'object');
  });
});

