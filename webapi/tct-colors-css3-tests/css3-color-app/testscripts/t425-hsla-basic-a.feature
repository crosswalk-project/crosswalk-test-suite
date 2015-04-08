Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "csswg/t425-hsla-basic-a.htm"
     And I save the page to "t425-hsla-basic-a"
    Then pic "t425-hsla-basic-a" of baseline and result should be "100" similar if have results
