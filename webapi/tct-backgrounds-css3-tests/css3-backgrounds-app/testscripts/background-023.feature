Feature: css3-backgrounds
 Scenario: background 023
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-023-manual.htm"
     And I save the page to "background-023"
     And I save the screenshot md5 as "background-023"
    Then file "background-023" of baseline and result should be the same
