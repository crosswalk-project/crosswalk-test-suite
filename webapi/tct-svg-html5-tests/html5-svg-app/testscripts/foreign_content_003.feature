Feature: html5-svg
 Scenario: foreign content three rect svg in button
   When launch "html5-svg-app"
     And I go to "svg/w3c/foreign_content_003-manual.html"
     And I save the page to "foreign_content_003"
     And I save the screenshot md5 as "foreign_content_003"
    Then file "foreign_content_003" of baseline and result should be the same
