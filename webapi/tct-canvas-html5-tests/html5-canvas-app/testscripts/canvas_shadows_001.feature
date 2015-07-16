Feature: html5-canvas
 Scenario: canvas shadows
  When launch "html5-canvas-app"
   And I go to "canvas/w3c/canvas_shadows_001-manual.htm"
   And I save the page to "canvas_shadows_001"
   And I save the screenshot md5 as "canvas_shadows_001"
  Then file "canvas_shadows_001" of baseline and result should be the same
