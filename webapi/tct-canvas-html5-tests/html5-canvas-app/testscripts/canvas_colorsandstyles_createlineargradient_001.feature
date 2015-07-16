Feature: html5-canvas
 Scenario: canvas colorsandstyles createlineargradient
  When launch "html5-canvas-app"
   And I go to "canvas/w3c/canvas_colorsandstyles_createlineargradient_001-manual.htm"
   And I save the page to "canvas_colorsandstyles_createlineargradient_001"
   And I save the screenshot md5 as "canvas_colorsandstyles_createlineargradient_001"
  Then file "canvas_colorsandstyles_createlineargradient_001" of baseline and result should be the same
