Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "colors/csswg/t422-rgba-a0.0-a.htm"
     And I save the page to "t422-rgba-a0.0-a"
     And I save the screenshot md5 as "t422-rgba-a0.0-a"
    Then file "t422-rgba-a0.0-a" of baseline and result should be the same
