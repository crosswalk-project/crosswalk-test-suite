Feature: css3-backgrounds
 Scenario: background intrinsic 001
   When launch "css3-backgrounds-app"
     And I go to "csswg/background-intrinsic-001-manual.htm"
     And I save the page to "background-intrinsic-001"
    Then pic "background-intrinsic-001" of baseline and result should be "100" similar if have results
