Feature: api tests
    Scenario: api test 001
        When launch "haha"
         And I go to "http://www.google.com"
         And I wait for 1 seconds
