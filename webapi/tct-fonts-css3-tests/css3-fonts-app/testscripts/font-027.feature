Feature: css3-fonts
 Scenario: font 027
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-027-manual.htm"
     And I save the page to "font-027"
    Then pic "font-027" of baseline and result should be "100" similar if have results
