Feature: Usecase WRT
 Scenario: Web Runtime/ChromeProtocol
  When launch "chromeprotocol"
   Then I should see title "Chrome URL Test"
    And I wait 5 seconds
    And I click view "description=chrome://gpu"
   Then I should see view "description=Graphics Feature Status"
    And I wait 2 seconds
    And I press "back" hardware key
   Then I should see title "Chrome URL Test"
