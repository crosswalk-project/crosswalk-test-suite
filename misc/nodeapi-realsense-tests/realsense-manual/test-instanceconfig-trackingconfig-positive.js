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
//var boolean_group = [true, false];
var boolean_group = [true];
//var number_group = [0, 1, 2];
var number_group = [1];
//var trackingMode = ['following', 'interactive', 'single-person'];
var trackingMode = ['following','interactive'];
//var detectMode = ['auto', 'close-range', 'mid-range', 'far-range', 'all'];
var detectMode = ['auto'];

var TrackingConfig_enable = boolean_group;
var TrackingConfig_enableSegmentation = boolean_group;
var TrackingConfig_enableHeadPose = boolean_group;
var TrackingConfig_enableBlob = boolean_group;
var TrackingConfig_enablePersonOrientation = boolean_group;
var TrackingConfig_enableHeadBoundingBox = boolean_group;
var TrackingConfig_enableFaceLandmarks = boolean_group;
var TrackingConfig_enableDetectionFromFar = boolean_group;
var TrackingConfig_maxTrackedPerson = number_group;
var TrackingConfig_trackingMode = trackingMode;
var TrackingConfig_detectMode = detectMode;

function _test(i) {
  describe('check enum SkeletonArea', function(done){
      it('checking member of SkeletonArea: '+ 
          i.enable + ' ' + 
          i.enableSegmentation + ' ' +
          i.enableHeadPose + ' ' +
          i.enableBlob + ' ' +
          i.enablePersonOrientation + ' ' +
          i.enableHeadBoundingBox + ' ' +
          i.enableFaceLandmarks + ' ' +
          i.enableDetectionFromFar+ ' ' +
          i.maxTrackedPerson+ ' ' +
          i.trackingMode + ' ' +
          i.detectMode, function(done) {
        var cfg = {};
        cfg['tracking'] = i;
        var instance = new module.Instance(cfg);
        instance.start().then(function(){
          console.log('Start camera');
          //instance.stop().then(function(){console.log('Stop camera');});
          assert.ok(true);
          done();
        }).catch(function(){
          //instance.stop().then(function(){console.log('Stop camera');});
          assert.ok(false);
          done();
        });
      });
  });
}

for (var i in TrackingConfig_enable) {
  for (var j in TrackingConfig_enableSegmentation) {
    for (var k in TrackingConfig_enableHeadPose) {
      for (var l in TrackingConfig_enableBlob) {
        for (var m in TrackingConfig_enablePersonOrientation) {
          for (var n in TrackingConfig_enableHeadBoundingBox) {
            for (var o in TrackingConfig_enableFaceLandmarks) {
              for (var p in TrackingConfig_enableDetectionFromFar) {
                for (var q in TrackingConfig_maxTrackedPerson) {
                  for (var r in TrackingConfig_trackingMode) {
                    for (var s in TrackingConfig_detectMode) {
                      var config = {enable: TrackingConfig_enable[i],
                                    enableSegmentation: TrackingConfig_enableSegmentation[j],
                                    enableHeadPose: TrackingConfig_enableHeadPose[k],
                                    enableBlob: TrackingConfig_enableBlob[l],
                                    enablePersonOrientation: TrackingConfig_enablePersonOrientation[m],
                                    enableHeadBoundingBox: TrackingConfig_enableHeadBoundingBox[n],
                                    enableFaceLandmarks: TrackingConfig_enableFaceLandmarks[o],
                                    enableDetectionFromFar: TrackingConfig_enableDetectionFromFar[p],
                                    maxTrackedPerson: TrackingConfig_maxTrackedPerson[q],
                                    trackingMode: TrackingConfig_trackingMode[r],
                                    detectMode: TrackingConfig_detectMode[s]
                                   } 
                      _test(config);
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
