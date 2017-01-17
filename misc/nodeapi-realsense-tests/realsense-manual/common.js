var emitter = require('events').EventEmitter;
function inherits(target, source) {
  for (var k in source.prototype) {
    target.prototype[k] = source.prototype[k];
  }
}
function getInstance(module, instanceConfig, cameraConfig) {
  var module = module;
  inherits(module.Instance, emitter);
  if (cameraConfig) {
    return new module.Instance(instanceConfig, cameraConfig);
  } else {
    return new module.Instance(instanceConfig);
  }
}
var getObj = function getObj(module, name, instanceConfig, cameraConfig) {
  var m = getInstance(module, instanceConfig, cameraConfig);
  if (name == 'Instance') {
    return m;
  }
  if (name == 'PersonTracking') {
    return m.personTracking
  }
  else if (name == 'SkelonArea') {
    m.getInstanceConfig.then(
      data => {
        return data.skeleton.traingArea;
      }
    );
  }
}
exports.getObj = getObj;
