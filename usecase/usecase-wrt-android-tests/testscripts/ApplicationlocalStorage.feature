Feature: Usecase WRT
 Scenario: Web Runtime/ApplicationlocalStorage/restartapp Test
  When I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Save localStorage value successfully: test"
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I click view "description=Clear LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Clear all localStorage value"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I wait 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Save localstorage value successfully: test"
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I click view "description=Clear LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Clear all localStorage value"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I wait 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Save localstorage value successfully: test"
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I click view "description=Clear LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Clear all localStorage value"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I wait 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Save localstorage value successfully: test"
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I click view "description=Clear LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Clear all localStorage value"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I wait 2 seconds
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Set LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Save localstorage value successfully: test"
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
    And I launch "localstoragetest" with "org.xwalk.localstoragetest" and "LocalstoragetestActivity" on android
    And I click view "description=Get LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Get localStorage value: test"
    And I click view "description=Clear LocalStorage"
   Then I should see view "className=android.widget.EditText^^^descriptionContains=Clear all localStorage value"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=localstoragetest" to object "lst_app"
    And I swipe saved object "lst_app" to "left"
