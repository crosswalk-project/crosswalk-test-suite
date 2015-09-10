Feature: web-system-app
 Scenario: Crosswalk Canvas lock
  When launch "canvas"
    And I wait 3 seconds
    And I click view "className=android.widget.Button^^^description=Rotate 90deg"
    And I save the page to "rotate-90deg-lock"
    And I save the screenshot md5 as "rotate-90deg-lock"
    And I click view "className=android.widget.Button^^^description=Scale 200%"
    And I save the page to "scale-200-lock"
    And I save the screenshot md5 as "scale-200-lock"
   Then file "rotate-90deg-lock" of baseline and result should be the same
   Then file "scale-200-lock" of baseline and result should be the same
    And I turn off screen
    And I turn on screen
   Then file "rotate-90deg-lock" of baseline and result should be the same
    And I turn off screen
    And I turn on screen
   Then file "scale-200-lock" of baseline and result should be the same
