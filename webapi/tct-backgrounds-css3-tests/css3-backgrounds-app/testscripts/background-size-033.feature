Feature: css3-backgrounds
 Scenario: background size 033
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-size-033-manual.html"
     And I save the page to "background-size-033"
     And I save the screenshot md5 as "background-size-033"
    Then file "background-size-033" of baseline and result should be the same
