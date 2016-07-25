Feature: Usecase WebAPI
 Scenario: Others APIs/Es6NumericLiterals Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/Es6NumericLiterals/index.html"
     And I go to frame "resFrame"
    Then I should see "true" in "blog" area
    Then I should see "true" in "olog" area

