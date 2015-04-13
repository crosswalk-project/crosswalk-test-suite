Feature: css3-backgrounds
 Scenario: background 019
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-019-manual.htm"
     And I save the page to "background-019"
     And I save the screenshot md5 as "background-019"
    Then file "background-019" of baseline and result should be the same
