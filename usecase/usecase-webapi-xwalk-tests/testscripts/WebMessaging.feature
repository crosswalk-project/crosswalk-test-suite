Feature: Usecase WebAPI
 Scenario: Networking & Storage/WebMessaging Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/WebMessaging/index.html"
     And I fill in "sendcontent" with "hi"
     And I press "b1"
     And I go to frame "messageframe"
    Then I should see "The received message : hi"
     And I go out of frame
     And I fill in "sendcontent" with "hellow"
     And I press "b1"
     And I go to frame "messageframe"
    Then I should see "The received message : hellow" 
