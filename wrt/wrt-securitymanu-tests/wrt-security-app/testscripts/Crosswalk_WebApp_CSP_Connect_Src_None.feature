Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Connect Src None
  When launch "csp_directive_none_tests"
   Then I should see "Pass" with "green" color in "test" area
