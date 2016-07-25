Feature: Usecase WebAPI
 Scenario: Device & Hardware/WebCrypto Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/WebCrypto/index.html"
     And I click "generateKeyPair"
    Then I should not see "Generate key pair failed" in "publicKey" area
     And I click "signData"
    Then I should not see "Sign data failed" in "publicKey" area
     And I click "verifyData"
    Then I should not see "verify data failed" in "publicKey" area
