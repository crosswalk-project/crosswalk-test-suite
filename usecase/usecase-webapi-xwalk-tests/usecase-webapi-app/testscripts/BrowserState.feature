Feature: Usecase WebAPI
 Scenario: Device & Hardware/BrowserState Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/BrowserState/index.html"
     And I open airplane mode
     And I wait 10 seconds
     And I save "linevalue" from "isonline" area
     And I close airplane mode
    Then "linevalue" should be "online status is false"
     And I wait 10 seconds
    Then I should see "online status is true"

