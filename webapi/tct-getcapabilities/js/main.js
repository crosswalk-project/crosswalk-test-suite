/*
Copyright (c) 2013 Intel Corporation.

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
        Jing Tao <taox.jing@intel.com>
        Wang, Jing J <jing.j.wang@intel.com>

*/

var buildinfoDone = false;
var capabilityDone = false;

function getInfo(){
    function onerror(e){
        console.log(e.message);
    }
    tizen.filesystem.resolve('documents/tct',
        function (dir) {
            getCap(dir);
            getBuildInfo(dir);
        },function (e) {
            console.log(e.message);
            if (e.name == "NotFoundError"){
                tizen.filesystem.resolve('documents', function(dir){
                    console.log("create");
                    var tctdir = dir.createDirectory("tct");
                    getCap(tctdir);
                    getBuildInfo(tctdir);
                }, onerror, "rw");
            }
        },"rw");
}

function closeWindow() {
    window.open('', '_self', '');
    window.close();
}

function exitTest(){
    try {
        var app = tizen.application.getCurrentApplication();
        app.exit();
    } catch(err) {
        closeWindow();
    }
}

function getCap(dir) {
    var xmlResult = "";

    if (tizen.systeminfo == 'undefined') {
        xmlResult = "<div>tizen.systeminfo is undefined</div>";
    } else {
        xmlResult = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n";
        xmlResult += "<capabilities xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n";
        xmlResult += "xsi:noNamespaceSchemaLocation=\"capability.xsd\">\r\n";

        var caps = tizen.systeminfo.getCapabilities();
        for (x in caps) {
            if (typeof(caps[x]) == "boolean")
                xmlResult += "    <capability name=\"" + x + "\" support=\"" + caps[x] + "\" type=\"boolean\"/>\r\n";
            else {
                if (typeof(caps[x]) == "number")
                    xmlResult += "    <capability name=\"" + x + "\" support=\"true\" type=\"Integer\">\r\n";
                else if (typeof(caps[x]) == "string")
                    xmlResult += "    <capability name=\"" + x + "\" support=\"true\" type=\"String\">\r\n";
                else
                    xmlResult += "    <capability name=\"" + x + "\" support=\"true\" type=\"" + typeof(caps[x]) + "\">\r\n";
                xmlResult += "        <value>" + caps[x] + "</value>\r\n";
                xmlResult += "    </capability>\r\n";
            }
        }
        xmlResult += "</capabilities>";
    }

    console.log("capability.xml");

    writeFile(dir,"capability.xml", xmlResult);
}

function getBuildInfo(dir) {
    var xmlResult = "";

    function onSuccessCallback(build) {
        xmlResult = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n";
        xmlResult += "<buildinfos xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n";
        xmlResult += "xsi:noNamespaceSchemaLocation=\"buildinfo.xsd\">\r\n";

        xmlResult += "    <buildinfo name=\"model\" support=\"true\" type=\"String\">\r\n";
        xmlResult += "        <value>" + build.model + "</value>\r\n";
        xmlResult += "    </buildinfo>\r\n";

        xmlResult += "    <buildinfo name=\"manufacturer\" support=\"true\" type=\"String\">\r\n";
        xmlResult += "        <value>" + build.manufacturer + "</value>\r\n";
        xmlResult += "    </buildinfo>\r\n";

        xmlResult += "    <buildinfo name=\"buildVersion\" support=\"true\" type=\"String\">\r\n";
        xmlResult += "        <value>" + build.buildVersion + "</value>\r\n";
        xmlResult += "    </buildinfo>\r\n";

        xmlResult += "</buildinfos>";

        document.getElementById("log").innerHTML = xmlResult;
        writeFile(dir,"buildinfo.xml", xmlResult);
    }

    function onErrorCallback(error) {
        console.log("An error occurred " + error.message);
    }

    tizen.systeminfo.getPropertyValue("BUILD", onSuccessCallback, onErrorCallback);
}

function writeFile(dir,filename,content){
    errorCallback = function(error) {
        alert("openStream fail: "+error);
    };
    dir.deleteFile(dir.fullPath+ "/" + filename);
    file = dir.createFile(filename);
    file.openStream("rw", function(fs){
        fs.write(content);
        fs.close();

        if (filename == "capability.xml") capabilityDone = true;
        else if (filename == "buildinfo.xml") buildinfoDone = true;

        if (capabilityDone && buildinfoDone) exitTest();

    }, errorCallback, "UTF-8");
}
