Feature: Usecase WebAPI
 Scenario: Device & Hardware/Geolocation Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I open wifi
     And I open GPS
     And I go to "/samples/Geolocation/index.html"
    Then I should see "n/a" in "latitudeDiv" area
    Then I should see "n/a" in "longitudeDiv" area
     And I wait 5 seconds
     And I save "latvalue" from "latitudeDiv" area
     And I save "longvalue" from "longitudeDiv" area
    Then "latvalue" should be greater than "0"
    Then "longvalue" should be greater than "0"
