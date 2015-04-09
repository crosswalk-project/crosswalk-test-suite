Feature: css3-fonts
 Scenario: font weight 014
   When launch "css3-fonts-app"
     And I go to "csswg/font-weight-014-manual.htm"
     And I save the page to "font-weight-014"
    Then pic "font-weight-014" of baseline and result should be "100" similar if have results
