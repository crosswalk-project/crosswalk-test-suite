Feature: css3-backgrounds
 Scenario: CSS3BG background position 2cm 1cm
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/CSS3BG_background-position_2cm_1cm-manual.html"
     And I save the page to "CSS3BG_background-position_2cm_1cm"
    Then pic "CSS3BG_background-position_2cm_1cm" of baseline and result should be "100" similar if have results
