Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "colors/csswg/t31-color-text-a.htm"
     And I save the page to "t31-color-text-a"
     And I save the screenshot md5 as "t31-color-text-a"
    Then file "t31-color-text-a" of baseline and result should be the same
