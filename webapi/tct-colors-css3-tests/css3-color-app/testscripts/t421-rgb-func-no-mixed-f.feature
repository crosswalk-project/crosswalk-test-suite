Feature: css3-color
 Scenario: t421 rgb func no mixed f
   When launch "css3-color-app"
     And I go to "csswg/t421-rgb-func-no-mixed-f.htm"
     And I save the page to "t421-rgb-func-no-mixed-f"
    Then pic "t421-rgb-func-no-mixed-f" of baseline and result should be "100" similar if have results
