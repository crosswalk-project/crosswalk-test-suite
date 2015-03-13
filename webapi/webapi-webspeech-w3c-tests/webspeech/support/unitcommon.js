/*

Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Authors:

 */


MIN_BYTE = -128;
MAX_BYTE = 127;
MIN_OCTET = 0;
MAX_OCTET = 255;
MIN_SHORT = -32768;
MAX_SHORT = 32767;
MIN_UNSIGNED_SHORT = 0;
MAX_UNSIGNED_SHORT = 65535;
MIN_LONG = -2147483648;
MAX_LONG = 2147483647;
MIN_UNSIGNED_LONG = 0;
MAX_UNSIGNED_LONG = 4294967295;
MIN_LONG_LONG = -9223372036854775808;
MAX_LONG_LONG = 9223372036854775807;
MIN_UNSIGNED_LONG_LONG = 0;
MAX_UNSIGNED_LONG_LONG = 18446744073709551615;

TYPE_MISMATCH_EXCEPTION = {name: 'TypeMismatchError'};
TYPE_ERROR_EXCEPTION = {name: 'TypeError'};
NOT_FOUND_EXCEPTION = {name: 'NotFoundError'};
INVALID_VALUES_EXCEPTION = {name: 'InvalidValuesError'};
IO_EXCEPTION = {name: 'IOError'};
SECURITY_EXCEPTION = {name: 'SecurityError'};


(function () {
   var head_src = document.head.innerHTML;
   if (head_src.search(/\/testharness.js\W/) === -1) {
       document.write('<script language="javascript" src="../resources/testharness.js"></script>\n');
   }
   if (head_src.search(/\/testharnessreport.js\W/) === -1) {
       document.write('<script language="javascript" src="../resources/testharnessreport.js"></script>\n');
   }
})();

var _registered_types = {};

function _resolve_registered_type(type) {
    while (type in _registered_types) {
        type = _registered_types[type];
    }
    return type;
}

/**
 * Method checks extra argument for none argument method.
 * The only check is that method will not throw an exception.
 * Example usage:
 * checkExtraArgument(tizen.notification, "removeAll");
 *
 * @param object object
 * @param methodName string - name of the method
 */
function checkExtraArgument(object, methodName) {
    var extraArgument = [
        null,
        undefined,
        "Tizen",
        1,
        false,
        ["one", "two"],
        {argument: 1},
        function () {}
    ], i;

    for (i = 0; i < extraArgument.length; i++) {
        object[methodName](extraArgument[i]);
    }
}

/**
 * Method to validate conversion.
 * Example usage:
 *   conversionTable = getTypeConversionExceptions("functionObject", true);
 *   for(i = 0; i < conversionTable.length; i++) {
 *       errorCallback = conversionTable[i][0];
 *       exceptionName = conversionTable[i][1];
 *
 *       assert_throws({name : exceptionName},
 *       function () {
 *           tizen.systemsetting.setProperty("HOME_SCREEN",
 *               propertyValue, successCallback, errorCallback);
 *       }, exceptionName + " should be thrown - given incorrect errorCallback.");
 *   }
 *
 * @param conversionType
 * @param isOptional
 * @returns table of tables which contain value (index 0) and exceptionName (index 1)
 *
 */
