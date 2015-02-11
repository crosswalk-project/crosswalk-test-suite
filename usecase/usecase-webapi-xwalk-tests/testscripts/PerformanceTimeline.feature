Feature: Usecase WebAPI
 Scenario: Performance & Optimization/PerformanceTimeline Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/PerformanceTimeline/index.html"
     And I press "pc1_send"
     And I wait 20 seconds
    Then I should see "http://test.csswg.org/source/support/cat.png" in "name" area
    Then I should see "resource" in "entryType" area
    Then I should see "ms" in "start" area
    Then I should see "ms" in "duration" area

