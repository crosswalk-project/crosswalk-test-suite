Feature: css3-color
 Scenario: t31 color currentColor b
   When launch "css3-color-app"
     And I go to "csswg/t31-color-currentColor-b.htm"
     And I save the page to "t31-color-currentColor-b"
    Then pic "t31-color-currentColor-b" of baseline and result should be "100" similar if have results
