Feature: stability-android
 Scenario: Download_File_LongTime
  When launch "downloadtest"
    And I wait 15 seconds
    And repeat to download resources from link "tizen-ivi_20150117.1_ivi-efi-x86_64-sdb.raw.bz2" for 1800 seconds
    And I click the link "Parent Directory"
  Then I should see "ivi-efi-x86_64/"
