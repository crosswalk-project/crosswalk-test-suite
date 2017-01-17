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
  it('check SkeletonInfo interface: skeletonJoints', function() {
    var skeletonJoints = person.skeletonInfo.skeletonJoints;
    var len = skeletonJoints.length;
    assert.ok(skeletonJoints);
    assert.ok(typeof(skeletonJoints) == 'object');
    assert.ok(len > 0);
  });
});

