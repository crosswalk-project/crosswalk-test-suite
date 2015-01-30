Feature: Usecase WebAPI
 Scenario: Performance & Optimization/NavigationTiming Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/NavigationTiming/index.html"
     And I click "getNavigationTiming"
    Then I should not see "N/A"

