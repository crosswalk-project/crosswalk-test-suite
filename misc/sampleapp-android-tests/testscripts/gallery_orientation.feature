Feature: gallery
 Scenario: gallery orientation
  When launch "gallery"
   Then I should see view "description=blueimp Gallery"
    And I set orientation "l"
   Then I should see view "description=blueimp Gallery"
    And I set orientation "r"
   Then I should see view "description=blueimp Gallery"
