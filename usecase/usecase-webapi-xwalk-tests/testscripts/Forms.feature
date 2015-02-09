Feature: Usecase WebAPI
 Scenario: Device & Hardware/Forms Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/Forms/index.html"
     And I go to frame "myiframe"
     And I fill in "myinput" with "12345"
     And I click "Reset"
    Then I should see nothing in "value" attr of "myinput" area
     And I fill in "myinput" with "12345~!@#><?{:}"
     And I click "Reset"
    Then I should see nothing in "value" attr of "myinput" area
     And I click "Submit"
    Then I should see "PASS" with "green" color in "test1" area

