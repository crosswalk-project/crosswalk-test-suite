Feature: web-system-app
 Scenario: Crosswalk FullScreen reopen
  When launch "fullscreen"
    And I wait 2 seconds
    And I click view "description=FullScreen"
    And I wait 2 seconds
    And I take screenshot as "requestFullScreen-reopen"
    And I save the screenshot md5 as "requestFullScreen-reopen"
   Then file "requestFullScreen-reopen" of baseline and result should be the same
    And switch to "fullscreen"
    And I wait 2 seconds
    And I click view "description=Cancel FullScreen"
    And I wait 2 seconds
    And I save the page to "cancelFullScreen-reopen"
    And I save the screenshot md5 as "cancelFullScreen-reopen"
   Then file "cancelFullScreen-reopen" of baseline and result should be the same
    And switch to "fullscreen"
   Then file "cancelFullScreen-reopen" of baseline and result should be the same
