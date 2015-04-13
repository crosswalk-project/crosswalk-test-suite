Feature: css3-text
 Scenario: CSS3TextEffects overflow wrap breakword
   When launch "css3-text-app"
     And I go to "text/CSS3TextEffects_overflow-wrap_breakword.html"
     And I save the page to "CSS3TextEffects_overflow-wrap_breakword"
     And I save the screenshot md5 as "CSS3TextEffects_overflow-wrap_breakword"
    Then file "CSS3TextEffects_overflow-wrap_breakword" of baseline and result should be the same
