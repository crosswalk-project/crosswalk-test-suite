Feature: Usecase WebAPI
 Scenario: Networking & Storage/RawSockets Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/RawSockets/index.html"
     And I click "connect"
    Then I should see "TCPServersocket - Connected"
     And I fill in "socketinput" with "hellow"
     And I click "send"
    Then I should see "TCPServersocket - receive - hellow"
    Then I should see "TCPServersocket - send - hellow"
    Then I should see "TCPSocket - receive - hellow"
     And I click "disconnect"
    Then I should see "TCPServersocket - Disconnected"   

