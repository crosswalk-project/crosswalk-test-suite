Feature: css3-fonts
 Scenario: font 027
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-027-manual.htm"
     And I save the page to "font-027"
     And I save the screenshot md5 as "font-027"
    Then file "font-027" of baseline and result should be the same
