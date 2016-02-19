Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Style Src Value
  When launch "csp_directive_list_tests"
   Then I should see "XXXXX" with "blue" color in "styleTest" area
