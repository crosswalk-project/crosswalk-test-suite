Feature: css3-backgrounds
 Scenario: background 012
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-012-manual.htm"
     And I save the page to "background-012"
     And I save the screenshot md5 as "background-012"
    Then file "background-012" of baseline and result should be the same
