Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebStorage Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/WebStorage/index.html"
     And I fill in element "session" by "id" with "hi"
     And I fill in element "local" by "id" with "hello"
     And I click element with id "add" by js
    Then I should see "hi" in "tableList" area
    Then I should see "hello" in "tableList" area
     And I fill in element "local" by "id" with "none"
     And I click element with id "remove" by js
    Then I should not see "hi" in "tableList" area
    Then I should see "hello" in "tableList" area

