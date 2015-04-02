Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "csswg/t421-rgb-hex-parsing-f.htm"
     And I save the page to "t421-rgb-hex-parsing-f"
    Then pic "t421-rgb-hex-parsing-f" of baseline and result should be "100" similar if have results
