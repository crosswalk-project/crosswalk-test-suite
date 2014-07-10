Feature: Crosswalk test
 Scenario: test storage insurance on trip
  Given I go to "file:///opt/webapi-uiautomation-tests/w3c-webstorage/Storage_example_insurance_on_trip-manual.html"
   Then I should see "you had not been insurance on this trip."
   When I check the "input"
   When I reload
    Then I should see "you had been insurance on this trip."
