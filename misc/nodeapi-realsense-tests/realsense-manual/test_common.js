var instanceConfig = { 
//    skeleton: {
//        enable: true,
//        maxTrackedPerson: 2,
//        trackArea: 'AREA_UPPER_BODY'
//    },

    tracking: {
        enable: true
        //enableHeadPose: true,
        //enablePersonOrientation: true,
        //enableHeadBoundingBox: true,
        //enableFaceLandmarks: true
    }  
    //expression: {
    //    enable: true,
    //    enableAllExpressions: true
    //},  
    //gesture: {
    //    enable: true,
    //    enableAllGestures: true
    //},  
    //recognition: {
    //    enable: true,
    //    policy: "standard",
    //    useMultiFrame: false
    //}   
};
var emitter = require('events').EventEmitter;
var common = require('./common.js');
var module = require('bindings')('pt');
var m = common.getObj(module, 'Instance', instanceConfig);
function inherits(target, source) {
  for (var k in source.prototype) {
    target.prototype[k] = source.prototype[k];
  }
}
inherits(module.Instance, emitter);
//var m = new module.Instance(instanceConfig)
m.on('persontracked', function(result) {
  result.persons.forEach(function(person) {
    console.log('persion');
  });
});
m.start().then(function(){console.log('start');});
