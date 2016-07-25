Feature: Usecase WebAPI
 Scenario: Experimental API/SIMD Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/SIMD/index.html"
     And I go to frame "simdframe"
     And I click "start"
     And I wait 10 seconds
     And I click "Stop"
     And I save "FTP-value 1" from "fps" area
     And I click "simd"
     And I click "start"
     And I wait 10 seconds
     And I click "Stop"
     And I save "FTP-value 2" from "fps" area
    Then "FTP-value 1" should be less than "FTP-value 2" beyond "1"
