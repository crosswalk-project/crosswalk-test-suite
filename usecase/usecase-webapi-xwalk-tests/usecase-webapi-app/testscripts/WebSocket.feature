Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebSocket Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebSocket/index.html"
     And I click "connect"
    Then I should see "Connecting......"
    Then I should see "Successfully connect to WebSocket server" in 5 seconds
     And I fill in "socketinput" with "hellow"
     And I click "send"
    Then I should see "WebSocket - receive - hellow"
     And I click "disconnect"
    Then I should see "WebSocket connection is closed"   

