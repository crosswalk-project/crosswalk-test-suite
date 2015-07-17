Feature: mark
 Scenario: mark element
   When launch "html5-extra-app"
     And I go to "semantics/text-level-semantics/the-mark-element/mark_element_base_usage-manual.html"
     And I save the page to "mark_element_base_usage"
     And I save the screenshot md5 as "mark_element_base_usage"
    Then file "mark_element_base_usage" of baseline and result should be the same
