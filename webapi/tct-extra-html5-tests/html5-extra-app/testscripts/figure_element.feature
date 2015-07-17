Feature: figure
 Scenario: figure element
   When launch "html5-extra-app"
     And I go to "semantics/grouping-content/the-figure-element/figure_element-manual.html"
     And I save the page to "figure_element"
     And I save the screenshot md5 as "figure_element"
    Then file "figure_element" of baseline and result should be the same
