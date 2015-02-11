Feature: hexgl
 Scenario: hexgl checking - MOTION
  When launch "hexgl"
   # check game title
   Then I should see title "HexGL"

   # check quality: SD', 'HD', 'ULTRA'
   And I should see "QUALITY: SD"
   And I click "s-quality"
   Then I should see "QUALITY: HD"
   And I click "s-quality"
   Then I should see "QUALITY: ULTRA"

   #check controls
   Then I should see "CONTROLS: TOUCH"
   And I click "s-controls"
   And I should see "CONTROLS: MOTION"

   #check start
   And I should see "START"
   And I click button with class "titles-button" and text "START"
   And I wait 1 seconds
   #"controls-1"->"CONTROLS: TOUCH", "controls-2"->"CONTROLS:MOTION"
   And I click "controls-2"

   Then I should see "Loading..."
   And I wait 3 seconds

#   Then I check screenshot "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_motion.png" should have 90 similarity with "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_motion_baseline.png"
#   And I wait 10 seconds
   #below time could be more longer during testing, e.g. 10min, as game is dynamic here, so set to 50%
#   Then I check screenshot "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_motion2.png" should have 50 similarity with "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_motion2_baseline.png"

 Scenario: hexgl checking - TOUCH
  When launch "hexgl"
   # check game title
   Then I should see title "HexGL"
   And I should see "QUALITY: SD"
   Then I should see "CONTROLS: TOUCH"

   #check start
   And I should see "START"
   And I click button with class "titles-button" and text "START"
   And I wait 1 seconds
   # "controls-1"->"CONTROLS: TOUCH", "controls-2"->"CONTROLS:MOTION"
   And I click "controls-1"

   Then I should see "Loading..."
   And I wait 3 seconds

#   Then I check screenshot "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_touch.png" should have 90 similarity with "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_touch_baseline.png"
#   And I wait 10 seconds
   #below time could be more longer during testing, e.g. 10min
#   Then I check screenshot "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_touch.png" should have 90 similarity with "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/hexgl_touch_baseline.png"

#   Then I get screenshot as base64