function getTypeConversionExceptions(conversionType, isOptional) {
    var exceptionName = "TypeMismatchError",
        conversionTable;
    switch (conversionType) {
        case "enum":
            conversionTable = [
                [0, exceptionName],
                [true, exceptionName],
                ["dummyInvalidEnumValue", exceptionName],
                [{ }, exceptionName]
            ];
            if (!isOptional) {
                conversionTable.push([null, exceptionName]);
                conversionTable.push([undefined, exceptionName]);
            }
            break;
        case "double":
            conversionTable = [
                [NaN, exceptionName],
                [Number.POSITIVE_INFINITY, exceptionName],
                [Number.NEGATIVE_INFINITY, exceptionName],
                ["TIZEN", exceptionName],
                [{ name : "TIZEN" }, exceptionName],
                [function () { }, exceptionName]
            ];
            if (!isOptional) {
                conversionTable.push([undefined, exceptionName]);
            }
            break;
        case "object":
            conversionTable = [
                [true, exceptionName],
                [false, exceptionName],
                [NaN, exceptionName],
                [0, exceptionName],
                ["", exceptionName],
                ["TIZEN", exceptionName]
            ];
            if (!isOptional) {
                conversionTable.push([null, exceptionName]);
                conversionTable.push([undefined, exceptionName]);
            }
            break;
        case "functionObject":
            conversionTable = [
                [true, exceptionName],
                [false, exceptionName],
                [NaN, exceptionName],
                [0, exceptionName],
                ["", exceptionName],
                ["TIZEN", exceptionName],
                [[], exceptionName],
                [{ }, exceptionName]
            ];
            if (!isOptional) {
                conversionTable.push([null, exceptionName]);
                conversionTable.push([undefined, exceptionName]);
            }
            break;
        case "array":
            conversionTable = [
                [true, exceptionName],
                [false, exceptionName],
                [NaN, exceptionName],
                [0, exceptionName],
                ["", exceptionName],
                ["TIZEN", exceptionName],
                [{ }, exceptionName],
                [function () { }, exceptionName]
            ];
            if (!isOptional) {
                conversionTable.push([null, exceptionName]);
                conversionTable.push([undefined, exceptionName]);
            }
            break;
        case "dictionary":
            conversionTable = [
                [true, exceptionName],
                [false, exceptionName],
                [NaN, exceptionName],
                [0, exceptionName],
                ["", exceptionName],
                ["TIZEN", exceptionName]
            ];
            if (!isOptional) {
                conversionTable.push([null, exceptionName]);
                conversionTable.push([undefined, exceptionName]);
            }
            break;
        default:
            assert_unreached("Fix your test. Wrong conversionType '" + conversionType + "'.");
    };

    return conversionTable;
}

function assert_type(obj, type, description) {
    var org_type = type, prop_name, prop_type, prop_value;

    type = _resolve_registered_type(type);

    if (typeof (type) === 'string') {
        type = type.toLowerCase();
        switch (type) {
            case 'object':
            case 'string':
            case 'number':
            case 'function':
            case 'boolean':
            case 'undefined':
            case 'xml':
                assert_equals(typeof (obj), type, description);
                break;
            case 'null':
                assert_true(obj === null, description);
                break;
            case 'array':
                assert_true(Array.isArray(obj), description);
                break;
            case 'date':
                assert_true(obj instanceof Date, description);
                break;
            case 'byte':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_BYTE, description + " - value too low.");
                assert_less_than_equal(obj, MAX_BYTE, description + " - value too high.");
                assert_equals(Math.abs(obj % 1), 0, description + " - value is not an integer.");
                break;
            case 'octet':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_OCTET, description + " - value too low.");
                assert_less_than_equal(obj, MAX_OCTET, description + " - value too high.");
                assert_equals(obj % 1, 0, description + " - value is not an integer.");
                break;
            case 'short':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_SHORT, description + " - value too low.");
                assert_less_than_equal(obj, MAX_SHORT, description + " - value too high.");
                assert_equals(Math.abs(obj % 1), 0, description + " - value is not an integer.");
                break;
            case 'unsigned short':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_UNSIGNED_SHORT, description + " - value too low.");
                assert_less_than_equal(obj, MAX_UNSIGNED_SHORT, description + " - value too high.");
                assert_equals(obj % 1, 0, description + " - value is not an integer.");
                break;
            case 'long':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_LONG, description + " - value too low.");
                assert_less_than_equal(obj, MAX_LONG, description + " - value too high.");
                assert_equals(Math.abs(obj % 1), 0, description + " - value is not an integer.");
                break;
            case 'unsigned long':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_UNSIGNED_LONG, description + " - value too low.");
                assert_less_than_equal(obj, MAX_UNSIGNED_LONG, description + " - value too high.");
                assert_equals(obj % 1, 0, description + " - value is not an integer.");
                break;
            case 'long long':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_LONG_LONG, description + " - value too low.");
                assert_less_than_equal(obj, MAX_LONG_LONG, description + " - value too high.");
                assert_equals(Math.abs(obj % 1), 0, description + " - value is not an integer.");
                break;
            case 'unsigned long long':
                assert_equals(typeof (obj), 'number', description);
                assert_greater_than_equal(obj, MIN_UNSIGNED_LONG_LONG, description + " - value too low.");
                assert_less_than_equal(obj, MAX_UNSIGNED_LONG_LONG, description + " - value too high.");
                assert_equals(obj % 1, 0, description + " - value is not an integer.");
                break;
            case 'double':
                assert_equals(typeof (obj), 'number', description);
                break;
            default:
                assert_unreached('Fix your test. Wrong type \'' + org_type + '\'');
        }
    } else if (typeof (type) === 'function') {
        assert_true(obj instanceof type, description);
    } else if (typeof (type) === 'object') {
        for (prop_name in type) {
            prop_type = type[prop_name];
            if (prop_type === 'function') {
                assert_inherits(obj, prop_name);
                assert_equals(typeof obj[prop_name], prop_type, 'Object should have method ' + prop_name);
            } else {
                assert_own_property(obj, prop_name);
            }
        }
    } else {
        assert_unreached('Fix your test. Wrong type ' + org_type);
    }
}

