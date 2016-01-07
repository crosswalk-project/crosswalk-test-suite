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
    And switch to "indexdb"
    And I wait 2 seconds
   Then I should see view "className=android.view.View^^^description=123"
   Then I should see view "className=android.view.View^^^description=Intel"
