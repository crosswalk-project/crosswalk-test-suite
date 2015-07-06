Feature: simd
 Scenario: simd checking
  When launch "simd"
   # need wait sometimes to trigger the home page 
   And I wait 8 seconds  
   Then I should see "Start"
   Then I should see "Stop"
   Then I should see "Turn On SIMD"
   Then I should see "SIMD:Off WW:1"
   And I should see "FPS: 0.0"
   
   And I press "Start"
   And I wait 5 seconds
   Then I check "fps" is 1.5 times after click "simd" for 10 seconds
   And I press "Stop"

