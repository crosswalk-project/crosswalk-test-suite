Feature: gallery
 Scenario: gallery checking
  When launch "gallery"
   # check home page
   #Then I should see title "Blueimp Gallery"
   #And I should see "View Your Photos On Wireless Display"
   Then I should see "blueimp Gallery is a touch-enabled"

   # check "Crosswalk" hyperlink
   #And I should see "Crosswalk"
   #Then I verify "Crosswalk" with link "https://crosswalk-project.org/"

   # check "blueimp Gallery" hyperlink
   And I should see "blueimp Gallery"
   Then I verify "blueimp Gallery" with link "https://github.com/blueimp/Gallery"

   # check "Download" hyperlink
   And I should see "Download"
   Then I verify "Download" with link "https://github.com/blueimp/Gallery/tags"

   # check "Source Code" hyperlink
   And I should see "Source Code"
   Then I verify "Source Code" with link "https://github.com/blueimp/Gallery"

   # check "Documentation" hyperlink
   And I should see "Documentation"
   Then I verify "Documentation" with link "https://github.com/blueimp/Gallery/blob/master/README.md"

   # check "Swipe" hyperlink
   And I should see "Swipe"
   Then I verify "Swipe" with link "http://swipejs.com/"
  
   # check content
   And I should see "Carousel image gallery"
   Then I should see "Carousel video gallery"
   Then I should see "Lightbox image gallery"

   # check help content
   #And I press "Click here for how to setup wireless display."
   #Then I should see "Requirements"
   #And I should see "How to Setup Wireless Display"
   #And I should see "Use Simulated Secondary Display"

 
