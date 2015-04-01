Feature: css3-fonts
 Scenario: c524 font var 000
   When launch "css3-fonts-app"
     And I go to "csswg/c524-font-var-000-manual.htm"
     And I save the page to "c524-font-var-000"
    Then pic "c524-font-var-000" of baseline and result should be "100" similar if have results