function register_type(alias, type_spec) {
    _registered_types[alias] = type_spec;
}

/**
 * Method to check if attribute is const.
 * Example usage:
 * check_const(tizen.bluetooth.deviceMinor, 'TOY_DOLL', 0x03, 'number', 0x29B);
 *
 * @param obj  object to test which  has const attribute
 * @param attributeName attribute name.
 * @param expectedValue expected value of provided attribute name
 * @param expectedType expected type of provided attribute name
 * @param valueToAssign value to assign in order to check if attribute value can be modified
 */
function check_const(obj, attributeName, expectedValue, expectedType, valueToAssign) {
    var tmp;
    if (expectedValue === valueToAssign) {
        assert_unreached("Fix your test. The same values given for "  + attributeName +
            " in 'value' and 'valueToSet' arguments.");
    }
    if (typeof (attributeName) === "string") {
        assert_true(attributeName in obj, "Name " + attributeName + " doesn't exist in provided object.");
        assert_equals(obj[attributeName], expectedValue, "Value of " + attributeName + " is diffrent.");
        if (typeof (expectedType) !== "undefined") {
            if (expectedValue === null) {
                assert_type(obj[attributeName], "object", "Type of " + attributeName + " is different.");
            } else {
                assert_type(obj[attributeName], expectedType, "Type of " + attributeName + " is different.");
            }
        } else {
            assert_unreached("Fix your test. Wrong type " + expectedType);
        }
        tmp = obj[attributeName];
        obj[attributeName] = valueToAssign;
        assert_equals(obj[attributeName], tmp, attributeName + " can be modified.");
    } else {
        assert_unreached("Fix your test. Wrong type of name " + typeof (attributeName));
    }
}

/**
 * Method to check if attribute is readonly.
 * Example usage:
 * check_readonly(statusNotification, "postedTime", null, 'object', new Date());
 *
 * @param obj  object to test which  has readonly attribute
 * @param attributeName attribute name.
 * @param expectedValue expected value of provided attribute name
 * @param expectedType expected type of provided attribute name
 * @param valueToAssign value to assign in order to check if attribute value can be modified
 */
function check_readonly(obj, attributeName, expectedValue, expectedType, valueToAssign) {
    check_const(obj, attributeName, expectedValue, expectedType, valueToAssign);
}

/**
 * Method to check if attribute can be set to null.
 * Example usage:
 * check_not_nullable(syncInfo, "mode");
 *
 * @param obj object to test which has not nullable attribute
 * @param attributeName attribute name.
 */
