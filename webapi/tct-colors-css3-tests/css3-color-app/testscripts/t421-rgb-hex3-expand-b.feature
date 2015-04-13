Feature: css3-color
 Scenario: t421 rgb hex3 expand b
   When launch "css3-color-app"
     And I go to "colors/csswg/t421-rgb-hex3-expand-b.htm"
     And I save the page to "t421-rgb-hex3-expand-b"
     And I save the screenshot md5 as "t421-rgb-hex3-expand-b"
    Then file "t421-rgb-hex3-expand-b" of baseline and result should be the same
