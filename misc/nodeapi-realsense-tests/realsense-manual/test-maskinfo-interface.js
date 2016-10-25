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
  it('check MaskInfo interface: width exist', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    var width = blobMask.width;
    assert.ok(width != undefined);
  });
  it('check MaskInfo interface: width type', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    var width = blobMask.width;
    assert.equal(typeof(width), 'number');
  });
  it('check MaskInfo interface: height exist', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    var height = blobMask.height;
    assert.ok(height != undefined);
  });
  it('check MaskInfo interface: height type', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    var height = blobMask.height;
    assert.equal(typeof(height), 'number');
  });
  it('check MaskInfo interface: maskData exist', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    var maskData= blobMask.maskData;
    assert.ok(maskData != undefined);
  });
  it('check MaskInfo interface: maskData type', function() {
    var trackInfo = person.trackInfo;
    var blobMask = trackInfo.blobMask;
    var maskData= blobMask.maskData;
    assert.equal(typeof(maskData), 'object');
  });
});
