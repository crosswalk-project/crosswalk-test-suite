Feature: gallery
 Scenario: gallery orientation
  When launch "gallery"
   Then I should see view "description=blueimp Gallery"
    And I press "home" hardware key
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=Gallery" to object "gall_app"
    And I click saved object "gall_app"
   Then I should see view "description=blueimp Gallery"