function check_not_nullable(obj, attributeName)
{   var old_value = obj[attributeName];
    obj[attributeName] = null;
    assert_not_equals(obj[attributeName], null, "Attribute " + attributeName + " can be set to null.");
    obj[attributeName] = old_value;
}

/**
 * Method to check NoInterfaceObject
 * Example usage:
 * check_no_interface_object("BluetoothAdapter")
 *
 * @param interfaceName interface name
 */
/*
function check_no_interface_object(interfaceName) {
    assert_throws({name: "TypeError"}, function () {
        tizen[interfaceName]();
    },"Wrong call as a function");
    assert_throws({name: "TypeError"}, function () {
        new tizen[interfaceName]();
    },"Wrong call as a new function");
    assert_throws({name: "TypeError"}, function () {
        ({}) instanceof tizen[interfaceName];
    },"instanceof exception");
    assert_equals(tizen[interfaceName], undefined, interfaceName + " is not undefined.");
}
*/

/**
 * Method to check Constructors
 * Example usage:
 * check_constructor("BluetoothAdapter")
 *
 * @param constructorName constructor name
 */
function check_constructor(obj, constructorName) {
    assert_true(constructorName in obj, "No " + constructorName + " in " + obj);
    assert_false({} instanceof obj[constructorName],"Custom object is not instance of " + constructorName);
    assert_throws({
        name: "TypeError"
    }, function () {
        obj[constructorName]();
    }, "Constructor called as function.");
}


/**
 * Method to check if given method can be overridden in a given object - (TEMPORARY REMOVED).
 * That method also checks if given method exists in a given object.
 * Example usage:
 * check_method_exists(tizen.notification, "get");
 *
 * @param obj object with method
 * @param methodName name of the method to check.
 */
function check_method_exists(obj, methodName) {
    assert_type(obj[methodName], 'function', "Method does not exist.");
}

/**
 * Method to check extensibility of given object.
 * Method checks if new attribute and method can be added.
 * Example usage:
 * check_extensibility(tizen.notification);
 *
 * @param obj object to check
 */
function check_extensibility(obj) {
    var dummyAttribute = "dummyAttributeValue", dummyMethodResult = "dummyMethodResultValue";
    obj.newDummyMethod = function() {
        return dummyMethodResult;
    }
    assert_equals(obj.newDummyMethod(), dummyMethodResult, "Incorrect result from added method.");

    obj.newDummyAttribute = dummyAttribute;
    assert_equals(obj.newDummyAttribute, dummyAttribute, "Incorrect result from added attribute.");
}

/**
 * Method to check if attribute can be modify.
 * Example usage:
 * check_attr(downloadRequest, "fileName", default_val, "string", "file_name.html");
 *
 * @param obj  object to test which has not readonly attribute
 * @param attributeName attribute name.
 * @param expectedValue expected value of provided attribute name
 * @param expectedType expected type of provided attribute name
 * @param valueToAssign value to assign in order to check if attribute value can be modified
 */
function check_attribute(obj, attributeName, expectedValue, expectedType, valueToAssign) {
    if (expectedValue === valueToAssign) {
        assert_unreached("Fix your test. The same values given for "  + attributeName +
            " in 'value' and 'valueToSet' arguments.");
    }
    if (typeof (attributeName) === "string") {
        assert_true(attributeName in obj, "Name " + attributeName + " doesn't exist in provided object.");
        assert_equals(obj[attributeName], expectedValue, "Value of " + attributeName + " is diffrent.");
        if (typeof (expectedType) !== "undefined") {
            if (expectedValue === null) {
                assert_type(obj[attributeName], "object", "Type of " + attributeName + " is different.");
            } else {
                assert_type(obj[attributeName], expectedType, "Type of " + attributeName + " is different.");
            }
        } else {
            assert_unreached("Fix your test. Wrong type " + expectedType);
        }
        obj[attributeName] = valueToAssign;
        assert_equals(obj[attributeName], valueToAssign, attributeName + " can be modified.");
    } else {
        assert_unreached("Fix your test. Wrong type of name " + typeof (attributeName));
    }
}

