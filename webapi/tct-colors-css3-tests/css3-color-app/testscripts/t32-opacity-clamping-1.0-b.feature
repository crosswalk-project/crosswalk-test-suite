Feature: css3-color
 Scenario: t32 opacity clamping b
   When launch "css3-color-app"
     And I go to "colors/csswg/t32-opacity-clamping-1.0-b.htm"
     And I save the page to "t32-opacity-clamping-1.0-b"
    Then pic "t32-opacity-clamping-1.0-b" of baseline and result should be "100" similar if have results
