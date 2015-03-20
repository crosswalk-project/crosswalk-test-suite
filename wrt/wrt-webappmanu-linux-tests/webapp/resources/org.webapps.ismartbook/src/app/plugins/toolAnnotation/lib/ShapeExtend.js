(function() {

var ShapeExtend = function(picType,lastPoint,nextPoint) {
  this.initialize(picType,lastPoint, nextPoint);
}
var p = ShapeExtend.prototype = new createjs.Shape(); // inherit from Shape

p.picType = null;//"pen","line","rectangle","ellipse","eraser";
p.lastPoint = {x:null,y:null};
p.nextPoint = {x:null,y:null};
p.Shape_initialize = p.initialize;
p.initialize = function(picType,lastPoint,nextPoint) {
	this.Shape_initialize();
	if(picType){
		this.picType = picType;
	}
	if(lastPoint){
		this.lastPoint = lastPoint;
	}
	if(nextPoint){
		this.nextPoint = nextPoint;
	}
}
window.ShapeExtend = ShapeExtend;
}());