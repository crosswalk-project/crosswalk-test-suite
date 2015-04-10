Feature: css3-fonts
 Scenario: c525 font wt 000
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/c525-font-wt-000-manual.htm"
     And I save the page to "c525-font-wt-000"
     And I save the screenshot md5 as "c525-font-wt-000"
    Then file "c525-font-wt-000" of baseline and result should be the same
