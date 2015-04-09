Feature: css3-fonts
 Scenario: c526 font sz 000
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/c526-font-sz-000-manual.htm"
     And I save the page to "c526-font-sz-000"
    Then pic "c526-font-sz-000" of baseline and result should be "100" similar if have results
