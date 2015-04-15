/*
* Copyright (C) 2011 Samsung Electronics Corporation. All rights reserved.
* 
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided the following conditions
* are met:
* 
* 1.  Redistributions of source code must retain the above copyright
*     notice, this list of conditions and the following disclaimer.
* 
* 2.  Redistributions in binary form must reproduce the above copyright
*     notice, this list of conditions and the following disclaimer in the
*     documentation and/or other materials provided with the distribution.
* 
* THIS SOFTWARE IS PROVIDED BY SAMSUNG ELECTRONICS CORPORATION AND ITS
* CONTRIBUTORS "AS IS", AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING
* BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
* FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL SAMSUNG
* ELECTRONICS CORPORATION OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
* INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES(INCLUDING
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
* DATA, OR PROFITS, OR BUSINESS INTERRUPTION), HOWEVER CAUSED AND ON ANY THEORY
* OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT(INCLUDING
* NEGLIGENCE OR OTHERWISE ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
* EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
 
function FpsSampler(aSamplePeriod, aDivId) {

    this.samplePeriod = aSamplePeriod;
    this.fpsDivId = aDivId;
    this.fpsDiv = null;
    this.fps = 0;
    this.frameCount = 0;
    this.tStart = null;
    
    this.markFrame = function() {
    	if(this.frameCount == 0) {
			this.tStart = new Date().valueOf();
        }

        if(this.frameCount === this.samplePeriod) {
            var tNow = new Date().valueOf();    
            var delta = Math.max(1, tNow - this.tStart);
            this.fps = Math.round((this.samplePeriod * 1000) / delta);
            this.frameCount = 0;
        }
        else {
            this.frameCount++;
        }
    };
       
    this.display = function() {
    	if(this.fpsDiv === null) this.fpsDiv = document.getElementById(this.fpsDivId);
    	this.fpsDiv.firstChild.nodeValue = this.fps;
    };
}

function MSecSampler(aSamplePeriod, aDivId) {

    this.samplePeriod = aSamplePeriod;
    this.msDivId = aDivId;
    this.msDiv = null;
    this.ms = 0;
    this.msAccumulator = 0;
    this.frameCount = 0;
    this.tStart = null;
    this.isAccumulating = false;    // allow calling endFrame before startFrame
    
    this.startFrame = function() {
        if(this.isAccumulating) return;
        this.isAccumulating = true;
        
    	if(this.frameCount % this.samplePeriod == 0) {
            this.msAccumulator = 0;
    		this.frameCount = 0;
    	}
		this.tStart = new Date().valueOf();
    };
    
    this.endFrame = function() {
        if(!this.isAccumulating) return;
        this.isAccumulating = false;
        
    	var tNow = new Date().valueOf();	
        this.msAccumulator += (tNow - this.tStart);
		this.frameCount++;
        if(this.frameCount % this.samplePeriod == 0) {
            this.ms = Math.round(this.msAccumulator / this.frameCount);
            this.frameCount = 0;
        }
    };
    
    this.display = function() {
    	if(this.msDiv === null) this.msDiv = document.getElementById(this.msDivId);
    	this.msDiv.firstChild.nodeValue = this.ms + " ms";
    };
}
