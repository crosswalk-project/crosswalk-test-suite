/*
Copyright (c) 2014 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Liu, Xin <xinx.liu@intel.com>

 */
var resume1Url, resume2Url;
var flag = false;
var resume1_flag = false , resume2_flag = false;
$(document).delegate("#main", "pageinit", function() {
  resume1Url = "TESTER-HOME-DIR/apps_rw/xwalk/applications/xwalktests.XwalkSysTests/tests/ApplicationSwitching/res/TestResume1.wgt";
  resume2Url = "TESTER-HOME-DIR/apps_rw/xwalk/applications/xwalktests.XwalkSysTests/tests/ApplicationSwitching/res/TestResume2.wgt";
  $("#install1").bind("vclick", function() {
    install(resume1Url, "install1");
    resume1_flag = true;
    if(resume1_flag && resume2_flag)
      $("#launch1").removeClass("ui-disabled");
  });

  $("#install2").bind("vclick", function() {
    install(resume2Url, "install2");
    resume2_flag = true;
    if(resume1_flag && resume2_flag)
      $("#launch1").removeClass("ui-disabled");
  });

  $("#uninstall1").bind("vclick", function() {
    uninstall1();
    $("#launch1").addClass("ui-disabled");
  });

  $("#uninstall2").bind("vclick", function() {
    uninstall2();
    $("#launch1").addClass("ui-disabled");
  });
    
  $("#launch1").bind("vclick", function() {
    launch();
    $("#uninstall1").removeClass("ui-disabled");
    $("#uninstall2").removeClass("ui-disabled");
  });
   
  try {
    tizen.package.setPackageInfoEventListener(packageEventCallback);
  } catch (e) {
    alert("Exception: " + e.message);
  }
  //packagePre();
  $("#launch1").addClass("ui-disabled");
  $("#uninstall1").addClass("ui-disabled");
  $("#uninstall2").addClass("ui-disabled");
});

var packageEventCallback = {
  oninstalled: function(packageInfo) {
    alert("The package " + packageInfo.name + " is installed");
    flag = true;
  },
  onupdated: function(packageInfo) {
    alert("The package " + packageInfo.name + " is updated");
    flag = true;
  },
  onuninstalled: function(packageId) {
    alert("The package " + packageId + " is uninstalled");
    flag = false;
  }
};

function fileURI() {
  var documentsDir;
  function onsuccess(files) {
    for (var i = 0; i < files.length; i++) {
      if(files[i].name == "TestResume1.wgt") {
        var Url1 = files[i].toURI();
        resume1Url = Url1.replace("file:///", "/");
      }
      if(files[i].name == "TestResume2.wgt") {
        var Url2 = files[i].toURI();
        resume2Url = Url2.replace("file:///", "/");
      }
    }
  }

  function onerror(error) {
    alert("The error " + error.message + " occurred when listing the files in the selected folder");
  }

  tizen.filesystem.resolve(
    'documents',
    function(dir) {
      documentsDir = dir;
      dir.listFiles(onsuccess, onerror);
    }, function(e) {
      alert("Error " + e.message);
    }, "r"
  );
}

function install(url, type) {
  var onInstallationSuccess = {
    onprogress: function(packageId, percentage) {
      console.log("On installation(" + packageId + "): progress(" + percentage + ")");
      if(type == "install1")
        document.getElementById("install1").innerHTML =  '<div data-role="button" id="install1" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>';
      if(type == "install2")
        document.getElementById("install2").innerHTML =  '<div data-role="button" id="install2" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>';
    },
    oncomplete: function(packageId) {
      console.log("Installation(" + packageId + ") Complete");
      if(type == "install1"){
        document.getElementById("install1").innerHTML =  '<div data-role="button" id="install1" style="height:40px; line-height:40px;">TestResume1 Install</div>';
        $("#install1").addClass("ui-disabled");
      }
      if(type == "install2") {
        document.getElementById("install2").innerHTML =  '<div data-role="button" id="install2" style="height:40px; line-height:40px;">TestResume2 Install</div>';
        $("#install2").addClass("ui-disabled");
      }
    }
  }

  var onError = function (err) {
    alert("Error occured on installation : " + err.name);
  }

  try {
    tizen.package.install(url, onInstallationSuccess, onError);
  } catch (e) {
    alert("Exception: " + e.name);
  }
}

function uninstall1() {
  var onUninstallationSuccess = {
    onprogress: function(packageId, percentage) {
      console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
      document.getElementById("uninstall1").innerHTML =  '<div data-role="button" id="uninstall1" style="height:40px; line-height:40px;">UnInstalling... ' + percentage + "%" + '</div>';
    },
    oncomplete: function(packageId) {
      console.log("Uninstallation(" + packageId + ") Complete");
      document.getElementById("uninstall1").innerHTML =  '<div data-role="button" id="uninstall1" style="height:40px; line-height:40px;">TestResume1 UnInstall</div>';
    }
  }

  var onError = function (err) {
    alert("Error occured on installation : " + err.name);
  }

  try {
    if(flag == false)
      alert("TestResume is already Uninstalled or not Installed");
    else
      tizen.package.uninstall("wrt3owa028", onUninstallationSuccess, onError);
  } catch (e) {
        alert("Exception: " + e.name);
  }
}

function uninstall2() {
  var onUninstallationSuccess = {
    onprogress: function(packageId, percentage) {
      console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
      document.getElementById("uninstall2").innerHTML =  '<div data-role="button" id="uninstall2" style="height:40px; line-height:40px;">UnInstalling... ' + percentage + "%" + '</div>';
    },
    oncomplete: function(packageId) {
      console.log("Uninstallation(" + packageId + ") Complete");
      document.getElementById("uninstall2").innerHTML =  '<div data-role="button" id="uninstall2" style="height:40px; line-height:40px;">TestResume2 UnInstall</div>';
    }
  }

  var onError = function (err) {
    alert("Error occured on installation : " + err.name);
  }

  try {
    if(flag == false)
      alert("TestResume is already Uninstalled or not Installed");
    else
      tizen.package.uninstall("wrt3owa029", onUninstallationSuccess, onError);
  } catch (e) {
    alert("Exception: " + e.name);
  }
}

function launch() {
  function onSuccess() {
    console.log("Application launched successfully");
  }

  function onError(err) {
    alert("launch failed : " + err.message);
  }

  try {
    tizen.application.launch("wrt3owa028.TESTS", onSuccess, onError);
  } catch (exc) {
    alert("launch exc:" + exc.message);
  }
}

function packagePre() {
  var documentsDir;
  function onsuccess(files) {
    for (var i = 0; i < files.length; i++) {
      if(files[i].name == "TestResume2") {
        documentsDir.copyTo(
          files[i].fullPath,
          "documents/TestResume2.wgt",
          true,
          function() {
            console.log("Package Precondition Success(1)!");
        });
      }
      if(files[i].name == "TestResume1") {
        documentsDir.copyTo(
          files[i].fullPath,
          "documents/TestResume1.wgt",
          true,
          function() {
            console.log("Package Precondition Success(2)!");
        });
      }
    }
    fileURI();
  }

  function onerror(error) {
    alert("The error " + error.message + " occurred when listing the files in the selected folder");
  }
  
  // FIXME(babu): https://crosswalk-project.org/jira/browse/XWALK-2564
  /*tizen.filesystem.resolve(
    'wgt-package/tests/applicationswitching/res/',
     function(dir){
       documentsDir = dir;
       dir.listFiles(onsuccess, onerror);
     }, function(e) {
       alert("Error " + e.message);
     }, "r"
  );*/
}
