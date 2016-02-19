Feature: wrt-security-app
 Scenario: Crosswalk WebApp CSP Img Src Value
  When launch "csp_directive_none_tests"
   Then I should not see view "className=android.widget.Image^^^description=icon-128"
