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
var boolean_group = [true, false];
var number_group = [0, 1, 2];
var trackingArea = ['upper-body', 'upper-body-rough', 'full-body-rough', 'full-body'];

var SkeletonConfig_enable = boolean_group;
var SkeletonConfig_maxTrackedPerson = number_group;
var SkeletonConfig_trackingArea = trackingArea;

function _test(i) {
  describe('check enum SkeletonArea', function(done){
      it('checking member of SkeletonArea: '+ i.enable + i.maxTrackedPerson + i.trackingArea, function(done) {
        var cfg = {};
        cfg['skeleton'] = i;
        console.log(cfg);
        var instance = new module.Instance(cfg);
        instance.start().then(function(){
          console.log('Start camera');
          instance.stop().then(function(){console.log('Stop camera');});
          assert.ok(true);
          done();
        }).catch(function(){
          instance.stop().then(function(){console.log('Stop camera');});
          assert.ok(false);
          done();
        });
      });
  });
}

for (var i in SkeletonConfig_enable) {
  for (var j in SkeletonConfig_maxTrackedPerson) {
    for (var k in SkeletonConfig_trackingArea) {
      var config = {enable: SkeletonConfig_enable[i],
                    maxTrackedPerson: SkeletonConfig_maxTrackedPerson[j],
                    trackingArea: SkeletonConfig_trackingArea[k]
                   } 
      console.log(config);
      _test(config);
    }
  }
}
