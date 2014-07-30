Feature: w3c-webstorage
 Scenario: storage insurance on trip
   When launch "webapi-uiautomation-tests"
    And I go to "opt/webapi-uiautomation-tests/w3c-webstorage/Storage_example_insurance_on_trip-manual.html"
   Then I should see "you had not been insurance on this trip."
    And I check the "input"
    And I reload
   Then I should see "you had been insurance on this trip."
