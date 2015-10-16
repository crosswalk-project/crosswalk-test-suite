Feature: web-system-app
 Scenario: Crosswalk FullScreen volume
  When launch "fullscreen"
    And I wait 2 seconds
    And I click view "description=FullScreen"
    And I wait 2 seconds
    And I take screenshot as "requestFullScreen-volume"
    And I save the screenshot md5 as "requestFullScreen-volume"
   Then file "requestFullScreen-volume" of baseline and result should be the same
    And I press "volume_up" hardware key
    And I wait 2 seconds
   Then file "requestFullScreen-volume" of baseline and result should be the same
    And I press "volume_down" hardware key
    And I wait 2 seconds
   Then file "requestFullScreen-volume" of baseline and result should be the same
    And I click view "description=Cancel FullScreen"
    And I wait 2 seconds
    And I save the page to "cancelFullScreen-volume"
    And I save the screenshot md5 as "cancelFullScreen-volume"
   Then file "cancelFullScreen-volume" of baseline and result should be the same
    And I press "volume_up" hardware key
    And I wait 2 seconds
   Then file "cancelFullScreen-volume" of baseline and result should be the same
    And I press "volume_down" hardware key
    And I wait 2 seconds
   Then file "cancelFullScreen-volume" of baseline and result should be the same
