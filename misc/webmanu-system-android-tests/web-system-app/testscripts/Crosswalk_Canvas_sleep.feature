Feature: web-system-app
 Scenario: Crosswalk Canvas sleep
  When launch "canvas"
    And I wait for 3 seconds
    And I click view "className=android.widget.Button^^^description=Rotate 90deg"
    And I save the page to "rotate-90deg-sleep"
    And I save the screenshot md5 as "rotate-90deg-sleep"
   Then file "rotate-90deg-sleep" of baseline and result should be the same
    And I turn off screen
    And I wait for 15 seconds
    And I turn on screen
   Then file "rotate-90deg-sleep" of baseline and result should be the same
    And I click view "className=android.widget.Button^^^description=Scale 200%"
    And I save the page to "scale-200-sleep"
    And I save the screenshot md5 as "scale-200-sleep"
   Then file "scale-200-sleep" of baseline and result should be the same
    And I turn off screen
    And I wait for 15 seconds
    And I turn on screen
   Then file "scale-200-sleep" of baseline and result should be the same
