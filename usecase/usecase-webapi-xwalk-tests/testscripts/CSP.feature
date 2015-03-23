Feature: Usecase WebAPI
 Scenario: Security/CSP/csp-none Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/csp-none/index.html"
    Then I should see "t1" area in "white" color
    Then I should see "PASS" in "h3" area

 Scenario: Security/CSP/csp-self Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/csp-self/index.html"
    Then I should see "Pass" in "t1" area
    Then I should see "Pass" in "t2" area

 Scenario: Security/CSP/csp-asterisk Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/csp-asterisk/index.html"
    Then I should see "Pass" in "t1" area

 Scenario: Security/CSP/csp-cross-origin Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/csp-cross-origin/index.html"
    Then I should see "Pass" in "t1" area
    Then I should see "Pass" in "t2" area
    Then I should see "Pass" in "t3" area
    Then I should see "frame1" area in "white" color

 Scenario: Security/CSP/default-src_asterisk Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/default-src_asterisk/index.html"
    Then I should see "PASS"

 Scenario: Security/CSP/sandbox-same-origin-allow-scripts Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/sandbox-same-origin-allow-scripts/index.html"
    Then I should not see "Fail"

 Scenario: Security/CSP/script-src_inline_eval Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/script-src_inline_eval/index.html"
    Then I should not see "FAIL"

 Scenario: Security/CSP/style-src_self Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/style-src_self/index.html"
    Then I should not see "FAIL"
    Then I should see "test-blue" area in "blue" color

 Scenario: Security/CSP/csp-default-src-self Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/CSP/res/default-src_self/index.html"
     And I save div "test1" as "pic1" with width "75" and height "0"
     And I save div "test2" as "pic2" with width "75" and height "0"
     And I save div "test" as "pic3" with width "75" and height "0"
    Then pic "pic1" and pic "pic2" should be more than "99" similar
    Then pic "pic1" and pic "pic3" should be less than "99" similar
     And I remove all the pictures
    Then I should see "PASS" in "text1" area
    Then I should see "test-blue" area in "blue" color 

