Feature: Sandbox
 Scenario: sandbox attri default block submit
    When launch "html5-sandbox-app"
     And I go to "w3c/sandbox_007-manual.htm"
     And I go to frame "content"
     And I press "submitButton"
    Then I should not see "FAIL"
