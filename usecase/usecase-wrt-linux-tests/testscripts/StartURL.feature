Feature: Usecase Linux
 Scenario: Runtime/StartURL/localsource test
  When launch "localsource"
  Then I should see "Test passes if the test app could be launched successfully"

 Scenario: Runtime/StartURL/websource test
  When launch "websource"
  Then I should see "FAQ" in 60 seconds
