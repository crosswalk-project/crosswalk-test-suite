Feature: figcaption
 Scenario: figcaption element
   When launch "html5-extra-app"
     And I go to "semantics/grouping-content/the-figcaption-element/figcaption_element-manual.html"
     And I save the page to "figcaption_element"
     And I save the screenshot md5 as "figcaption_element"
    Then file "figcaption_element" of baseline and result should be the same
