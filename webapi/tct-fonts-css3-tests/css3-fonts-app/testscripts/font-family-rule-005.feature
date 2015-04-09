Feature: css3-fonts
 Scenario: font family rule 005
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-family-rule-005-manual.htm"
     And I should see "PASS" in "test" area
