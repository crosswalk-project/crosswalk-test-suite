Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebStorage Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebStorage/index.html"
     And I fill in "session" with "hi"
     And I fill in "local" with "hellow"
     And I click "add"
    Then I should see "hi" in "tableList" area
    Then I should see "hellow" in "tableList" area
     And I click "clear"
    Then I should see "storage removed" 

