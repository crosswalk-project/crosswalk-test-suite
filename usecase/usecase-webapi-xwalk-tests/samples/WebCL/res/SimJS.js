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

var SQRT_FLOPS	= 5;
var POW_FLOPS	= 10;
var nFlops 		= 0;

var P_MASK = 255;
var P_SIZE = 256;
var P = [151,160,137,91,90,15,
  131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
  190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
  88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
  77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
  102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
  135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
  5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
  223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
  129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
  251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
  49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
  138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180,
  151,160,137,91,90,15,
  131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
  190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
  88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
  77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
  102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
  135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
  5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
  223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
  129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
  251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
  49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
  138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180,
  ];

var G_MASK = 15;
var G_SIZE = 16;
var G_VECSIZE = 4;
var G = [
	 +1.0, +1.0, +0.0, 0.0 ,
	 -1.0, +1.0, +0.0, 0.0 ,
	 +1.0, -1.0, +0.0, 0.0 ,
	 -1.0, -1.0, +0.0, 0.0 ,
	 +1.0, +0.0, +1.0, 0.0 ,
	 -1.0, +0.0, +1.0, 0.0 ,
	 +1.0, +0.0, -1.0, 0.0 ,
	 -1.0, +0.0, -1.0, 0.0 ,
	 +0.0, +1.0, +1.0, 0.0 ,
	 +0.0, -1.0, +1.0, 0.0 ,
	 +0.0, +1.0, -1.0, 0.0 ,
	 +0.0, -1.0, -1.0, 0.0 ,
	 +1.0, +1.0, +0.0, 0.0 ,
	 -1.0, +1.0, +0.0, 0.0 ,
	 +0.0, -1.0, +1.0, 0.0 ,
	 +0.0, -1.0, -1.0, 0.0
];

function l4(s, v)
{
	console.log(s + ": [" + v[0] + ", " + v[1] + ", " + v[2] + ", " + v[3] + "]");
}

function e4(v)
{
	if(isNaN(v[0]) || isNaN(v[1]) || isNaN(v[2]) || isNaN(v[3])) {
		throw "e4 NAN detected";
		//userData.simAbort = true;
	}
}

function e1(s)
{
	if(isNaN(s)) {
		throw "e1 NAN detected";
		//userData.simAbort = true;
	}
}

function add4(a, b)
{
	nFlops += 4;
	//e4(a); e4(b);
	return [ a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3] ];
}

function sub4(a, b)
{
	nFlops += 4;
	//e4(a); e4(b);
	return [ a[0]-b[0], a[1]-b[1], a[2]-b[2], a[3]-b[3] ];
}

function mul4(v, s)
{
	nFlops += 4;
	//e4(v);e1(s);
	return [ s*v[0], s*v[1], s*v[2], s*v[3] ];
}

function div4(v, s)
{
	nFlops += 4;
	//e4(v);e1(s);
	return [ v[0]/s, v[1]/s, v[2]/s, v[3]/s ];
}

function dot4(a, b)
{
	nFlops += 7;
	//e4(a); e4(b);
	return (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2]) + (a[3]*b[3]);
}

// Note: Three vertices are xyz
function vload4(index, ar)
{
	var i = index * NUM_VERTEX_COMPONENTS;
	return [ ar[i], ar[i+1], ar[i+2], 1.0 ];
}

// Note: Three vertices are xyz
function vstore4(v, index, ar)
{
	//e4(v);
	var i = index * NUM_VERTEX_COMPONENTS;
	ar[i  ] = v[0];
	ar[i+1] = v[1];
	ar[i+2] = v[2];
}

function clamp(x, minval, maxval)
{
	// min(max(x, minval), maxval)
	var mx = (x > minval) ? x : minval;
	return (mx < maxval) ? mx : maxval;
}
	
/*int mod(int x, int a)
{
	int n = (x / a);
	int v = v - n * a;
	if ( v < 0 )
		v += a;
	return v;
}*/

