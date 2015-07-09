Feature: Usecase WebAPI
 Scenario: Device & Hardware/Geolocation Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/Geolocation/index.html"
     And I wait 5 seconds
    Then I should see num in "latitudeDiv" area greater than "0"
    Then I should see num in "longitudeDiv" area greater than "0"

