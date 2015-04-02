Feature: css3-fonts
 Scenario: c525 font wt 000
   When launch "css3-fonts-app"
     And I go to "csswg/c525-font-wt-000-manual.htm"
     And I save the page to "c525-font-wt-000"
    Then pic "c525-font-wt-000" of baseline and result should be "100" similar if have results
