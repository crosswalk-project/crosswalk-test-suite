(function() {

var TextExtend = function(picType,lastPoint,nextPoint) {
  this.initialize(picType,lastPoint,nextPoint);
}
var p = TextExtend.prototype = new createjs.Text(); // inherit from Text

p.picType = null;//"pen","line","rectangle","ellipse","eraser","text";
p.lastPoint = {x:null,y:null};
p.nextPoint = {x:null,y:null};

p.fontWeight = null;
p.fontSize = null;
p.fontFamily = null;

p.Text_initialize = p.initialize;
p.initialize = function(picType,lastPoint,nextPoint) {
	this.Text_initialize();
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
window.TextExtend = TextExtend;
}());