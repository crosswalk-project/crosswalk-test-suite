Feature: css3-fonts
 Scenario: font weight 013
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-013-manual.htm"
     And I save the page to "font-weight-013"
     And I save the screenshot md5 as "font-weight-013"
    Then file "font-weight-013" of baseline and result should be the same
