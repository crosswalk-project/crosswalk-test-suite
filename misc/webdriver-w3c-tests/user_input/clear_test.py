# -*- mode: python; fill-column: 100; comment-column: 100; -*-

import os
import sys
import unittest

from selenium.common.exceptions import InvalidElementStateException

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir)))
import base_test


class ElementClearTest(base_test.WebDriverBaseTest):

    def test_writable_text_input_element_should_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_writable_input_page.html"))
        e = self.driver.find_element_by_id("writableTextInput")
        e.clear()
        self.assertEquals("", e.get_attribute("value"))

    def test_disabled_text_input_element_should_not_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_disabled_input_page.html"))
        e = self.driver.find_element_by_id("disabledTextInput")
        self.assertRaises(InvalidElementStateException, lambda: e.clear())

    def test_read_only_text_input_element_should_not_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_readonly_input_page.html"))
        e = self.driver.find_element_by_id("readOnlyTextInput")
        self.assertRaises(InvalidElementStateException, lambda: e.clear())

    def test_writable_text_area_element_should_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_writable_textarea_page.html"))
        e = self.driver.find_element_by_id("writableTextArea")
        e.clear()
        self.assertEquals("", e.get_attribute("value"))

    def test_disabled_text_area_element_should_not_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_disabled_textarea_page.html"))
        e = self.driver.find_element_by_id("disabledTextArea")
        self.assertRaises(InvalidElementStateException, lambda: e.clear())

    def test_read_only_text_input_element_should_not_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_readonly_textarea_page.html"))
        e = self.driver.find_element_by_id("readOnlyTextArea")
        self.assertRaises(InvalidElementStateException, lambda: e.clear())

    def test_content_editable_area_should_clear(self):
        self.driver.get(self.webserver.where_is(
            "user_input/res/element_clear_contenteditable_page.html"))
        e = self.driver.find_element_by_id("contentEditableElement")
        e.clear()
        self.assertEquals("", e.text)

if __name__ == "__main__":
    unittest.main()
