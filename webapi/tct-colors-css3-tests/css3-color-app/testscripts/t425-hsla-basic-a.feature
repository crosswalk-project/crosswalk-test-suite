Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "colors/csswg/t425-hsla-basic-a.htm"
     And I save the page to "t425-hsla-basic-a"
     And I save the screenshot md5 as "t425-hsla-basic-a"
    Then file "t425-hsla-basic-a" of baseline and result should be the same
