Feature: css3-color
 Scenario: t32 opacity zorder c
   When launch "css3-color-app"
     And I go to "colors/csswg/t41-html4-keywords-a.htm"
     And I save the page to "t41-html4-keywords-a"
    Then pic "t41-html4-keywords-a" of baseline and result should be "100" similar if have results
