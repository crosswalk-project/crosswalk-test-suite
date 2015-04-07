Feature: css3-text
 Scenario: CSS3TextEffects word wrap normal
   When launch "css3-text-app"
     And I go to "text/CSS3TextEffects_word-wrap_normal.html"
     And I save the page to "CSS3TextEffects_word-wrap_normal"
    Then pic "CSS3TextEffects_word-wrap_normal" of baseline and result should be "100" similar if have results
