Feature: Doit_im_Link
 Scenario: Doit_im_Link
  When launch "doitim"
   And I wait 5 seconds
   And I click the link "Help"
  Then I should see "FAQ" in 5 seconds
