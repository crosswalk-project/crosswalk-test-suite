Feature: Usecase WRT
 Scenario: Web Runtime/SecurityUrlCertificate
  When launch "usecase_wrt_android_tests"
     And I go to "/samples/SecurityUrlCertificate/index.html"
     And I click the link "Open Website"
     And I wait for 5 seconds
     Then I should see an alert
     And I accept the alert
     And I wait for 5 seconds
     Then I should see "sign in" in 5 seconds