function mod(x, a)
{
	var n = (x / a);
	var v = v - n * a;
	if ( v < 0 )
		v += a;
	return v;
}

/*float mix1d(float a, float b, float t)
{
	float ba = b - a;
	float tba = t * ba;
	float atba = a + tba;
	return atba;
}*/

function mix1d(a, b, t)
{
	nFlops += 3;
	var ba = b - a;
	var tba = t * ba;
	var atba = a + tba;
	return atba;
}

/*float2 mix2d(float2 a, float2 b, float t)
{
	float2 ba = b - a;
	float2 tba = t * ba;
	float2 atba = a + tba;
	return atba;
}*/

function mix2d(a, b, t)
{
	nFlops += 6;
	var ba   = [0, 0];
	var tba  = [0, 0];
	var atba = [0, 0];
	ba[0] = b[0] - a[0];
	ba[1] = b[1] - a[1];
	tba[0] = t * ba[0];
	tba[1] = t * ba[1];
	atba[0] = a[0] + tba[0];
	atba[1] = a[1] + tba[1];
	return atba;
}

/*float4 mix3d(float4 a, float4 b, float t)
{
	float4 ba = b - a;
	float4 tba = t * ba;
	float4 atba = a + tba;
	return atba;
}*/

function mix3d(a, b, t)
{
	nFlops += 12;
	var ba   = [0, 0, 0, 0];
	var tba  = [0, 0, 0, 0];
	var atba = [0, 0, 0, 0];
	ba[0] = b[0] - a[0];
	ba[1] = b[1] - a[1];
	ba[2] = b[2] - a[2];
	ba[3] = b[3] - a[3];
	tba[0] = t * ba[0];
	tba[1] = t * ba[1];
	tba[2] = t * ba[2];
	tba[3] = t * ba[3];
	atba[0] = a[0] + tba[0];
	atba[1] = a[1] + tba[1];
	atba[2] = a[2] + tba[2];
	atba[3] = a[3] + tba[3];
	return atba;
}

/*float smooth(float t)
{
	return t*t*t*(t*(t*6.0f-15.0f)+10.0f);
}*/

function smooth(t)
{
	nFlops += 7;
	return t*t*t*(t*(t*6.0-15.0)+10.0);
}

/*int lattice3d(int4 i)
{
	return P[i.x + P[i.y + P[i.z]]];
}*/

function lattice3d(i)
{
	nFlops += 2;
	return P[i[0] + P[i[1] + P[i[2]]]];
}


/*float gradient3d(int4 i, float4 v)
{
	int index = (lattice3d(i) & G_MASK) * G_VECSIZE;
	float4 g = (float4)(G[index + 0], G[index + 1], G[index + 2], 1.0f);
	return dot(v, g);
}*/

function gradient3d(i, v)
{
	var index = (lattice3d(i) & G_MASK) * G_VECSIZE;
	var g = [ G[index + 0], G[index + 1], G[index + 2], 1.0 ];
	return dot4(v, g);
}

/*float4 normalized(float4 v)
{
	float d = sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
	d = d > 0.0f ? d : 1.0f;
	float4 result = (float4)(v.x, v.y, v.z, 0.0f) / d;
	result.w = 1.0f;
	return result;
}*/

function normalized(v)
{
	nFlops += (SQRT_FLOPS + 8);
	var d = Math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
	d = d > 0.0 ? d : 1.0;
	var result = [ v[0]/d, v[1]/d, v[2]/d, 1.0 ];
	return result;
}

