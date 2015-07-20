Feature: Usecase WebAPI
 Scenario: Device & Hardware/WebCL Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebCL/index.html"
     And I wait 2 seconds
     And I go to frame "webclframe"
     And I click "b1"
     And I wait 5 seconds
    Then I check "fps" is "smaller" and "sms" is "larger" than after click "b1" for 10 seconds

