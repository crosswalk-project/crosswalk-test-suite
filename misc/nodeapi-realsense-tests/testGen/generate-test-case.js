// Copyright (c) 2016 Intel Corporation. All rights reserved.
// Use of this source code is governed by a MIT-style license that can be
// found in the LICENSE file.

"use strict";

const path = require('path');
const fs = require("fs.promised");
const mkdirp = require("mkdirp");
const glob = require('glob');

const webIDL2 = require("webidl2");
const dot = require("dot");
dot.templateSettings.strip = false; // Do not remove spaces & linebreaks
const dots = dot.process({path: path.join(__dirname, "templates")});

const _writeFile = function(name, text) {
  return fs.writeFile(name, text);
};

const _packEmptyLines = function(str) {
  return str.replace(/\n{3,}/gm, '\n\n').replace(/(\r\n){3,}/gm, '\r\n\r\n');
};

const _parseIDL = function(idlText) {
  return webIDL2.parse(idlText);
};

const _readFile = function (path) {
  return fs.readFile(path);
};

function generateTestCase() {
  var array = glob.sync(path.join('idl','*'));
  array.forEach(file =>{
    var ext = path.parse(file).ext;
    if (ext === '.widl') {
      _readFile(file)
        .then(data => {
          var idlTree = _parseIDL(data.toString());
          idlTree.forEach(def => {
            def.file_name = path.parse(file).name;
            console.log("----start-----");
            console.log(def);
            console.log("----end-----");
            if (def.type === 'interface') {
              console.log('interface is ' + def.name);
              const testText = _packEmptyLines(dots.apiExistence(def));
              const dirName = "realsense";
              mkdirp.sync(dirName);
              const fileName = path.join('..', dirName, 'test-' + def.name.toLowerCase() + '-api-existence.js');
              console.log(fileName);
              _writeFile(fileName, testText);
            }
            //else if (def.type === 'enum') {
            //  const testText = _packEmptyLines(dots.enumExistence(def));
            //  const dirName = "realsense";
            //  mkdirp.sync(dirName);
            //  const fileName = path.join('..', dirName, 'test-' + def.name.toLowerCase() + '-enum-existence.js');
            //  console.log(fileName);
            //  _writeFile(fileName, testText);
            //}
          });
        })
        .catch(e => {
          console.log(e);
        });
    }
    var name = path.parse(file).name;
    if (ext === '.json') {
      _readFile(file)
        .then(data => {
          var obj = JSON.parse(data);
          var rlt = {}
          var index = 1;
          for (var i in obj) {
            for (var j in obj[i]){
              rlt[index] = {};
              rlt[index]['index'] = index;
              rlt[index]['name'] = i;
              rlt[index]['type'] = typeof(obj[i][j]);
              rlt[index]['value'] = obj[i][j];
              index++;
            }
          }
          //for (var i in obj['enable']) {
          //  for (var j in obj['maxTrackedPerson']) {
          //    for (var k in obj['trackingArea']) {
          //      rlt[index] = {};
          //      rlt[index]['index'] = index;
          //      rlt[index]['values'] = {};
          //      rlt[index]['values']['enable'] = obj['enable'][i] 
          //      rlt[index]['values']['maxTrackedPerson'] = obj['maxTrackedPerson'][j] 
          //      rlt[index]['values']['trackingArea'] = obj['trackingArea'][k] 
          //      index++;
          //    }
          //  }
          //}
          for (var i in rlt ) {
            var def = rlt[i];
            var index = def['index'];
            const testText = _packEmptyLines(dots[name](def));
            const dirName = "realsense";
            mkdirp(path.join('..', dirName, name));
            //const fileName = path.join('..', dirName, name, 'test-' + name + '-positive' + index + '.js');
            const fileName = path.join('..', dirName, name, 'test-' + name + '-' + rlt[i]['name'] +'-'+ rlt[i]['value'] + '-positive.js');
            console.log(fileName);
            _writeFile(fileName, testText);
         };
      });
    };
  })
}

generateTestCase();

module.exports = {
  generateTestCase: generateTestCase
};
