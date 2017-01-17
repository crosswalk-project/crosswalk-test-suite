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
  
  before(function(done){
    var instanceConfig = {
      tracking: {
        enable: true,
      }
    }
    var instance = new module.Instance(instanceConfig);
    instance.on('persontracked', function(result) {
      PersonTrackingResult = result;
      persons = PersonTrackingResult.persons;
      done();
    });
    instance.start().then(function(){console.log('Start camera')});
    this.timeout(10000);
  })
  it('get PersonTrackingResult', function() {
    assert.ok(PersonTrackingResult!=null);
  });
  it('get persons of PersonTrackingResult', function() {
    var len = persons.length;
    assert.ok(persons != null && persons != undefined);
    assert.ok(typeof(persons) == 'object');
    assert.ok(len>0);
  });
});

