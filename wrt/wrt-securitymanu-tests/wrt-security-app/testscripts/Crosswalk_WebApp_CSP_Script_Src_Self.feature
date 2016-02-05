Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Script Src Self
  When launch "csp_script_self_tests"
   Then I should see "Pass" with "green" color in "test" area
