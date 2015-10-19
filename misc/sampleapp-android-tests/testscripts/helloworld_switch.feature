Feature: helloworld
 Scenario: helloworld orientation
  When launch "helloworld"
   Then I should see view "description=Hello, world!"
    And I press "home" hardware key
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=Hello World" to object "hello_app"
    And I click saved object "hello_app"
   Then I should see view "description=Hello, world!"
