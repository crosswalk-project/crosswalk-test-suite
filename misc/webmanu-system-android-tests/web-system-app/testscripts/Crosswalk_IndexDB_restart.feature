Feature: web-system-app
 Scenario: Crosswalk IndexDB restart
  When launch "indexdb"
    And I fill in "txtName" with "123"
    And I fill in "txtEmail" with "Intel"
    And I click view "description=Add"
   Then I should see view "className=android.view.View^^^description=123"
   Then I should see view "className=android.view.View^^^description=Intel"
    And I fill in "txtID" with "123"
    And I click view "description=Delete"
   Then I should see view "className=android.view.View^^^description=No Record"
    And I click view "description=Add"
   Then I should see view "className=android.view.View^^^description=123"
   Then I should see view "className=android.view.View^^^description=Intel"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=IndexDB" to object "indexdb_app"
    And I swipe saved object "indexdb_app" to "left"
   Then I should not see view "description=Add Record"
    And I launch "indexdb" with "org.xwalk.indexdb" and "IndexdbActivity" on android
    And I wait 2 seconds
   Then I should see view "className=android.view.View^^^description=123"
   Then I should see view "className=android.view.View^^^description=Intel"
