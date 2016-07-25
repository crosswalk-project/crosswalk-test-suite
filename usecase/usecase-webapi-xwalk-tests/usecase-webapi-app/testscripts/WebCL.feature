Feature: Usecase WebAPI
 Scenario: Device & Hardware/WebCL Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/WebCL/index.html"
     And I wait 2 seconds
     And I go to frame "webclframe"
     And I click "b1"
     And I wait 5 seconds
     And I save "value1_fps" from "fps" area 
     And I click "b1"
     And I wait 5 seconds
     And I save "value2_fps" from "fps" area 
    Then "value2_fps" should be greater than "value1_fps"