/*float gradient_noise3d(float4 position)
{

	float4 p = position;
	float4 pf = floor(p);
	int4 ip = (int4)((int)pf.x, (int)pf.y, (int)pf.z, 0.0);
	float4 fp = p - pf;
	ip &= P_MASK;

	int4 I000 = (int4)(0, 0, 0, 0);
	int4 I001 = (int4)(0, 0, 1, 0);
	int4 I010 = (int4)(0, 1, 0, 0);
	int4 I011 = (int4)(0, 1, 1, 0);
	int4 I100 = (int4)(1, 0, 0, 0);
	int4 I101 = (int4)(1, 0, 1, 0);
	int4 I110 = (int4)(1, 1, 0, 0);
	int4 I111 = (int4)(1, 1, 1, 0);

	float4 F000 = (float4)(0.0f, 0.0f, 0.0f, 0.0f);
	float4 F001 = (float4)(0.0f, 0.0f, 1.0f, 0.0f);
	float4 F010 = (float4)(0.0f, 1.0f, 0.0f, 0.0f);
	float4 F011 = (float4)(0.0f, 1.0f, 1.0f, 0.0f);
	float4 F100 = (float4)(1.0f, 0.0f, 0.0f, 0.0f);
	float4 F101 = (float4)(1.0f, 0.0f, 1.0f, 0.0f);
	float4 F110 = (float4)(1.0f, 1.0f, 0.0f, 0.0f);
	float4 F111 = (float4)(1.0f, 1.0f, 1.0f, 0.0f);

	float n000 = gradient3d(ip + I000, fp - F000);
	float n001 = gradient3d(ip + I001, fp - F001);

	float n010 = gradient3d(ip + I010, fp - F010);
	float n011 = gradient3d(ip + I011, fp - F011);

	float n100 = gradient3d(ip + I100, fp - F100);
	float n101 = gradient3d(ip + I101, fp - F101);

	float n110 = gradient3d(ip + I110, fp - F110);
	float n111 = gradient3d(ip + I111, fp - F111);

	float4 n40 = (float4)(n000, n001, n010, n011);
	float4 n41 = (float4)(n100, n101, n110, n111);

	float4 n4 = mix3d(n40, n41, smooth(fp.x));
	float2 n2 = mix2d(n4.xy, n4.zw, smooth(fp.y));
	float n = 0.5f - 0.5f * mix1d(n2.x, n2.y, smooth(fp.z));
	return n;
}*/

function gradient_noise3d(position)
{

	var p = position;
	var pf = [ Math.floor(p[0]), Math.floor(p[1]), Math.floor(p[2]), Math.floor(p[3]) ];
	var ip = [ pf[0], pf[1], pf[2], 0 ];
	var fp = sub4(p, pf);
	
	ip[0] = ip[0] & P_MASK;
	ip[1] = ip[1] & P_MASK;
	ip[2] = ip[2] & P_MASK;
	ip[3] = ip[3] & P_MASK;

	var I000 = [0, 0, 0, 0];
	var I001 = [0, 0, 1, 0];
	var I010 = [0, 1, 0, 0];
	var I011 = [0, 1, 1, 0];
	var I100 = [1, 0, 0, 0];
	var I101 = [1, 0, 1, 0];
	var I110 = [1, 1, 0, 0];
	var I111 = [1, 1, 1, 0];

	var F000 = [0.0, 0.0, 0.0, 0.0];
	var F001 = [0.0, 0.0, 1.0, 0.0];
	var F010 = [0.0, 1.0, 0.0, 0.0];
	var F011 = [0.0, 1.0, 1.0, 0.0];
	var F100 = [1.0, 0.0, 0.0, 0.0];
	var F101 = [1.0, 0.0, 1.0, 0.0];
	var F110 = [1.0, 1.0, 0.0, 0.0];
	var F111 = [1.0, 1.0, 1.0, 0.0];

	var n000 = gradient3d(add4(ip, I000), sub4(fp, F000));
	var n001 = gradient3d(add4(ip, I001), sub4(fp, F001));

	var n010 = gradient3d(add4(ip, I010), sub4(fp, F010));
	var n011 = gradient3d(add4(ip, I011), sub4(fp, F011));

	var n100 = gradient3d(add4(ip, I100), sub4(fp, F100));
	var n101 = gradient3d(add4(ip, I101), sub4(fp, F101));

	var n110 = gradient3d(add4(ip, I110), sub4(fp, F110));
	var n111 = gradient3d(add4(ip, I111), sub4(fp, F111));

	var n40 = [n000, n001, n010, n011];
	var n41 = [n100, n101, n110, n111];

	var n4 = mix3d(n40, n41, smooth(fp[0]));
	var n2 = mix2d([n4[0], n4[1]], [n4[2], n4[3]], smooth(fp[1]));
	var n = 0.5 - 0.5 * mix1d(n2[0], n2[1], smooth(fp[2]));
	nFlops += 2;
	return n;
}

