Feature: Usecase WRT
 Scenario: Web Runtime/WebappXwalkHost
  When launch "webappxwalkhost"
   Then I should see "Pass" in 20 seconds
