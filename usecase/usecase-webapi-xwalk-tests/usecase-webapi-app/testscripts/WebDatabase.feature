Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebDatabase Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebDatabase/index.html"
     And I fill in element "name" by "id" with "lucy"
     And I fill in element "age" by "id" with "13"
     And I click element with id "add" by js
    Then I should see "lucy" in "tableList" area
    Then I should see "13" in "tableList" area
     And I fill in element "name" by "id" with "lily"
     And I fill in element "age" by "id" with "14"
     And I click element with id "add" by js
    Then I should see "lily" in "tableList" area
    Then I should see "14" in "tableList" area
     And I click element with id "query" by js
    Then I should see "lily" in "tableList" area
    Then I should see "14" in "tableList" area
    Then I should not see "lucy" in "tableList" area
    Then I should not see "13" in "tableList" area
     And I click element with id "delete" by js
    Then I should not see "lily" in "tableList" area
    Then I should not see "14" in "tableList" area
    Then I should see "lucy" in "tableList" area
    Then I should see "13" in "tableList" area