/*float ridgedmultifractal3d(
	float4 position,
	float frequency,
	float lacunarity,
	float increment,
	float octaves)
{
	int i = 0;
	float fi = 0.0f;
	float remainder = 0.0f;
	float sample = 0.0f;
	float value = 0.0f;
	int iterations = (int)octaves;

	float threshold = 0.5f;
	float offset = 1.0f;
	float weight = 1.0f;

	float signal = fabs( (1.0f - 2.0f * gradient_noise3d(position * frequency)) );
	signal = offset - signal;
	signal *= signal;
	value = signal;

	for ( i = 0; i < iterations; i++ )
	{
		frequency *= lacunarity;
		weight = clamp( signal * threshold, 0.0f, 1.0f );
		signal = fabs( (1.0f - 2.0f * gradient_noise3d(position * frequency)) );
		signal = offset - signal;
		signal *= signal;
		signal *= weight;
		value += signal * pow( lacunarity, -fi * increment );

	}
	return value;
}*/

function ridgedmultifractal3d(
	position,
	frequency,
	lacunarity,
	increment,
	octaves)
{
	var i = 0;
	var fi = 0.0;
	var remainder = 0.0;
	var sample = 0.0;
	var value = 0.0;
	var iterations = Math.floor(octaves);

	var threshold = 0.5;
	var offset = 1.0;
	var weight = 1.0;

	var signal = Math.abs( (1.0 - 2.0 * gradient_noise3d(mul4(position, frequency))) );
	signal = offset - signal;
	signal *= signal;
	value = signal;
	nFlops += 4;

	for ( i = 0; i < iterations; i++ )
	{
		frequency *= lacunarity;
		weight = clamp( signal * threshold, 0.0, 1.0 );
		signal = Math.abs( (1.0 - 2.0 * gradient_noise3d(mul4(position, frequency))) );
		signal = offset - signal;
		signal *= signal;
		signal *= weight;
		value += signal * Math.pow( lacunarity, -fi * increment );
		nFlops += (POW_FLOPS + 9);
	}
	return value;
}

/*float4 cross3(float4 va, float4 vb)
{
	float4 vc = (float4)(va.y*vb.z - va.z*vb.y,
							va.z*vb.x - va.x*vb.z,
							va.x*vb.y - va.y*vb.x, 0.0f);
	return vc;
}*/

function cross3(va, vb)
{
	nFlops += 9;
	var vc = [ va[1]*vb[2] - va[2]*vb[1],
			   va[2]*vb[0] - va[0]*vb[2],
			   va[0]*vb[1] - va[1]*vb[0],
			   0.0 ];
	return vc;
}

