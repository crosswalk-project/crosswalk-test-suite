Feature: web-system-app
 Scenario: Crosswalk FullScreen rotation
  When launch "fullscreen"
    And I wait 2 seconds
    And I click view "description=FullScreen"
    And I wait 2 seconds
    And I take screenshot as "requestFullScreen-rotation"
    And I save the screenshot md5 as "requestFullScreen-rotation"
   Then file "requestFullScreen-rotation" of baseline and result should be the same
    And I set orientation "r"
    And I wait 2 seconds
    And I take screenshot as "requestFullScreen-rotation-r"
    And I save the screenshot md5 as "requestFullScreen-rotation-r"
   Then file "requestFullScreen-rotation-r" of baseline and result should be the same
    And I set orientation "n"
    And I click view "description=Cancel FullScreen"
    And I wait 2 seconds
    And I save the page to "cancelFullScreen-rotation"
    And I save the screenshot md5 as "cancelFullScreen-rotation"
   Then file "cancelFullScreen-rotation" of baseline and result should be the same
    And I set orientation "r"
    And I wait 2 seconds
    And I save the page to "cancelFullScreen-rotation-r"
    And I save the screenshot md5 as "cancelFullScreen-rotation-r"
   Then file "cancelFullScreen-rotation-r" of baseline and result should be the same
