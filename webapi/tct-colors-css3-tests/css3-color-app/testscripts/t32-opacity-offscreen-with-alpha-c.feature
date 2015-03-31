Feature: css3-color
 Scenario: t32 opacity offscreen with alpha c
   When launch "css3-color-app"
     And I go to "csswg/t32-opacity-offscreen-with-alpha-c.htm"
     And I save the page to "t32-opacity-offscreen-with-alpha-c"
    Then pic "t32-opacity-offscreen-with-alpha-c" of baseline and result should be "100" similar if have results
