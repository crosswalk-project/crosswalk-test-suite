Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebDatabase Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebDatabase/index.html"
     And I fill in "name" with "lucy"
     And I fill in "age" with "13"
     And I press "add"
    Then I should see "lucy" in "tableList" area
    Then I should see "13" in "tableList" area
     And I fill in "name" with "lily"
     And I fill in "age" with "14"
     And I press "add"
    Then I should see "lily" in "tableList" area
    Then I should see "14" in "tableList" area
     And I press "query"
    Then I should see "lily" in "tableList" area
    Then I should see "14" in "tableList" area
    Then I should not see "lucy" in "tableList" area
    Then I should not see "13" in "tableList" area
     And I press "delete"
    Then I should not see "lily" in "tableList" area
    Then I should not see "14" in "tableList" area
    Then I should see "lucy" in "tableList" area
    Then I should see "13" in "tableList" area

