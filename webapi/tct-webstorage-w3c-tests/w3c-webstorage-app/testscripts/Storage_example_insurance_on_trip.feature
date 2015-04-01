Feature: w3c-webstorage
 Scenario: storage insurance on trip
   When launch "w3c-webstorage-app"
    And I go to "webstorage/Storage_example_insurance_on_trip-manual.html"
    And I wait for 16 seconds
   Then I should see "you had not been insurance on this trip."
    And I check "test_checkbox"
    And I reload
   Then I should see "you had been insurance on this trip."
