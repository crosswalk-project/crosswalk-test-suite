Feature: css3-text
 Scenario: CSS3TextEffects text shadow none
   When launch "css3-text-app"
     And I go to "text/CSS3TextEffects_text-shadow_none.html"
     And I save the page to "CSS3TextEffects_text-shadow_none"
    Then pic "CSS3TextEffects_text-shadow_none" of baseline and result should be "100" similar if have results
