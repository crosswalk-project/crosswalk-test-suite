Feature: css3-color
 Scenario: t421 rgb func whitespace b
   When launch "css3-color-app"
     And I go to "csswg/t421-rgb-func-whitespace-b.htm"
     And I save the page to "t421-rgb-func-whitespace-b"
    Then pic "t421-rgb-func-whitespace-b" of baseline and result should be "100" similar if have results
