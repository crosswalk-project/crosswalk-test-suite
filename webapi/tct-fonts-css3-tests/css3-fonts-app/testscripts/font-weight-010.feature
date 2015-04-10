Feature: css3-fonts
 Scenario: font weight 010
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-010-manual.htm"
     And I save the page to "font-weight-010"
     And I save the screenshot md5 as "font-weight-010"
    Then file "font-weight-010" of baseline and result should be the same
