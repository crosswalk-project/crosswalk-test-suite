Feature: css3-backgrounds
 Scenario: background 011
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-011-manual.htm"
     And I save the page to "background-011"
     And I save the screenshot md5 as "background-011"
    Then file "background-011" of baseline and result should be the same
