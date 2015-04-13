Feature: css3-backgrounds
 Scenario: background intrinsic 001
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-intrinsic-001-manual.htm"
     And I save the page to "background-intrinsic-001"
     And I save the screenshot md5 as "background-intrinsic-001"
    Then file "background-intrinsic-001" of baseline and result should be the same