/**
 * Method to check if whole array can be overwritten with an invalid value.
 * Sample usage:
 * check_invalid_array_assignments(message, "to", false);
 *
 * @param obj object which has the array as its property
 * @param array name of the array to check
 * @param isNullable indicates if the array can be null
 */
function check_invalid_array_assignments(obj, array, isNullable) {
    var args = [undefined, true, false, NaN, 0, "TIZEN", {}, function () {}],
        val = obj[array], i;

    if (!isNullable) {
        obj[array] = null;
        assert_not_equals(obj[array], null, "Non-nullable array was set to null");
        assert_type(obj[array], "array", "Non-nullable array type changed after assigning null");
        assert_equals(obj[array].toString(), val.toString(), "Non-nullable array contents changed after assigning null");
    }

    for (i = 0 ; i < args.length ; i++) {
        obj[array] = args[i];
        assert_type(obj[array], "array", "Array type changed after assigning an invalid value");
        assert_equals(obj[array].toString(), val.toString(), "Array contents changed after assigning an invalid value");
    }
}

/**
 * Method to check if an object can be overwritten with an invalid value.
 * Sample usage:
 * check_invalid_object_assignments(message, "body", false);
 *
 * @param parentObj object which has the 'obj' object as its property
 * @param obj name of the object to check
 * @param isNullable indicates if the object can be null
 */
function check_invalid_obj_assignments(parentObj, obj, isNullable) {
    var args = [undefined, true, false, NaN, 0, "TIZEN", function () {}],
        val = parentObj[obj], i;

    if (!isNullable) {
        parentObj[obj] = null;
        assert_equals(parentObj[obj], val, "Non-nullable obj was modified after assigning null");
    }

    for (i = 0 ; i < args.length ; i++) {
        parentObj[obj] = args[i];
        assert_equals(parentObj[obj], val, "The object was set to " + args[i]);
    }
}

/**
 * Method to validate conversion for listeners.
 * Example usage:
 * incorrectListeners = getListenerConversionExceptions(["oninstalled", "onupdated", "onuninstalled"]);
 * for(i = 0; i < incorrectListeners.length; i++) {
 *     packageInformationEventCallback  = incorrectListeners[i][0];
 *     exceptionName = incorrectListeners[i][1];
 *     assert_throws({name : exceptionName},
 *        function () {
 *             tizen.package.setPackageInfoEventListener(packageInformationEventCallback);
 *         }, exceptionName + " should be thrown - given incorrect successCallback.");
 * }
 *
 *
 * @param callbackNames Array with names
 * @returns {Array} table of tables which contain incorrect listener (index 0) and exceptionName (index 1)
 *
 */
function getListenerConversionExceptions(callbackNames) {
    var result = [], conversionTable, i, j, listenerName;
    conversionTable = getTypeConversionExceptions("functionObject", false);

    for (i = 0; i < callbackNames.length; i++) {
        for (j = 0; j < conversionTable.length; j++) {
            listenerName = {};
            listenerName[callbackNames[i]] = conversionTable[j][0];
            result.push([listenerName, conversionTable[j][1]]);
        }
    }

    return result;
}



/**
 * Method to validate type checking of method argument.
 * Example usage:
 *   checkTypeMismatch("enum", true, function(argumentToCheck) {
 *      tizen.tv.channel.tune(CHANNEL_MAJOR, CHANNEL_MINOR, successCallback, errorCallback, {}, argumentToCheck);
 *  });
 *
 *
 * @param conversionType
 * @param isOptional
 * @param functionToCheck
 */
function checkTypeMismatch(conversionType, isOptional, functionToCheck) {
    var conversionTable, argumentToCheck, exceptionName, i;

    conversionTable = getTypeConversionExceptions(conversionType, isOptional);
    for(i = 0; i < conversionTable.length; i++) {
        argumentToCheck = conversionTable[i][0];
        exceptionName = conversionTable[i][1];

        assert_throws({name: exceptionName},
            function () {
                functionToCheck(argumentToCheck);
            },
            "Given argument of incorrect type: " + format_value(argumentToCheck)
        );
   }
}
