Feature: Usecase WebAPI
 Scenario: Networking & Storage/IndexedDB Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/IndexedDB/index.html"
     And I fill in "txtName" with "name"
     And I fill in "txtEmail" with "lucy"
     And I click element with id "btnAdd" by js
    Then I should see "name" in "tableList" area
    Then I should see "lucy" in "tableList" area
     And I fill in "txtName" with "class"
     And I fill in "txtEmail" with "student"
     And I click element with id "btnAdd" by js
    Then I should see "class" in "tableList" area
    Then I should see "student" in "tableList" area
     And I fill in "txtID" with "name"
     And I click element with id "btnDelete" by js
    Then I should not see "name" in "tableList" area
    Then I should not see "lucy" in "tableList" area

