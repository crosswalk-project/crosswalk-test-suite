Feature: wrt-internetstd-app
 Scenario: Crosswalk WebApp Scheme App
  When launch "web_scheme_app"
    And I click view "className=android.widget.Button^^^description=Get Protocol"
   Then I should see "protocol: app:" in "testDiv" area
    And I click view "className=android.widget.Button^^^description=Get Href"
   Then I should see text in "testDiv" area startswith "href: app:"
   Then I should see text in "testDiv" area endswith "index.html"
    And I click view "className=android.widget.Button^^^description=Get Origin"
   Then I should see "origin: app://" in "testDiv" area
