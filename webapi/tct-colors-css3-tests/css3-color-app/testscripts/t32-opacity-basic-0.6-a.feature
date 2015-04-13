Feature: css3-color
 Scenario: t32 opacity basic a
   When launch "css3-color-app"
     And I go to "colors/csswg/t32-opacity-basic-0.6-a.htm"
     And I save the page to "t32-opacity-basic-0.6-a"
     And I save the screenshot md5 as "t32-opacity-basic-0.6-a"
    Then file "t32-opacity-basic-0.6-a" of baseline and result should be the same
