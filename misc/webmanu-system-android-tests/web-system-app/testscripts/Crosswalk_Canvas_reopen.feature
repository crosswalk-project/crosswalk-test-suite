Feature: web-system-app
 Scenario: Crosswalk Canvas reopen
  When launch "canvas"
    And I wait 3 seconds
    And I click view "className=android.widget.Button^^^description=Rotate 90deg"
    And I wait 3 seconds
    And I save the page to "rotate-90deg"
    And I save the screenshot md5 as "rotate-90deg"
    And I click view "className=android.widget.Button^^^description=Scale 200%"
    And I wait 3 seconds
    And I save the page to "scale-200"
    And I save the screenshot md5 as "scale-200"
   Then file "rotate-90deg" of baseline and result should be the same
   Then file "scale-200" of baseline and result should be the same
    And switch to "canvas"
   Then file "scale-200" of baseline and result should be the same
