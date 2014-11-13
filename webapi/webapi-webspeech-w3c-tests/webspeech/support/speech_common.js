/**
 * Method to check Constructors
 * Example usage:
 * check_constructor("BluetoothAdapter")
 *
 * @param obj object name
 * @param constructorName constructor name
 */
var TYPE_ERROR_EXCEPTION = {name: 'TypeError'};
function check_constructor(obj,constructorName) {
    assert_true(constructorName in obj, "No " + constructorName + " in window.");
    assert_false({} instanceof obj[constructorName],"Custom object is not instance of " + constructorName);
    assert_throws({
        name: "TypeError"
    }, function () {
        obj[constructorName]();
    }, "Constructor called as function.");
}

/**
 * Method to check NoInterfaceObject
 * Example usage:
 * check_no_interface_object(window, "SpeechSynthesisGetter")
 * 
 * @param obj object of interface
 * @param interfaceName interface name
 */
function check_no_interface_object(obj, interfaceName) {
    assert_throws({name: "TypeError"}, function () {
        obj[interfaceName]();
    },"Wrong call as a function");
    assert_throws({name: "TypeError"}, function () {
        new obj[interfaceName]();
    },"Wrong call as a new function");
    assert_throws({name: "TypeError"}, function () {
        ({}) instanceof obj[interfaceName];
    },"instanceof exception");
    assert_equals(obj[interfaceName], undefined, interfaceName + " is not undefined.");
}

function getDOMStringConversionArray(isOptional){
    var typeArr = [true, false, NaN, 0, undefined, [1,2], {"a":1,"b":2}, function(){} ];
    if (!isOptional) {
        typeArr.push(null);
    }
    return typeArr;
}
