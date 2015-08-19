Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Certificate Untrusted
  When launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "Cancel"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
