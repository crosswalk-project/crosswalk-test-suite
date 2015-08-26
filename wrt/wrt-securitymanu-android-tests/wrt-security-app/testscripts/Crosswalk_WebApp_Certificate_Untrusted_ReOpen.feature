Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Certificate Untrusted
  When launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "Cancel"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=security_url_certificate_tests" to object "security_app"
    And I swipe saved object "security_app" to "left"
    And launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "Cancel"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
