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
        Cui,Jieqiong <jieqiongx.cui@intel.com>

*/

var videoFileList = new Array("3GP_h263_CIF_30FPS_507Kbps_HE-AAC_Stereo_64Kbps_60sec(4.1Mb)_BBB.3gp", "MP4_h264_CIF_15FPS_387Kbps_MP3_44.1KHz_64Kbps_60sec(3.4Mb)_BBB(hinted).mp4", "MP4_MPEG4_CIF_15FPS_387Kbps_MP3_44.1KHz_64Kbps_60sec(3Mb)_BBB(hinted).mp4");
var testTarget='';

$(document).ready(function(){
    $("#previous").addClass("ui-disabled");

    //add contentdiv style
    $("#contentdiv").css({"width":"340px","margin":"0px auto"});
    //set default video.src
    $("#MediaPlayback").attr("src", "../../res/media/meego/" + videoFileList[0]);
    document.getElementById("MediaPlayback").play();

    document.getElementById("MediaPlayback").volume = 0.6;
    $("#slider-1").hide();
    DisablePassButton();
});

function Previous() {
    testTarget=document.getElementById("MediaPlayback");
    var fileName = getFileName(testTarget.src);
    for(i=0;i<3;i++) {
        if(fileName != videoFileList[i])
            continue;
        else
            break;
    }
    if(i > 1) {
        testTarget.src="../../res/media/meego/"+videoFileList[i-1];
        testTarget.play();
        $("#next").removeClass("ui-disabled");
    }else {
        testTarget.src="../../res/media/meego/"+videoFileList[i-1];
        testTarget.play();
        $("#previous").addClass("ui-disabled");
        $("#next").removeClass("ui-disabled");
    }
}

function Next() {
    testTarget=document.getElementById("MediaPlayback");
    var fileName = getFileName(testTarget.src);
    for(i=0;i<3;i++) {
        if(fileName != videoFileList[i])
            continue;
        else
            break;
    }
    if(i < 1) {
        testTarget.src="../../res/media/meego/"+videoFileList[i+1];
        testTarget.play();
        $("#previous").removeClass("ui-disabled");
    }else {
        testTarget.src="../../res/media/meego/"+videoFileList[i+1];
        testTarget.play();
        $("#next").addClass("ui-disabled");
        $("#previous").removeClass("ui-disabled");
        EnablePassButton();
    }
}

function getFileName(o){
    var pos=o.lastIndexOf("/");
    return o.substring(pos+1);
}

function refreshData(o, newValue, handle, _popup, _handleText, element) {
    if (o.popupEnabled) {
			  _positionPopup(handle, _popup);
        _popup.html(Math.round(newValue*100)+"%" );
        document.getElementById("MediaPlayback").volume = newValue;
		}

		if (o.showValue) {
        _handleText.html(Math.round(newValue*100)+"%");
        document.getElementById("MediaPlayback").volume = newValue;
		}
}

// position the popup centered 5px above the handle
function _positionPopup(handle, _popup) {
	  var dstOffset = handle.offset();
	  _popup.offset( {
		    left: dstOffset.left + (handle.width() - _popup.width()) / 2,
		    top: dstOffset.top - _popup.outerHeight() - 5
	  });
}
