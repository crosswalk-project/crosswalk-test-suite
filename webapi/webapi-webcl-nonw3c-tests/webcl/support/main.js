function initCL() {
  var cl;
  try {
    if(typeof(webcl) == "undefined") {
      document.writeln("webcl property is yet to be defined in window");
      return null;
    }

    cl = window.webcl;
    if(cl == null) {
      document.writeln("Failed to fetch a webcl instance.");
    }
  
  } catch(ex) {
    document.writeln("Error message: " + ex.message);
  }

  return cl;
}

function getPlatforms() {
  var platforms;
  try {
    var cl = initCL();
    if(cl == null) {
      return null;
    }

    var platforms = cl.getPlatforms();
    if(platforms == null || platforms.length == 0) {
      document.writeln("No platforms available");
      return null;
    }

  } catch(ex) {
    document.writeln("Error message: " + ex.message);
  }

  return platforms;
}

function getDevicesWithExtensionEnabled(extensionName) {
  var devices;
  try {
    var platforms = getPlatforms();
    if(platforms == null) {
      return null;
    }

    platforms.forEach(function(platform) {
      var allDevices = platform.getDevices();
      if(allDevices.length > 0) {
        allDevices.forEach(function(device) {
          var isSuported = device.enableExtension(extensionName);
          if(isSuported) {
            devices.push(device);
          }
        });
      }
    });
  } catch(ex) {
    document.writeln("Error message: " + ex.message);
  }

  return devices;
}

function testResult(data, expect, loopNum, msg) {
  test(function() {
    var count = 0;
    for(var i=0; i< loopNum; i++) {
      count ++;
    }
    assert_true(count == expect, msg);
  });
}
