Feature: css3-fonts
 Scenario: font 008
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-008-manual.htm"
     And I save the page to "font-008"
     And I save the screenshot md5 as "font-008"
    Then file "font-008" of baseline and result should be the same
