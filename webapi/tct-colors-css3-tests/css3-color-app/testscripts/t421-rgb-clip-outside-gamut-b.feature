Feature: css3-color
 Scenario: t421 rgb clip outside gamut b
   When launch "css3-color-app"
     And I go to "colors/csswg/t421-rgb-clip-outside-gamut-b.htm"
     And I save the page to "t421-rgb-clip-outside-gamut-b"
    Then pic "t421-rgb-clip-outside-gamut-b" of baseline and result should be "100" similar if have results
