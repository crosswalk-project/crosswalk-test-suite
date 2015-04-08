Feature: xhtml5
 Scenario: page switching
  When launch "html5-extra-app"
   And I go to "xhtml5/body_link-manual.xhtml"
   And I should see "LINK" with "yellow" color in "testlink" area
   And I click "testlink"
  Then The current URL should be "xhtml5/test-body.xhtml"
   And I click "testback"
  Then The current URL should be "xhtml5/body_link-manual.xhtml"
   And I should see "LINK" with "blue" color in "testlink" area
