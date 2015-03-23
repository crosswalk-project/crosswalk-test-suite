define(function(require, exports, module) {
	var collector = {};
	collector.defaults = {
		url: "http://192.168.1.113:3000/benchmark",
	};
	collector.sentData = function(data) {
		if(typeof data != "object") {
			data = {data: data};
		}
		$.post(collector.defaults.url, data, function(result) {
			console.log(result);
		}, "jsonp");
	};
	return collector;
});