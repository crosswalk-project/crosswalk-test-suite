Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Frame Src None
  When launch "csp_directive_none_tests"
   Then I should not see "Frame A" in "frameTest" area
