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
      gesture: {
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
    this.timeout(60000);
  })
  it('check GestureData interface: isPointing exist', function() {
    var gesttureInfo = person.gestureInfo;
    var isPointing = gesttureInfo.isPointing;
    assert.ok(isPointing != undefined);
  });
  it('check GestureData interface: isPointing type', function() {
    var gesttureInfo = person.gestureInfo;
    var isPointing = gesttureInfo.isPointing;
    assert.equal(typeof(isPointing), 'boolean');
  });
  it('check GestureData interface: thePointingInfo exist', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    assert.ok(thePointingInfo != undefined);
  });
  it('check GestureData interface: thePointingInfo type', function() {
    var gesttureInfo = person.gestureInfo;
    var thePointingInfo = gesttureInfo.thePointingInfo;
    assert.equal(typeof(thePointingInfo), 'object');
  });
});
