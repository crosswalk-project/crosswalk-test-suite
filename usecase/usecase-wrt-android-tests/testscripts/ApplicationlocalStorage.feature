Feature: Usecase WRT
 Scenario: Web Runtime/ApplicationlocalStorage/restartapp Test
  When I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I click view "description=Clear LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Clear all localStorage value" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I wait for 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I click view "description=Clear LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Clear all localStorage value" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I wait for 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I click view "description=Clear LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Clear all localStorage value" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I wait for 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I click view "description=Clear LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Clear all localStorage value" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I wait for 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I press "recent" hardware key
    And I swipe view "description=localstoragetest" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I click view "description=Clear LocalStorage"
    And I wait for 2 seconds
   Then I expect the content "Clear all localStorage value" in the dumped xml
