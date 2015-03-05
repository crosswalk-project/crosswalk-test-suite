Feature: simd
 Scenario: simd checking
  When launch "simd"
   # need wait sometimes to trigger the home page 
   And I wait 8 seconds  
   Then I should see "START"
   Then I should see "+ SIMD"
   Then I should see "SIMD: Off"
   And I should see "FPS: 0.0"
   
   And I press "START"
   And I wait 5 seconds
   Then I check "fps" is 1.8 times after click "simd" for 10 seconds
   And I press "STOP"

