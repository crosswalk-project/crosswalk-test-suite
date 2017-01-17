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
var instance = util.getObj(module, "PersonTracking", instanceConfig, cameraConfig).instance;
var obj = util.getObj(module, "PersonTracking", instanceConfig, cameraConfig).obj;
describe('PersonTracking API Test', function () {

  describe('API Existance', function() {
    it('module.PersonTracking is exist', function() {
      assert.ok(typeof(obj) !== 'undefined' )
    });

    it('module.PersonTracking type is correct', function() {
      assert.equal(typeof(obj),'object');
    });

    it('new module.PersonTracking() object has a method .startTrackingPerson', function () {
      assert.equal(typeof(obj.startTrackingPerson), 'function');
    });

    it('new module.PersonTracking() object has a method .stopTrackingPerson', function () {
      assert.equal(typeof(obj.stopTrackingPerson), 'function');
    });

  });

});
