Feature: xhtml5
 Scenario: page switching
  When launch "html5-extra-app"
   And I go to "xhtml5/area_noref-manual.xhtml"
   And I click coords 60 and 60 of "src_img"
  Then The current URL should be "xhtml5/area_noref-manual.xhtml"
   And I click coords 10 and 10 of "src_img"
  Then The current URL should be "xhtml5/test-area.xhtml"
