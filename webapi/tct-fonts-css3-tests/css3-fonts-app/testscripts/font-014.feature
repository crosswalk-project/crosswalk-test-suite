Feature: css3-fonts
 Scenario: font 014
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-014-manual.htm"
     And I save the page to "font-014"
     And I save the screenshot md5 as "font-014"
    Then file "font-014" of baseline and result should be the same
