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
var instance = util.getObj(module, "Instance", instanceConfig, cameraConfig).instance;
var obj = util.getObj(module, "Instance", instanceConfig, cameraConfig).obj;
describe('Instance API Test', function () {

  describe('API Existance', function() {
    it('module.Instance is exist', function() {
      assert.ok(typeof(obj) !== 'undefined' )
    });

    it('module.Instance type is correct', function() {
      assert.equal(typeof(obj),'object');
    });

    it('module.Instance() object has the attribute state', function () {
      assert.ok(obj.state !== undefined );
    });
    it('module.Instance() object has the object attribute state', function () {
      assert.equal(typeof(obj.state),'object');
    });

    it('module.Instance() object has the readonly attribute state', function () {
      assert.throws(() => {obj.state = null});
    });

    it('new module.Instance() object has a method .getInstanceOptions', function () {
      assert.equal(typeof(obj.getInstanceOptions), 'function');
    });

    it('new module.Instance() object has a method .setInstanceOptions', function () {
      assert.equal(typeof(obj.setInstanceOptions), 'function');
    });

    it('new module.Instance() object has a method .start', function () {
      assert.equal(typeof(obj.start), 'function');
    });

    it('new module.Instance() object has a method .stop', function () {
      assert.equal(typeof(obj.stop), 'function');
    });

    it('new module.Instance() object has a method .pause', function () {
      assert.equal(typeof(obj.pause), 'function');
    });

    it('new module.Instance() object has a method .resume', function () {
      assert.equal(typeof(obj.resume), 'function');
    });

    it('new module.Instance() object has a method .reset', function () {
      assert.equal(typeof(obj.reset), 'function');
    });

    it('module.Instance() object has the attribute faceRecognition', function () {
      assert.ok(obj.faceRecognition !== undefined );
    });
    it('module.Instance() object has the object attribute faceRecognition', function () {
      assert.equal(typeof(obj.faceRecognition),'object');
    });

    it('module.Instance() object has the readonly attribute faceRecognition', function () {
      assert.throws(() => {obj.faceRecognition = null});
    });

    it('module.Instance() object has the attribute lyingPoseRecognition', function () {
      assert.ok(obj.lyingPoseRecognition !== undefined );
    });
    it('module.Instance() object has the object attribute lyingPoseRecognition', function () {
      assert.equal(typeof(obj.lyingPoseRecognition),'object');
    });

    it('module.Instance() object has the readonly attribute lyingPoseRecognition', function () {
      assert.throws(() => {obj.lyingPoseRecognition = null});
    });

    it('module.Instance() object has the attribute personTracking', function () {
      assert.ok(obj.personTracking !== undefined );
    });
    it('module.Instance() object has the object attribute personTracking', function () {
      assert.equal(typeof(obj.personTracking),'object');
    });

    it('module.Instance() object has the readonly attribute personTracking', function () {
      assert.throws(() => {obj.personTracking = null});
    });

  });

});
