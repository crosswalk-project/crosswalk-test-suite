Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "colors/csswg/t425-hsla-onscreen-b-manual.htm"
     And I save the page to "t425-hsla-onscreen-b"
    Then pic "t425-hsla-onscreen-b" of baseline and result should be "100" similar if have results
