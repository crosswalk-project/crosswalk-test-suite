Feature: css3-fonts
 Scenario: c524 font var 000
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/c524-font-var-000-manual.htm"
     And I save the page to "c524-font-var-000"
     And I save the screenshot md5 as "c524-font-var-000"
    Then file "c524-font-var-000" of baseline and result should be the same
