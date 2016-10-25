var emitter = require('events').EventEmitter;
function inherits(target, source) {
  for (var k in source.prototype) {
    target.prototype[k] = source.prototype[k];
  }
}
function getInstance(module, instanceConfig, cameraConfig) {
  var module = module;
  inherits(module.Instance, emitter);
  if (cameraConfig != {}) {
    //return new module.Instance(instanceConfig, cameraConfig);
    return new module.Instance(instanceConfig);
  } else {
    return new module.Instance(instanceConfig);
  }
}
var getObj = function getObj(module, name, instanceConfig, cameraConfig) {
  var m = getInstance(module, instanceConfig, cameraConfig);
  m.start().then(function(){console.log('Start camera!');});
  if (name == 'Instance') {
    return {
      instance: m,
      obj: m
    }
  }
  else if (name == 'PersonTracking') {
    return {
      instance: m,
      obj: m.personTracking
    }
  }
  else if (name == 'SkelonArea') {
    m.getInstanceConfig.then(
      data => {
        return {
          instance: m,
          obj: data.skeleton.traingArea
        }
      }
    );
  }
  else if (name == 'LyingPoseInfo') {
    m.lyingPoseRecognition.getCandidatesData().then(
      data => {
        return {
          instance: m,
          obj: data[0]
        }
      }
    )
  }
  else if (name == 'LyingPoseRecognition') {
    return {
      instance: m,
      obj: m.lyingPoseRecognition
    }
  }
  else if (name == 'RecognitionInfo') {
    m.faceRecognition.recognizeAll().then(
      data => {
        return {
          instance: m,
          obj: data[0]
        }
      }
    )
  }
  else if (name == 'FaceRecognition') {
    return {
      instance: m,
      obj: m.faceRecognition
    }
  }
  else if (name == 'PersonTracking') {
    return {
      instance: m,
      obj: m.personTracking
    }
  }
}
exports.getObj = getObj;
