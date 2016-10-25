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
var instance = util.getObj(module, "FaceRecognition", instanceConfig, cameraConfig).instance;
var obj = util.getObj(module, "FaceRecognition", instanceConfig, cameraConfig).obj;
describe('FaceRecognition API Test', function () {

  describe('API Existance', function() {
    it('module.FaceRecognition is exist', function() {
      assert.ok(typeof(obj) !== 'undefined' )
    });

    it('module.FaceRecognition type is correct', function() {
      assert.equal(typeof(obj),'object');
    });

    it('new module.FaceRecognition() object has a method .getRegisteredIDs', function () {
      assert.equal(typeof(obj.getRegisteredIDs), 'function');
    });

    it('new module.FaceRecognition() object has a method .clearDatabase', function () {
      assert.equal(typeof(obj.clearDatabase), 'function');
    });

    it('new module.FaceRecognition() object has a method .exportDatabase', function () {
      assert.equal(typeof(obj.exportDatabase), 'function');
    });

    it('new module.FaceRecognition() object has a method .importDatabase', function () {
      assert.equal(typeof(obj.importDatabase), 'function');
    });

    it('new module.FaceRecognition() object has a method .recognizeAll', function () {
      assert.equal(typeof(obj.recognizeAll), 'function');
    });

    it('new module.FaceRecognition() object has a method .registerPerson', function () {
      assert.equal(typeof(obj.registerPerson), 'function');
    });

    it('new module.FaceRecognition() object has a method .unRegisterPerson', function () {
      assert.equal(typeof(obj.unRegisterPerson), 'function');
    });

    it('new module.FaceRecognition() object has a method .isPersonRegistered', function () {
      assert.equal(typeof(obj.isPersonRegistered), 'function');
    });

    it('new module.FaceRecognition() object has a method .reinforceRegistration', function () {
      assert.equal(typeof(obj.reinforceRegistration), 'function');
    });

    it('new module.FaceRecognition() object has a method .recognize', function () {
      assert.equal(typeof(obj.recognize), 'function');
    });

    it('new module.FaceRecognition() object has a method .querySimilarityScoreByID', function () {
      assert.equal(typeof(obj.querySimilarityScoreByID), 'function');
    });

  });

});
