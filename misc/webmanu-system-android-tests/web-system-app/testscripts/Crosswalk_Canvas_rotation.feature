Feature: web-system-app
 Scenario: Crosswalk Canvas rotation 
  When launch "canvas"
    And I wait for 2 seconds
    And I click view "className=android.widget.Button^^^description=Rotate 90deg"
    And I save the page to "rotate-90deg-rotation"
    And I save the screenshot md5 as "rotate-90deg-rotation"
   Then file "rotate-90deg-rotation" of baseline and result should be the same
    And I set orientation "r"
    And I wait 2 seconds
    And I save the page to "rotate-90deg-rotation-r"
    And I save the screenshot md5 as "rotate-90deg-rotation-r"
   Then file "rotate-90deg-rotation-r" of baseline and result should be the same
    And I set orientation "n"
    And I click view "className=android.widget.Button^^^description=Scale 200%"
    And I wait 2 seconds
    And I save the page to "scale-200-rotation"
    And I save the screenshot md5 as "scale-200-rotation"
   Then file "scale-200-rotation" of baseline and result should be the same
    And I set orientation "r"
    And I wait 2 seconds
    And I save the page to "scale-200-rotation-r"
    And I save the screenshot md5 as "scale-200-rotation-r"
   Then file "scale-200-rotation-r" of baseline and result should be the same
