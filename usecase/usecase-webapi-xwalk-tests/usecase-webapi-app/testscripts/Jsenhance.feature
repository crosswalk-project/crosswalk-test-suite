Feature: Usecase WebAPI
 Scenario: Multimedia & Graphics/Jsenhance Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/Jsenhance/index.html"
    Then I should see "PASS" with "green" color in "test1" area
