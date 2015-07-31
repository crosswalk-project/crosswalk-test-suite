Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Frame Src Value
  When launch "csp_directive_list_tests"
   Then I should see "Frame A" in "frameTest" area
