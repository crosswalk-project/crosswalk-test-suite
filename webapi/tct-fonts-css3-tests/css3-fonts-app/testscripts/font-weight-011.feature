Feature: css3-fonts
 Scenario: font weight 011
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-011-manual.htm"
     And I save the page to "font-weight-011"
     And I save the screenshot md5 as "font-weight-011"
    Then file "font-weight-011" of baseline and result should be the same