/*__kernel void displace(
	const __global float *vertices,
	__global float *normals,
	__global float *output,
	float dimx, float dimy,
	float frequency,
	float amplitude,
	float phase,
	float lacunarity,
	float increment,
	float octaves,
	float roughness,
	uint count)
{
	int ix = (int) dimx;
	int tx = get_global_id(0);
	int ty = get_global_id(1);
	int sx = get_global_size(0);
	int index = ty * sx + tx;
	if(index >= count)
		return;

	int2 di = (int2)(tx, ty);

	float4 position = vload4((size_t)index, vertices);
	float4 normal = position;
	position.w = 1.0f;

	roughness /= amplitude;
	float4 sample = position + (float4)(phase + 100.0f, phase + 100.0f, phase + 100.0f, 0.0f);

	float4 dx = (float4)(roughness, 0.0f, 0.0f, 1.0f);
	float4 dy = (float4)(0.0f, roughness, 0.0f, 1.0f);
	float4 dz = (float4)(0.0f, 0.0f, roughness, 1.0f);

	float f0 = ridgedmultifractal3d(sample, frequency, lacunarity, increment, octaves);
	float f1 = ridgedmultifractal3d(sample + dx, frequency, lacunarity, increment, octaves);
	float f2 = ridgedmultifractal3d(sample + dy, frequency, lacunarity, increment, octaves);
	float f3 = ridgedmultifractal3d(sample + dz, frequency, lacunarity, increment, octaves);

	float displacement = (f0 + f1 + f2 + f3) / 4.0;

	float4 vertex = position + (amplitude * displacement * normal);
	vertex.w = 1.0f;

	normal.x -= (f1 - f0);
	normal.y -= (f2 - f0);
	normal.z -= (f3 - f0);
	normal = normalized(normal / roughness);

	vstore4(vertex, (size_t)index, output);
	vstore4(normal, (size_t)index, normals);
}*/

function displace(
    vertices,
	normals,
	output,
	frequency,
	amplitude,
	phase,
	lacunarity,
	increment,
	octaves,
	roughness,
	count,
	index)
{
	if(index >= count)
		return;

	// int2 di = (int2)(tx, ty);  // sg: di is not used

	var position = vload4(index, vertices);
	var normal = position;
	position.w = 1.0;

	roughness /= amplitude;
	var sample = add4(position, [phase + 100.0, phase + 100.0, phase + 100.0, 0.0]);
	nFlops += 4;

	var dx = [roughness, 0.0, 0.0, 1.0];
	var dy = [0.0, roughness, 0.0, 1.0];
	var dz = [0.0, 0.0, roughness, 1.0];

	var f0 = ridgedmultifractal3d(sample, frequency, lacunarity, increment, octaves);
	var f1 = ridgedmultifractal3d(add4(sample, dx), frequency, lacunarity, increment, octaves);
	var f2 = ridgedmultifractal3d(add4(sample, dy), frequency, lacunarity, increment, octaves);
	var f3 = ridgedmultifractal3d(add4(sample, dz), frequency, lacunarity, increment, octaves);
	nFlops += 3;
	
	var displacement = (f0 + f1 + f2 + f3) / 4.0;
	nFlops += 4;

	var vertex = add4(position, mul4(normal, amplitude * displacement));
	vertex[3] = 1.0;
	nFlops += 1;

	normal[0] -= (f1 - f0);
	normal[1] -= (f2 - f0);
	normal[2] -= (f3 - f0);
	normal = normalized(div4(normal, roughness));
	nFlops += 7;

	vstore4(vertex, index, output);
	vstore4(normal, index, normals);
}

// for testing
//
//var vertices 	= [1, 1, 1, 1];
//var normals  	= [0, 0, 0, 0];
//var output  	= [0, 0, 0, 0];
//var count		= 1;
//var index		= 0;

//displace(vertices, normals, output, userData.frequency, userData.amplitude, userData.phase, userData.lacunarity, userData.increment, userData.octaves, userData.roughness, count, index);
//console.log("nFlops: " + nFlops);

function SimulateJS() {
	var nVertices	= userData.nVertices;
	var initPos		= userData.initPos;
    var curPos 		= userData.curPos;
    var curNor 		= userData.curNor;
    
    nFlops = 0;
	for(var i=0; i<nVertices; i++)
		displace(initPos, curNor, curPos, userData.frequency, userData.amplitude, userData.phase, userData.lacunarity, userData.increment, userData.octaves, userData.roughness, nVertices, i);
		
	userData.phase += PHASE_DELTA;
	userData.nFlops = nFlops;
}