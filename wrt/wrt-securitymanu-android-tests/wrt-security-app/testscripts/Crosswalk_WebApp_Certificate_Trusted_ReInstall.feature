Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Certificate Trusted ReInstall
  When launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "OK"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "className=android.view.View^^^description=12306yjfk@rails.com.cn" in 30 seconds
    And uninstall "org.xwalk.security_url_certificate_tests"
    And install "../../security_url_certificate_tests.apk"
    And launch "security_url_certificate_tests"
   Then I should see view "description=Security URL Certificate Test" in 10 seconds
    And I register watcher "security" when "Ssl Certificate Error Alert" click "OK"
    And I click view "className=android.view.View^^^description=Open website"
   Then I should see view "className=android.view.View^^^description=12306yjfk@rails.com.cn" in 30 seconds
