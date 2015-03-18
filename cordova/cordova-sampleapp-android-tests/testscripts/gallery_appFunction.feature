Feature: gallery
 Scenario: gallery checking
  When I launch "gallery" with "com.example.gallery" and ".gallery"
   # check home page
   Then I should see "blueimp Gallery is a touch-enabled"

   # check "blueimp Gallery" hyperlink
   Then I should see "blueimp Gallery"
   Then I verify "blueimp Gallery" with link "https://github.com/blueimp/Gallery"

   # check "Download" hyperlink
   Then I should see "Download"
   Then I verify "Download" with link "https://github.com/blueimp/Gallery/tags"

   # check "Source Code" hyperlink
   Then I should see "Source Code"
   Then I verify "Source Code" with link "https://github.com/blueimp/Gallery"

   # check "Documentation" hyperlink
   Then I should see "Documentation"
   Then I verify "Documentation" with link "https://github.com/blueimp/Gallery/blob/master/README.md"

   # check "Swipe" hyperlink
   Then I should see "Swipe"
   Then I verify "Swipe" with link "http://swipejs.com/"
  
   # check content
   Then I should see "Carousel image gallery"
   Then I should see "Carousel video gallery"
   Then I should see "Lightbox image gallery"
