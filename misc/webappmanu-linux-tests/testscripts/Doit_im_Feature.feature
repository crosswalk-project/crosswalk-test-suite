Feature: Doit_im_Feature
 Scenario: Doit_im_Feature
  When launch "doitim"
   And I wait 5 seconds
   And I click the link "Download"
   And I click "download_android_intl"
  Then I should see a pop-up dialog
