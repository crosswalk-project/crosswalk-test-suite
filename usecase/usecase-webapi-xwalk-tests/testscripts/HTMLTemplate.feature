Feature: Usecase WebAPI
 Scenario: Device & Hardware/HTMLTemplate Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/HTMLTemplate/index.html"
    Then I should see "This sentence comes from template element as a descendant of the head element."
    Then I should see "This sentence comes from template element as a descendant of the body element."

