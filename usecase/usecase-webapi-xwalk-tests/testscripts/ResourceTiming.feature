Feature: Usecase WebAPI
 Scenario: Performance & Optimization/ResourceTiming Test
    When launch "usecase-webapi-xwalk-tests"
    And I go to "/samples/ResourceTiming/index.html"
    And I press "requestShow"
    And I wait for 5 seconds
    Then I should see "ms" in "fetchStart_redirectStart" area
    Then I should see "ms" in "domainLookupStart_redirectStart" area
    Then I should see "ms" in "connectStart_domainLookupEnd" area
    Then I should see "ms" in "responseEnd_requestStart" area
    Then I should see "ms" in "responseEnd_redirectStart" area

