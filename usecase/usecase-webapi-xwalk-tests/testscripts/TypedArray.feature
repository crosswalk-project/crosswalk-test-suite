Feature: Usecase WebAPI
 Scenario: Performance & Optimization/TypedArray Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/TypedArray/index.html"
    Then I should see "0" in "00" area
    Then I should see "0" in "01" area
    Then I should see "0" in "02" area
    Then I should see "0" in "03" area
    Then I should see "0" in "10" area
    Then I should see "0" in "11" area
    Then I should see "0" in "12" area
    Then I should see "0" in "13" area
    Then I should see "0" in "20" area
    Then I should see "0" in "21" area
    Then I should see "0" in "22" area
    Then I should see "0" in "23" area
    Then I should see "0" in "30" area
    Then I should see "0" in "31" area
    Then I should see "0" in "32" area
    Then I should see "0" in "33" area
     And I click "setValue"
    Then I should see "1" in "00" area
    Then I should see "1" in "01" area
    Then I should see "1" in "02" area
    Then I should see "1" in "03" area
    Then I should see "1" in "10" area
    Then I should see "1" in "11" area
    Then I should see "1" in "12" area
    Then I should see "1" in "13" area
    Then I should see "1" in "20" area
    Then I should see "1" in "21" area
    Then I should see "1" in "22" area
    Then I should see "1" in "23" area
    Then I should see "1" in "30" area
    Then I should see "1" in "31" area
    Then I should see "1" in "32" area
    Then I should see "1" in "33" area

