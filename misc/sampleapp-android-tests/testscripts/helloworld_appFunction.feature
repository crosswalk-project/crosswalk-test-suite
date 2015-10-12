Feature: helloworld
 Scenario: helloworld appFunction
  When launch "helloworld"
   Then I should see view "description=Hello, world!"
