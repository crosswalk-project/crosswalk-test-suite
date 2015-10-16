Feature: web-system-app
 Scenario: Crosswalk FullScreen lock
  When launch "fullscreen"
    And I wait 2 seconds
    And I click view "description=FullScreen"
    And I wait 2 seconds
    And I take screenshot as "requestFullScreen-lock"
    And I save the screenshot md5 as "requestFullScreen-lock"
   Then file "requestFullScreen-lock" of baseline and result should be the same
    And I turn off screen
    And I turn on screen
   Then file "requestFullScreen-lock" of baseline and result should be the same
    And I click view "description=Cancel FullScreen"
    And I wait 2 seconds
    And I save the page to "cancelFullScreen-lock"
    And I save the screenshot md5 as "cancelFullScreen-lock"
   Then file "cancelFullScreen-lock" of baseline and result should be the same
    And I turn off screen
    And I turn on screen
   Then file "cancelFullScreen-lock" of baseline and result should be the same
