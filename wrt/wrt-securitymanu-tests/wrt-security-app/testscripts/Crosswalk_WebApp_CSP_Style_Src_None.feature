Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Style Src None
  When launch "csp_directive_none_tests"
   Then I should see "XXXXX" with "black" color in "styleTest" area
