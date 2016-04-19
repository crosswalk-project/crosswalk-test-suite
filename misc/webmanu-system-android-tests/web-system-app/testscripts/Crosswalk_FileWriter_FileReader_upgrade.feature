Feature: web-system-app
 Scenario: Crosswalk FileWriter FileReader upgrade
  When launch "filereader"
    And I wait for 2 seconds
    And I click view "description=select file"
    And I click view "text=File Manager"
   Then I should see view "text=filereadertest.docx"
    And I click view "text=filereadertest.docx"
    And I wait for 2 seconds
   Then I should see "Pass" in "filePreview" area
    And I click view "description=write file"
   Then I should see "This new content comes from FileWriter" in "filePreview" area
    And upgrade "../../filereader_upgrade.apk"
    And I launch "filereader" with "org.xwalk.filereader" and "FilereaderActivity" on android
    And I wait for 2 seconds
    And I click view "description=read written file"
    And I wait for 2 seconds
   Then I expect the content "WRITTEN FILE:This new content comes from FileWriter" in the dumped xml
