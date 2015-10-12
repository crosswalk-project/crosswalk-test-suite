Feature: helloworld
 Scenario: helloworld orientation
  When launch "helloworld"
   Then I should see view "description=Hello, world!"
    And I set orientation "l"
   Then I should see view "description=Hello, world!"
    And I set orientation "r"
   Then I should see view "description=Hello, world!"
