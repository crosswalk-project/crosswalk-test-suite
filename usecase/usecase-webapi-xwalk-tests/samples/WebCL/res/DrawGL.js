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

var deformCamera	= null;		// camera for deformable object
var deformScene		= null;		// scene containing deformable object
var deformGeometry	= null;		// geometry for deformable object

var skyboxCamera	= null;		// camera for skybox (texture cube)
var skyboxScene		= null;		// scene for skybox (texture cube)

var useFresnel		= true;

var webgl			= null;		// WebGLRenderer object
var mouseX 			= 0;		// mouse X coord
var mouseY 			= 0;		// mouse Y coord

var NOBJ			= 200;		// number of deformable objects


// for Sphere creation
function SphereData() {
	this.radius			= 1;
	this.segmentsWidth	= 32; //64; //32;
	this.segmentsHeight	= 16; //32; //16;
}
var sphereData = new SphereData();

// for Cube creation
function CubeData() {
	this.side			= 100;
	this.segmentsLen	= 2;
	this.flipped		= false;
}
var cubeData = new CubeData();

// for Torus creation
function TorusData() {
	this.radius			= 100;
	this.tube			= 50;
	this.segmentsR		= 32;
	this.segmentsT		= 32;
}
var torusData = new TorusData();


function InitGL() {

	var container = document.createElement('div');
	document.body.appendChild(container);
	
	// initialize shader
	//
	var path = "textures/";
	var format = '.jpg';
	var urls = [
			path + 'posx' + format, path + 'negx' + format,
			path + 'posy' + format, path + 'negy' + format,
			path + 'posz' + format, path + 'negz' + format
		];

	var textureCube = THREE.ImageUtils.loadTextureCube( urls );

	var fresnelShader = THREE.ShaderUtils.lib["fresnel"];
	var fresnelUniforms = THREE.UniformsUtils.clone( fresnelShader.uniforms );

	fresnelUniforms["tCube"].texture = textureCube;
	fresnelUniforms["mFresnelBias"].value = 0.2
	//fresnelUniforms["mFresnelPower"].value = 3.0;

	var fresnelParameters = { fragmentShader: fresnelShader.fragmentShader, vertexShader: fresnelShader.vertexShader, uniforms: fresnelUniforms };
	var fresnelMaterial = new THREE.MeshShaderMaterial( fresnelParameters );

	var basicShader = THREE.ShaderUtils.lib["basic"];
	var basicMaterial = new THREE.MeshBasicMaterial( { color: 0xffffff, envMap: textureCube } );

	// initialize sphere scene and camera
	//
	deformCamera = new THREE.Camera( 60, WINW / WINH, 1, 100000 );
	deformCamera.position.z = 3200;

	deformScene = new THREE.Scene();
	deformGeometry = new THREE.Sphere( sphereData.radius, sphereData.segmentsWidth, sphereData.segmentsHeight );
	//deformGeometry = new THREE.Cube( cubeData.side, cubeData.side, cubeData.side, cubeData.segmentsLen, cubeData.segmentsLen, cubeData.segmentsLen, basicMaterial, cubeData.flipped, null);
	//deformGeometry = new THREE.Torus( torusData.radius, torusData.tube, torusData.segmentsR, torusData.segmentsT );
	
	/*for(var i=0; i<NOBJ; i++) {
		var deformMesh = null;
		
		if(i % 2 == 0)
			deformMesh = new THREE.Mesh( deformGeometry, fresnelMaterial );
		else
			deformMesh = new THREE.Mesh( deformGeometry, basicMaterial );

		deformMesh.position.x = 15000 * RANDM1TO1();
		deformMesh.position.y = 5000 * RANDM1TO1(); 
		deformMesh.position.z = 5000 * RANDM1TO1();
		deformMesh.scale.x = deformMesh.scale.y = deformMesh.scale.z = ((6 * RAND0TO1()) + 1) * 100;
		deformScene.addObject( deformMesh );
	}*/
	
	{
		var deformMesh = null;

		deformMesh = new THREE.Mesh( deformGeometry, fresnelMaterial );
		deformMesh.position.x = -1000;
		deformMesh.position.y = 0; 
		deformMesh.position.z = 0;
		deformMesh.scale.x = deformMesh.scale.y = deformMesh.scale.z = 500;
		deformScene.addObject( deformMesh );
		
		deformMesh = new THREE.Mesh( deformGeometry, basicMaterial );
		deformMesh.position.x = 1000;
		deformMesh.position.y = 0; 
		deformMesh.position.z = 0;
		deformMesh.scale.x = deformMesh.scale.y = deformMesh.scale.z = 500;
		deformScene.addObject( deformMesh );
	}
	
	// initialize background scene and camera
	//	
	skyboxCamera = new THREE.Camera( 60, WINW / WINH, 1, 100000 );
	skyboxScene = new THREE.Scene();
	THREE.SceneUtils.addPanoramaCubeWebGL( skyboxScene, 100000, textureCube );

	// initialize WebGL renderer
	//
	webgl = new THREE.WebGLRenderer();
	webgl.setSize( WINW, WINH );
	webgl.autoClear = false;
	container.appendChild( webgl.domElement );
	
	//webgl.domElement.addEventListener( 'mousemove', onDocumentMouseMove, false );
	document.addEventListener( 'mousemove', onDocumentMouseMove, false );
	
	return webgl.context;
}

