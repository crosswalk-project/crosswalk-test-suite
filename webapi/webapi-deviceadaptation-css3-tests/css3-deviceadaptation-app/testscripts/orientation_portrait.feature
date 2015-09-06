Feature: css3-deviceadaptation
 Scenario: orientation portrait
   When launch "css3-deviceadaptation-app"
     And I go to "deviceadaptation/orientation_portrait-manual.html"
     And I set orientation "l"
     And I save the page to "orientation_portrait"
     And I save the screenshot md5 as "orientation_portrait"
     And I set orientation "r"
    Then file "orientation_portrait" of baseline and result should be the same
