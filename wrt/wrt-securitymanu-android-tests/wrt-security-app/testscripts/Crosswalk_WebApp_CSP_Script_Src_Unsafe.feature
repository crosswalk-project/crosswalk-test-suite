Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Script Src Unsafe
  When launch "csp_script_unsafe_tests"
   Then I should see "Pass" with "green" color in "test" area
