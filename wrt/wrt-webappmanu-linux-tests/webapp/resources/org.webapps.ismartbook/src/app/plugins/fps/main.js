/*jshint indent:2 */

/*global define:true, window:false, $:false, jQuery:false */
define(function(require, exports, module) {
  "use strict";
  // var FPSMeter = require("fpsmeter");
  // var collector = require("pkg!collector");
  var fps = 0;
  var count = 0;
  $(document).on("fps",function(evt){

    count++;
    fps += evt.originalEvent.fps;
  });
  $(document).on("fpsend",function(evt){
    var averageFPS = parseFloat(fps/count);
    // collector.sentData({averageFPS: averageFPS});
    console.log("averageFPS",averageFPS);
    count = 0;
    fps = 0;
  });

  module.exports = FPSMeter;
});