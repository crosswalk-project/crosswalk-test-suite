Feature: w3c-webstorage
 Scenario: storage insurance on trip
   When launch "css3-color-app"
     And I go to "csswg/t31-color-currentColor-b.htm"
     And I save the page to "css3_colors_tests_entry1"
    Then pic "css3_colors_tests_entry1" of baseline and result should be "100" similar if have results
