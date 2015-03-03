Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebStorage Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebStorage/index.html"
     And I fill in element "session" by "id" with "hi"
     And I fill in element "local" by "id" with "hellow"
     And I click element with id "add" by js
    Then I should see "hi" in "tableList" area
    Then I should see "hellow" in "tableList" area
     And I click element with id "clear" by js
    Then I should see "storage removed" 

