Feature: html5-svg
 Scenario: svg label inline
   When launch "html5-svg-app"
     And I go to "svg/svg_label_inline-manual.html"
     And I save the page to "svg_label_inline"
     And I save the screenshot md5 as "svg_label_inline"
    Then file "svg_label_inline" of baseline and result should be the same
