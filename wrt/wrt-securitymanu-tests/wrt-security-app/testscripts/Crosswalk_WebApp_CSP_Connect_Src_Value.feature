Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Connect Src Value
  When launch "csp_directive_list_tests"
   Then I should see "Pass" with "green" color in "test" area