function onDocumentMouseMove(event) {

	mouseX = ( event.clientX - (WINW / 2) ) * 15;
	mouseY = ( event.clientY - (WINH / 2) ) * 15;
}

function ResetGeometry(gl) {

    if(!userData.glLoaded) return;
    
    gl.bindBuffer(gl.ARRAY_BUFFER, userData.curPosVBO);
    gl.bufferSubData(gl.ARRAY_BUFFER, 0, userData.initPos);
    
    gl.bindBuffer(gl.ARRAY_BUFFER, userData.curNorVBO);
    gl.bufferSubData(gl.ARRAY_BUFFER, 0, userData.initNor);
}

function DrawGL(gl) {

    if(gl === null) return;

	// obtain buffers from deformGeometry
	//
	if(deformGeometry.geometryGroups && !userData.glLoaded) {

		handle = deformGeometry.geometryGroups.undefined_0;

		userData.nVertices		= handle.vertices;
        userData.initPos        = new Float32Array(handle.__vertexArray);
        userData.initNor        = new Float32Array(handle.__normalArray);
		userData.curPos         = handle.__vertexArray;		
        userData.curNor         = handle.__normalArray;
		
		userData.curPosVBO      = handle.__webglVertexBuffer;
		userData.curNorVBO      = handle.__webglNormalBuffer;
		userData.glLoaded		= true;
		
		console.log("nVertices:            " + handle.vertices);
		console.log("3 * nVertices:        " + (3*handle.vertices));
		console.log("__vertexArray.length: " + handle.__vertexArray.length);		
	}
	 
	// if not sharing buffers with WebCL then need to update VBOs
	//
	if(userData.glLoaded) {
		if((userData.clSimMode === CL_SIM && !GLCL_SHARE_MODE) || userData.clSimMode === JS_SIM) {

			gl.bindBuffer(gl.ARRAY_BUFFER, userData.curPosVBO);
			gl.bufferSubData(gl.ARRAY_BUFFER, 0, userData.curPos);

			gl.bindBuffer(gl.ARRAY_BUFFER, userData.curNorVBO);
			gl.bufferSubData(gl.ARRAY_BUFFER, 0, userData.curNor);
		}
    }

	deformCamera.position.x += (   mouseX - deformCamera.position.x ) * .1;
	deformCamera.position.y += ( - mouseY - deformCamera.position.y ) * .1;

	skyboxCamera.target.position.x = - deformCamera.position.x;
	skyboxCamera.target.position.y = - deformCamera.position.y;
	skyboxCamera.target.position.z = - deformCamera.position.z;

	webgl.clear();
	webgl.render( skyboxScene, skyboxCamera );
	webgl.render( deformScene, deformCamera );
}