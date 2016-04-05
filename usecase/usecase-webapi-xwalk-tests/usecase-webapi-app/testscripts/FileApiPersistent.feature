Feature: Usecase WebAPI
 Scenario: Others APIs/FileApiPersistent Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/FileApiPersistent/index.html"
     And I go to frame "resFrame"
     And I click "bt1"
    Then I should see "Write completed" in "log" area
     And I click "bt2"
    Then I should see "PERSISTENT CONTENT" in "log" area

