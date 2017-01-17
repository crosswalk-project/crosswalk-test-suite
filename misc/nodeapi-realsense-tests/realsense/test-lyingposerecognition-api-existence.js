"use strict"
const assert = require('assert');
var util = require('./util.js');
var module = require('bindings')('realsense_pt');

var instanceConfig = {};
instanceConfig = {
  lying: {
    enable: true,
    maxTrackedPerson:1
  }
};
var cameraConfig = {};
var instance = util.getObj(module, "LyingPoseRecognition", instanceConfig, cameraConfig).instance;
var obj = util.getObj(module, "LyingPoseRecognition", instanceConfig, cameraConfig).obj;
describe('LyingPoseRecognition API Test', function () {

  describe('API Existance', function() {
    it('module.LyingPoseRecognition is exist', function() {
      assert.ok(typeof(obj) !== 'undefined' )
    });

    it('module.LyingPoseRecognition type is correct', function() {
      assert.equal(typeof(obj),'object');
    });

    it('new module.LyingPoseRecognition() object has a method .setRecognitionState', function () {
      assert.equal(typeof(obj.setRecognitionState), 'function');
    });

    it('new module.LyingPoseRecognition() object has a method .getRecognitionState', function () {
      assert.equal(typeof(obj.getRecognitionState), 'function');
    });

    it('new module.LyingPoseRecognition() object has a method .getCandidatesCount', function () {
      assert.equal(typeof(obj.getCandidatesCount), 'function');
    });

    it('new module.LyingPoseRecognition() object has a method .getCandidatesData', function () {
      assert.equal(typeof(obj.getCandidatesData), 'function');
    });

  });

});
