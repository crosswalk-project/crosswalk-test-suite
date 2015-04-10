Feature: css3-fonts
 Scenario: font weight 014
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-014-manual.htm"
     And I save the page to "font-weight-014"
     And I save the screenshot md5 as "font-weight-014"
    Then file "font-weight-014" of baseline and result should be the same
