Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Script Src None
  When launch "csp_script_none_tests"
   Then I should see "Pass" with "green" color in "test" area