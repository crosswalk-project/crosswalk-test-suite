Feature: Usecase WebAPI
 Scenario: Security/Sandbox Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/Sandbox/index.html"
    Then I should see "Filler Text" in "same" area
     And I go to frame "frame1"
    Then I should see "testDiv" area in "green" color
     And I go out of frame
     And I go to frame "frame2"
     And I click "mySubmit"
    Then I should see "Filler Text" with "green" color in "text" area
