Feature: Usecase WebAPI
 Scenario: Device & Hardware/ShadowDom Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/ShadowDom/index.html"
     And I fill in "form-control" with "Alan Mathison Turing"
     And I click "submit"
    Then I should see "Alan Mathison Turing" in "outPut" area
