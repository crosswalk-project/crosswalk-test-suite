Feature: Usecase WebAPI
 Scenario: Experimental API/WiFiDirect Test
    When device has WiFi Direct capability and WiFi is enabled
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/WifiDirect/index.html"
    Then I should see nearby WifiDirect devices that are available for connecting
     And I click on one of the devices with label "available"
    Then I should see label changed from "available" to "invited"
    Then I should see button labeled "Cancel invite"
    When the device being connected to doesn't require further authorization,
     Or on the other device, "Invitation to connect" is accepted:
     e.g. printer another Android phone running the same test or
     e.g. another Android phone running Settings->WiFi->Advanced->WiFi Direct page.
    Then I should see label changed from "invited" to "connected"
    Then I should see button labeled "Cancel invite" changed to "Disconnect"
    Then I should text under State: "connected as client - server IP is..."
     Or I should see text under state: "connected as group server"
    Then I click "Disconnect"
    Then "State:" displays "disconnected" and "available"
