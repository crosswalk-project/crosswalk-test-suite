Feature: Storage
 Scenario: storage load page times
    When launch "w3c-webstorage-app"
     And I go to "webstorage/Storage_example_load_page_times-manual.html"
     And I press "clear_button"
     And I reload
    Then I should see "You have viewed this page 1 time(s)."
     And I reload
     And I reload
     And I reload
     And I reload
    Then I should see "You have viewed this page 5 time(s)."
