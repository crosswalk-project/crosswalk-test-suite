Feature: html5-svg
 Scenario: svg label inline
   When launch "html5-svg-app"
     And I go to "svg/svg_label_inline-manual.html"
     And I save the page to "svg_label_inline"
    Then pic "svg_label_inline" of baseline and result should be "100" similar if have results
