Feature: css3-text
 Scenario: CSS3TextEffects hyphens
   When launch "css3-text-app"
     And I go to "text/CSS3TextEffects_hyphens_manual.html"
     And I save the page to "CSS3TextEffects_hyphens"
     And I save the screenshot md5 as "CSS3TextEffects_hyphens"
    Then file "CSS3TextEffects_hyphens" of baseline and result should be the same
