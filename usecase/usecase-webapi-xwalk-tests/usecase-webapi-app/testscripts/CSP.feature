Feature: Usecase WebAPI
 Scenario: Security/CSP/csp-none Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/CSP/res/csp-none/index.html"
    Then I should see "ABCD" with "red" color in "csp_local" area
    Then I should see "ABCD" with "red" color in "csp_online" area

 Scenario: Security/CSP/csp-asterisk Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/CSP/res/csp-asterisk/index.html"
     And I save the page to "csp-asterisk"
     And I save the screenshot md5 as "csp-asterisk"
    Then file "csp-asterisk" of baseline and result should be the same

 Scenario: Security/CSP/sandbox-same-origin-allow-scripts Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/CSP/res/sandbox-same-origin-allow-scripts/index.html"
    Then I should see "Filler Text" in "test" area
    Then I should see "Filler Text" in "test2" area

 Scenario: Security/CSP/csp-default-src-self Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/CSP/res/default-src_self/index.html"
     And I save the page to "default-src_self"
     And I save the screenshot md5 as "default-src_self"
    Then file "default-src_self" of baseline and result should be the same
