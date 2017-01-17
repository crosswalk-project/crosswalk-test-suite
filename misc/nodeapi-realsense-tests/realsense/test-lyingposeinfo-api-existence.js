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
var instance = util.getObj(module, "LyingPoseInfo", instanceConfig, cameraConfig).instance;
var obj = util.getObj(module, "LyingPoseInfo", instanceConfig, cameraConfig).obj;
describe('LyingPoseInfo API Test', function () {

  describe('API Existance', function() {
    it('module.LyingPoseInfo is exist', function() {
      assert.ok(typeof(obj) !== 'undefined' )
    });

    it('module.LyingPoseInfo type is correct', function() {
      assert.equal(typeof(obj),'object');
    });

    it('module.LyingPoseInfo() object has the attribute position', function () {
      assert.ok(obj.position !== undefined );
    });
    it('module.LyingPoseInfo() object has the object attribute position', function () {
      assert.equal(typeof(obj.position),'object');
    });

    it('module.LyingPoseInfo() object has the writable attribute position', function () {
      var tmp;
      tmp = obj.position;
      obj.position = null;
      assert.notEqual(tmp, obj.position);
    });

    it('module.LyingPoseInfo() object has the attribute boundingBox', function () {
      assert.ok(obj.boundingBox !== undefined );
    });
    it('module.LyingPoseInfo() object has the object attribute boundingBox', function () {
      assert.equal(typeof(obj.boundingBox),'object');
    });

    it('module.LyingPoseInfo() object has the writable attribute boundingBox', function () {
      var tmp;
      tmp = obj.boundingBox;
      obj.boundingBox = null;
      assert.notEqual(tmp, obj.boundingBox);
    });

    it('module.LyingPoseInfo() object has the attribute result', function () {
      assert.ok(obj.result !== undefined );
    });
    it('module.LyingPoseInfo() object has the object attribute result', function () {
      assert.equal(typeof(obj.result),'object');
    });

    it('module.LyingPoseInfo() object has the writable attribute result', function () {
      var tmp;
      tmp = obj.result;
      obj.result = null;
      assert.notEqual(tmp, obj.result);
    });

    it('module.LyingPoseInfo() object has the attribute confidence', function () {
      assert.ok(obj.confidence !== undefined );
    });
    it('module.LyingPoseInfo() object has the number attribute confidence', function () {
      assert.equal(typeof(obj.confidence),'number');
    });

    it('module.LyingPoseInfo() object has the writable attribute confidence', function () {
      var tmp;
      tmp = obj.confidence;
      obj.confidence = NaN;
      assert.notEqual(tmp, obj.confidence);
    });

  });

});
