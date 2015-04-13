Feature: css3-fonts
 Scenario: font weight 015
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-015-manual.htm"
     And I save the page to "font-weight-015"
     And I save the screenshot md5 as "font-weight-015"
    Then file "font-weight-015" of baseline and result should be the same
