Feature: web-system-app
 Scenario: Crosswalk Cookie kill
  When launch "cookie"
   Then I register watcher "creat_cookie" when "Cookie created" click "OK"
   Then I register watcher "read_cookie" when "The value of the cookie is Cookietest" click "OK"
    And I wait 20 seconds
   Then I should see view "description=How cookies work"
    And I fill in "cookievalue" with "Cookietest"
    And I click view "description=Create cookie 1"
    And I force to run all watchers
    And I wait 2 seconds
    And I click view "description=Read cookie 1"
    And I force to run all watchers
    And I execute command "adb shell am force-stop org.xwalk.cookie"
    And launch "cookie"
    And I wait 20 seconds
    And I fill in "cookievalue" with "Cookietest12"
    And I click view "description=Read cookie 1"
    And I force to run all watchers
