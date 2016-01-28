Feature: hexgl
 Scenario: hexgl checking - MOTION
  When launch "hexgl"
   # check game title
   Then I should see title "HexGL by BKcore"

   #check controls
   Then I should see "Controls: TOUCH"
   And I click "s-controlType"
   And I should see "Controls: LEAP MOTION CONTROLLER"

   # check quality
   And I should see "Quality: VERY HIGH"
   And I click "s-quality"
   Then I should see "Quality: LOW"

   # check hud
   And I should see "HUD: ON"
   And I click "s-hud"
   And I should see "HUD: OFF"

   #check start
   And I should see "Start"
   And I click "start"
   And I wait 3 seconds
   And I click "ctrl-help"
   And I wait 10 seconds
   Then I should see "Waiting for the Leap Motion Controller server..."
   And I wait 3 seconds

 Scenario: hexgl checking - TOUCH
  When launch "hexgl"
   # check game title
   Then I should see title "HexGL by BKcore"
   Then I should see "Controls: TOUCH"
   And I should see "Quality: VERY HIGH"
   And I click "s-quality"

   #check start
   And I should see "Start"
   And I click "start"
   And I wait 3 seconds
   Then I should see "Click/Touch to continue"
   And I click "ctrl-help"
   And I wait 10 seconds
   Then I should not see "Click/Touch to continue"
   And I wait 3 seconds


