"use strict"

const assert = require('assert');
var module = require('./pt.js');
var enum_group = [];

enum_group.push("frontal")

enum_group.push("profile")

enum_group.push("all")

enum_group.push('invalid');

function _test(i) {
  describe('check enum TrackingAngle', function(){
      it('checking member of TrackingAngle: '+ enum_group[i], function(done) {
        var cfg = {}
        
        cfg['trackingAngle'] = enum_group[i];
        
        var instance = new module.Instance(cfg);
        console.log(123);
        instance.getInstanceConfig().then(data => {
          console.log(data);
          assert.equal(data.trackingAngle, enum_group[i]);
          done();
        });
      });
  });
}

for (var x in enum_group) {
  _test(x);
}
