Feature: xhtml5
 Scenario: page switching
  When launch "webapi-uiautomation-tests"
   And I go to "opt/webapi-uiautomation-tests/html5-extra/xhtml5/area_noref-manual.xhtml"
   And I click coords 60 and 60 of "src_img"
  Then The current URL should be "opt/webapi-uiautomation-tests/html5-extra/xhtml5/area_noref-manual.xhtml"
   And I click coords 10 and 10 of "src_img"
  Then The current URL should be "opt/webapi-uiautomation-tests/html5-extra/xhtml5/test-area.xhtml"
