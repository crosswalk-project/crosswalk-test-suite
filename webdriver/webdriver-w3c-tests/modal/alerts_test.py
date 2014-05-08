# -*- mode: python; fill-column: 100; comment-column: 100; -*-

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import base_test

from client.exceptions import ElementNotVisibleException, NoSuchAlertException
from client.wait import WebDriverWait

class AlertsTest(base_test.WebDriverBaseTest):

    def setUp(self):
        self.wait = WebDriverWait(self.driver, 5, ignored_exceptions = [NoSuchAlertException])
        self.driver.get(self.webserver.where_is('modal/res/alerts.html'))

    def tearDown(self):
        try:
            self.driver.switch_to_alert().dismiss()
        except NoSuchAlertException:
            pass

    # Alerts
    def test_should_allow_user_to_accept_an_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        self.driver.get_current_url()

    def test_should_allow_user_to_accept_an_alert_with_no_text(self):
        self.driver.find_element_by_id('empty-alert').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        self.driver.get_current_url()

    def test_should_allow_user_to_dismiss_an_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.dismiss()
        self.driver.get_current_url()

    def test_should_allow_user_to_get_text_of_an_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        value = alert.get_text()
        alert.accept()
        self.assertEquals('cheese', value)

    def test_setting_the_value_of_an_alert_throws(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
	with self.assertRaises(ElementNotVisibleException):
	    alert.send_keys('cheese')
        alert.accept()

    def test_alert_should_not_allow_additional_commands_if_dismissed(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        with self.assertRaises(NoSuchAlertException):
            alert.get_text()

    # Prompts
    def test_should_allow_user_to_accept_a_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == '')

    def test_should_allow_user_to_dismiss_a_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.dismiss()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == 'null')

    def test_should_allow_user_to_set_the_value_of_a_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.send_keys('cheese')
        alert.accept()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == 'cheese')

    def test_should_allow_user_to_get_text_of_a_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        value = alert.get_text()
        alert.accept()
        self.assertEquals('Enter something', value)

    def test_prompt_should_not_allow_additional_commands_if_dismissed(self):
        self.driver.find_element_by_id('prompt').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        with self.assertRaises(NoSuchAlertException):
            alert.get_text()

    def test_prompt_should_use_default_value_if_no_keys_sent(self):
        self.driver.find_element_by_id('prompt-with-default').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == 'This is a default value')

    def test_prompt_should_have_null_value_if_dismissed(self):
        self.driver.find_element_by_id('prompt-with-default').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.dismiss()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == 'null')

    # Confirmations
    def test_should_allow_user_to_accept_a_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == 'true')

    def test_should_allow_user_to_dismiss_a_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.dismiss()
        self.wait.until(lambda x: x.find_element_by_id('text').get_text() == 'false')

    def test_setting_the_value_of_a_confirm_throws(self):
        self.driver.find_element_by_id('confirm').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        with self.assertRaises(ElementNotVisibleException):
            alert.send_keys('cheese')
        alert.accept()

    def test_should_allow_user_to_get_text_of_a_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        value = alert.get_text()
        alert.accept()
        self.assertEquals('cheese', value)

    def test_confirm_should_not_allow_additional_commands_if_dismissed(self):
        self.driver.find_element_by_id('confirm').click()
        alert = self.wait.until(lambda x: x.switch_to_alert())
        alert.accept()
        with self.assertRaises(NoSuchAlertException):
            alert.get_text()

    def test_switch_to_missing_alert_fails(self):
    	with self.assertRaises(NoSuchAlertException):
            self.driver.switch_to_alert()

if __name__ == '__main__':
    unittest.main()
