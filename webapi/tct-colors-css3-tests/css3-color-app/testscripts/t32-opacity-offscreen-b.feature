Feature: css3-color
 Scenario: t32 opacity offscreen b
   When launch "css3-color-app"
     And I go to "colors/csswg/t32-opacity-offscreen-b.htm"
     And I save the page to "t32-opacity-offscreen-b"
     And I save the screenshot md5 as "t32-opacity-offscreen-b"
    Then file "t32-opacity-offscreen-b" of baseline and result should be the same
