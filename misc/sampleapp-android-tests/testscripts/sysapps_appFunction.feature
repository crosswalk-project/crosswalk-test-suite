Feature: sysapp
 Scenario: sysapp checking
  When launch "sysapps"
   # check home page 's top nav
   Then I should see "Device Capabilities demo"
   And I should see "CPU"
   And I should see "Memory"
   And I should see "Storage"
   And I should see "Display"
   And I should see "Codec"

   # check "CPU Monitor" data
   And I wait 5 seconds
   Then I should see "CPU Monitor"
   # to check Canvas output, check x/y axis, but data is hard to check here
   # data is diff for different devices
   #And I should see "100"
   And I should see "0"
   And I should see "The CPU of this device is"
   And I should see "processor"

   # check Memory Monitor data
   Then I should see "Memory Monitor"
   And I should see "Used memory:"
   And I should see "Total memory:"

   # check data by screenshot
#   Then I check screenshot "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/sysapp_cpumem.png" should have 90 similarity with "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/sysapp_cpumem_baseline.png"

   # check Storage State
   Then I should see "Storage State"
   And I should see "storage device"
   And I should see "Internal"
   And I should see "sdcard"
   And I should see "and its capacity is"

   # check Display State
   Then I should see "Display State"
   And I should see "display device"
   And I should see "an auxiliary" 

   # check audio/video upload file
   Then I should see "Check Audio/Video uploaded file"
   And I should see "Please select an audio or video file"
   And I click "file-to-upload"
   # here could consider more combination of native app operation here, and cover positive/negative usage
   #And I go back
   #And I click "Upload"

   # check data by screenshot
#   Then I check screenshot "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/sysapp_uploadfile.png" should have 90 similarity with "/home/cici/webdriver/auto/wrt-sampleapp-android-tests/testscripts/resource/sysapp_uploadfile_baseline.png"


