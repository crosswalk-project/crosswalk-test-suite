Feature: css3-text
 Scenario: CSS3TextEffects text shadow none
   When launch "css3-text-app"
     And I go to "text/CSS3TextEffects_text-shadow_none.html"
     And I save the page to "CSS3TextEffects_text-shadow_none"
     And I save the screenshot md5 as "CSS3TextEffects_text-shadow_none"
    Then file "CSS3TextEffects_text-shadow_none" of baseline and result should be the same
