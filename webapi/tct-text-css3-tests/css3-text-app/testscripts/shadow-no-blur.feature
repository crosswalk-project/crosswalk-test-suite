Feature: css3-text
 Scenario: css3 TextEffects tests entry7
   When launch "css3-text-app"
     And I go to "text/webkit/shadow-no-blur.html"
     And I save the page to "shadow-no-blur"
    Then pic "shadow-no-blur" of baseline and result should be "100" similar if have results
