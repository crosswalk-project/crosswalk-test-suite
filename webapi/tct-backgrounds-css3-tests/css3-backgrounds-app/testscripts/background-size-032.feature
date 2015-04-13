Feature: css3-backgrounds
 Scenario: background size 032
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-size-032-manual.html"
     And I save the page to "background-size-032"
     And I save the screenshot md5 as "background-size-032"
    Then file "background-size-032" of baseline and result should be the same
