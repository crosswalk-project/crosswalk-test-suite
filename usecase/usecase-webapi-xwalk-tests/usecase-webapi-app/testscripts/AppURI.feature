Feature: Usecase WebAPI
 Scenario: Runtime & Packaging/AppURI Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/AppURI/index.html"
     And I click "getURLInfo"
     And I wait 2 seconds
    Then I should see "AppURI: file:///android_asset/www/samples/AppURI/index.html" in "uri" area
    Then I should see "Protocol: file:" in "protocol" area
    Then I should see "Origin: file://" in "origin" area
    Then I should see "Pathname: /android_asset/www/samples/AppURI/index.html" in "pathname" area
