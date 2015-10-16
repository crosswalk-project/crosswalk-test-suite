Feature: web-system-app
 Scenario: Crosswalk FullScreen sleep
  When launch "fullscreen"
    And I wait 2 seconds
    And I click view "description=FullScreen"
    And I wait 2 seconds
    And I take screenshot as "requestFullScreen-sleep"
    And I save the screenshot md5 as "requestFullScreen-sleep"
   Then file "requestFullScreen-sleep" of baseline and result should be the same
    And I turn off screen
    And I wait for 15 seconds
    And I turn on screen
   Then file "requestFullScreen-sleep" of baseline and result should be the same
    And I click view "description=Cancel FullScreen"
    And I wait 2 seconds
    And I save the page to "cancelFullScreen-sleep"
    And I save the screenshot md5 as "cancelFullScreen-sleep"
   Then file "cancelFullScreen-sleep" of baseline and result should be the same
    And I turn off screen
    And I wait for 15 seconds
    And I turn on screen
   Then file "cancelFullScreen-sleep" of baseline and result should be the same
