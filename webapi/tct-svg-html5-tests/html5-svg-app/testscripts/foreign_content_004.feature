Feature: html5-svg
 Scenario: foreign content four rect svg in caption
   When launch "html5-svg-app"
     And I go to "svg/w3c/foreign_content_004-manual.html"
     And I save the page to "foreign_content_004"
    Then pic "foreign_content_004" of baseline and result should be "100" similar if have results
