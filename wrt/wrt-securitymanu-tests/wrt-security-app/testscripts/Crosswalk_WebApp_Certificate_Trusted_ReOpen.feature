Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Certificate Trusted ReOpen
  When launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "OK"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "className=android.view.View^^^description=12306yjfk@rails.com.cn" in 30 seconds
    And I press "recent" hardware key
    And I wait 2 seconds
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=security_url_certificate_tests" to object "security_app"
    And I swipe saved object "security_app" to "left"
    And launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "OK"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "className=android.view.View^^^description=12306yjfk@rails.com.cn" in 30 seconds
