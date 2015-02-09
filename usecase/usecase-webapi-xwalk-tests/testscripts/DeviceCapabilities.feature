Feature: Usecase WebAPI
 Scenario: Experimental API/DeviceCapabilities Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/DeviceCapabilities/index.html"
     And I wait 1 seconds
    Then I verify value in "NumOfProcessors" is "int" type
    Then I verify value in "ArchName" is "string" type
    Then I verify value in "Load" is "float" type
    Then I verify value in "Capacity" is "int" type
    Then I verify value in "AvailCapacity" is "int" type
    Then I verify value in "StorageUnit number" is "int" type
    Then I verify value in "StorageUnit id" is "int" type
    Then I verify value in "StorageUnit name" is "string" type
    Then I verify value in "StorageUnit type" is "string" type
    Then I verify value in "StorageUnit capacity" is "int" type
    Then I verify value in "DisplayUnit number" is "int" type
    Then I verify value in "DisplayUnit id" is "int" type
    Then I verify value in "DisplayUnit name" is "string" type
    Then I verify value in "DisplayUnit primary" is "boolean" type
    Then I verify value in "DisplayUnit external" is "boolean" type
    Then I verify value in "DisplayUnit deviceXDPI" is "int" type
    Then I verify value in "DisplayUnit deviceYDPI" is "int" type
    Then I verify value in "DisplayUnit availWidth" is "int" type
    Then I verify value in "DisplayUnit availHeight" is "int" type
    Then I verify value in "DisplayUnit width" is "int" type
    Then I verify value in "DisplayUnit height" is "int" type
    Then I verify value in "DisplayUnit colorDepth" is "int" type
    Then I verify value in "DisplayUnit pixelDepth" is "int" type
    Then I verify value in "AudioCodec format" is "string" type
    Then I verify value in "VideoCodec format" is "string" type
    Then I verify value in "VideoCodec hwAccel" is "boolean" type
    Then I verify value in "VideoCodec encode" is "boolean" type
























