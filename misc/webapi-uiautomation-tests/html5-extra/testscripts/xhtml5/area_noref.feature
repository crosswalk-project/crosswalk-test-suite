Feature: Crosswalk test
 Scenario: test page jump
  Given I go to "file:///opt/webapi-uiautomation-tests/html5-extra/xhtml5/area_noref-manual.xhtml"
   When I click center area
   Then the browser's URL should be "file:///opt/webapi-uiautomation-tests/html5-extra/xhtml5/area_noref-manual.xhtml"
   When I click around area
   Then the browser's URL should be "file:///opt/webapi-uiautomation-tests/html5-extra/xhtml5/test-area.xhtml"
