Feature: Usecase WebAPI
 Scenario: Multimedia & Graphics/WebRTC Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebRTC/index.html"
     And I click "startbutton"
    Then I should see "pc1 and pc2 are connected successfully, and can send message now!" in 5 seconds
     And I fill in "pc1_input" with "Hello! Nice to meet you!"
     And I click "pc1_send"
    Then I should see "Received message: Hello! Nice to meet you!" in 5 seconds
     And I click "stopbutton"
    Then I should see "The connection is closed, stop send message now!" in 5 seconds
