Feature: css3-text
 Scenario: CSS3TextEffects text align left
   When launch "css3-text-app"
     And I go to "text/csswg/text-align-001.html"
     And I save the page to "text-align-001"
     And I save the screenshot md5 as "text-align-001"
    Then file "text-align-001" of baseline and result should be the same
