Feature: gallery
 Scenario: gallery checking
  When launch "gallery"
   # check home page
   Then I should see title "Image Gallery"
   And I should see "View Your Photos On Wireless Display"

   # check "Crosswalk" hyperlink
   And I should see "Crosswalk"
   Then I verify "Crosswalk" with link "https://crosswalk-project.org/"

   # check "blueimp Gallery" hyperlink
   And I should see "blueimp Gallery"
   Then I verify "blueimp Gallery" with link "https://github.com/blueimp/Gallery"

   # check "Presentation API" hyperlink
   And I should see "Presentation API"
   Then I verify "Presentation API" with link "http://otcshare.github.io/presentation-spec/index.html"

   # check help content
   And I press "Click here for how to setup wireless display."
   Then I should see "Requirements"
   And I should see "How to Setup Wireless Display"
   And I should see "Use Simulated Secondary Display"

 
