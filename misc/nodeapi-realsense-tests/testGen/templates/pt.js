// Copyright (c) 2016 Intel Corporation. All rights reserved.
//  // Use of this source code is governed by a MIT-style license that can be
//   // found in the LICENSE file.
//const webIDL2 = require('webidl2');
var assert = require('assert');

//var idlTree = _readFile(file).then(data => {_parseIDL(data.toString())});
//var enum_group = 

var PT = require('pt');
var enum_group = ['frontal', 'profile', 'all',]; //from widl parser
enum_group.push('invild');
describe('enum name', function(){
  for (var i in enum_group) {
    it ('# enum group'+ enum_group[i], function(done){
      var CFG = {trackingAngle: enum_group[i]}; //
      var Instance = new PT.Instance(CFG);
      Instance.getInstanceConfig().then(data =>{
        assert.equal(data.trackingAngle, enum_group[i])};
        done());
    }
  })
})
