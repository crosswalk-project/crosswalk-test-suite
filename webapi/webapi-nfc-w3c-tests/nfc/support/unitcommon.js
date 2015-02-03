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
NOT_FOUND_EXCEPTION = {name: 'NotFoundError'};
INVALID_VALUES_EXCEPTION = {name: 'InvalidValuesError'};
IO_EXCEPTION = {name: 'IOError'};
SECURITY_EXCEPTION = {name: 'SecurityError'};


(function () {
    var head_src = document.head.innerHTML;
    if (head_src.indexOf('testharness.js') === -1) {
        document.write("<script src=\"..\/resources\/testharness.js\"><\/script>");
    }

    if (head_src.indexOf('testharnessreport.js') === -1) {
        document.write("<script src=\"..\/resources\/testharnessreport.js\"><\/script>");
    }
})();

var _registered_types = {};

function _resolve_registered_type(type) {
    while (type in _registered_types) {
        type = _registered_types[type];
    }
    return type;
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

/**
 * Method to check if attribute is const.
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
 * Method to check if given method can be overridden in a given object - (TEMPORARY REMOVED).
 * That method also checks if given method exists in a given object.
 * Example usage:
 * check_method_exists(Navigator.nfc, "powerOn");
 *
 * @param obj object with method
 * @param methodName name of the method to check.
 */
function check_method_exists(obj, methodName) {
    assert_type(obj[methodName], 'function', "Method does not exist.");
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

