Feature: Usecase WebAPI
 Scenario: Social/ContactsManager Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/ContactsManager/index.html"
     And I click "saveButton"
    Then I should see "David" in "David" area
    Then I should see "Beckham" in "David" area
    Then I should see "13913976543" in "David" area
     And I fill in "queryName" with "David"
     And I wait 1 seconds
     And I click "queryButton"
    Then I should see "David" with "red" color in "David" area
    Then I should see "Beckham" with "red" color in "David" area
    Then I should see "13913976543" with "red" color in "David" area
     And I click "clearButton"
     And I wait 3 seconds
    Then I should see nothing in "innerText" attr of "tableList" area
