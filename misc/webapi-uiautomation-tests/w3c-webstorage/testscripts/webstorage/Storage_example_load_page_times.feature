Feature: Crosswalk test
 Scenario: test storage load page times
  Given I go to "file:///opt/webapi-uiautomation-tests/w3c-webstorage/Storage_example_load_page_times-manual.html"
    When I check the "button"
    When I reload
      Then I should see "You have viewed this page 1 time(s)."
    When I reload
    When I reload
    When I reload
    When I reload
      Then I should see "You have viewed this page 5 time(s)."
