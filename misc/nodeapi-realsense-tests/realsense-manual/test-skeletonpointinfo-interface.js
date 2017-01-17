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
         enable: true,
         maxTrackedPerson: 1,
         trackingArea: "upper-body"
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
  it('check SkeletonPointInfo interface: jointType exist', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.ok(SkeletonPointInfo.jointType);
  });
  it('check SkeletonPointInfo interface: jointType type', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.equal(typeof(SkeletonPointInfo.jointType), 'object');
  });
  it('check SkeletonPointInfo interface: worldCoordinate exist', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.ok(SkeletonPointInfo.worldCoordinate);
  });
  it('check SkeletonPointInfo interface: worldCoordinate type', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.equal(typeof(SkeletonPointInfo.worldCoordinate), 'object');
  });
  it('check SkeletonPointInfo interface: imageCoordinate exist', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.ok(SkeletonPointInfo.imageCoordinate);
  });
  it('check SkeletonPointInfo interface: imageCoordinate type', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.equal(typeof(SkeletonPointInfo.imageCoordinate), 'object');
  });
  it('check SkeletonPointInfo interface: worldConfidence exist', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.ok(SkeletonPointInfo.worldConfidence);
  });
  it('check SkeletonPointInfo interface: worldConfidence type', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.equal(typeof(SkeletonPointInfo.worldConfidence), 'number');
  });
  it('check SkeletonPointInfo interface: imageConfidence exist', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.ok(SkeletonPointInfo.imageConfidence);
  });
  it('check SkeletonPointInfo interface: imageConfidence type', function() {
    var skeletonJoints = person.skeletonJoints;
    var SkeletonPointInfo = skeletonJoints[0];
    assert.equal(typeof(SkeletonPointInfo.imageConfidence), 'number');
  });
});

