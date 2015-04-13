Feature: css3-fonts
 Scenario: font family invalid characters 001
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-family-invalid-characters-001-manual.htm"
     And I save the page to "font-family-invalid-characters-001"
     And I save the screenshot md5 as "font-family-invalid-characters-001"
    Then file "font-family-invalid-characters-001" of baseline and result should be the same
