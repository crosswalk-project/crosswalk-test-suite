Feature: xhtml5
 Scenario: page switching
  When launch "webapi-uiautomation-tests"
   And I go to "opt/webapi-uiautomation-tests/html5-extra/xhtml5/area_noref-manual.xhtml"
   And I click "center area"
  Then the browser's URL should be "file:///opt/web-demo-tests/html5-extra/xhtml5/area_noref-manual.xhtml"
  When I click "around area"
  Then the browser's URL should be "file:///opt/web-demo-tests/html5-extra/xhtml5/test-area.xhtml"
