Feature: css3-color
 Scenario: t32 opacity zorder c
   When launch "css3-color-app"
     And I go to "colors/csswg/t41-html4-keywords-a.htm"
     And I save the page to "t41-html4-keywords-a"
     And I save the screenshot md5 as "t41-html4-keywords-a"
    Then file "t41-html4-keywords-a" of baseline and result should be the same
