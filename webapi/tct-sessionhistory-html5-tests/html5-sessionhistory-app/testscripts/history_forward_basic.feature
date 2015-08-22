Feature: html5-sessionhistory
 Scenario: history forward basic
   When launch "html5-sessionhistory-app"
     And I go to "sessionhistory/history_forward_basic-manual.html"
     And I go to frame "testIframe"
    Then I should see "001"
     And I wait 6 seconds
    Then I should see "002"
