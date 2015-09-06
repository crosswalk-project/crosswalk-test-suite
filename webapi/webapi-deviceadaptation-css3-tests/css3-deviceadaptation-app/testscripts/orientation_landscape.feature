Feature: css3-deviceadaptation
 Scenario: orientation landscape
   When launch "css3-deviceadaptation-app"
     And I go to "deviceadaptation/orientation_landscape-manual.html"
     And I set orientation "l"
     And I save the page to "orientation_landscape"
     And I save the screenshot md5 as "orientation_landscape"
     And I set orientation "r"
    Then file "orientation_landscape" of baseline and result should be the same
