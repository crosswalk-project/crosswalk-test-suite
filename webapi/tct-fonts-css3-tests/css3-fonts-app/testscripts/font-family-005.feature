Feature: css3-fonts
 Scenario: font family 005
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-family-005-manual.htm"
     And I save the page to "font-family-005"
     And I save the screenshot md5 as "font-family-005"
    Then file "font-family-005" of baseline and result should be the same
