Feature: css3-color
 Scenario: t32 opacity offscreen with alpha c
   When launch "css3-color-app"
     And I go to "colors/csswg/t32-opacity-offscreen-with-alpha-c.htm"
     And I save the page to "t32-opacity-offscreen-with-alpha-c"
     And I save the screenshot md5 as "t32-opacity-offscreen-with-alpha-c"
    Then file "t32-opacity-offscreen-with-alpha-c" of baseline and result should be the same
