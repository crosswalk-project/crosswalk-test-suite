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
var instance = util.getObj(module, "RecognitionInfo", instanceConfig, cameraConfig).instance;
var obj = util.getObj(module, "RecognitionInfo", instanceConfig, cameraConfig).obj;
describe('RecognitionInfo API Test', function () {

  describe('API Existance', function() {
    it('module.RecognitionInfo is exist', function() {
      assert.ok(typeof(obj) !== 'undefined' )
    });

    it('module.RecognitionInfo type is correct', function() {
      assert.equal(typeof(obj),'object');
    });

    it('module.RecognitionInfo() object has the attribute trackID', function () {
      assert.ok(obj.trackID !== undefined );
    });
    it('module.RecognitionInfo() object has the number attribute trackID', function () {
      assert.equal(typeof(obj.trackID),'number');
    });

    it('module.RecognitionInfo() object has the writable attribute trackID', function () {
      var tmp;
      tmp = obj.trackID;
      obj.trackID = NaN;
      assert.notEqual(tmp, obj.trackID);
    });

    it('module.RecognitionInfo() object has the attribute recognitionID', function () {
      assert.ok(obj.recognitionID !== undefined );
    });
    it('module.RecognitionInfo() object has the number attribute recognitionID', function () {
      assert.equal(typeof(obj.recognitionID),'number');
    });

    it('module.RecognitionInfo() object has the writable attribute recognitionID', function () {
      var tmp;
      tmp = obj.recognitionID;
      obj.recognitionID = NaN;
      assert.notEqual(tmp, obj.recognitionID);
    });

    it('module.RecognitionInfo() object has the attribute similarityScore', function () {
      assert.ok(obj.similarityScore !== undefined );
    });
    it('module.RecognitionInfo() object has the number attribute similarityScore', function () {
      assert.equal(typeof(obj.similarityScore),'number');
    });

    it('module.RecognitionInfo() object has the writable attribute similarityScore', function () {
      var tmp;
      tmp = obj.similarityScore;
      obj.similarityScore = NaN;
      assert.notEqual(tmp, obj.similarityScore);
    });

  });

});
