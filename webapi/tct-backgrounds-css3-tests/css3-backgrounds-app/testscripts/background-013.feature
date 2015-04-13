Feature: css3-backgrounds
 Scenario: background 013
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-013-manual.htm"
     And I save the page to "background-013"
     And I save the screenshot md5 as "background-013"
    Then file "background-013" of baseline and result should be the same
