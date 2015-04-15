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

if(typeof(WebCL) === "undefined") {

    console.log("Using opencl.js stub");

    function WebCL () {
        this.SUCCESS = 0;
        this.DEVICE_TYPE_GPU = 1;
        this.DEVICE_TYPE_CPU = 2;
        this.PROGRAM_BUILD_LOG = 3;
        this.MEM_READ_ONLY = 4;
        this.MEM_WRITE_ONLY = 5;
        this.MEM_READ_WRITE = 6;
        this.KERNEL_WORK_GROUP_SIZE = 7;

        // see OpenCL 1.1 tables 6.2, 6.3

        this.KERNEL_ARG_CHAR        =   8000;
        this.KERNEL_ARG_UCHAR       =   8001;
        this.KERNEL_ARG_SHORT       =   8002;
        this.KERNEL_ARG_USHORT      =   8003;
        this.KERNEL_ARG_INT         =   8004;
        this.KERNEL_ARG_UINT        =   8005;
        this.KERNEL_ARG_LONG        =   8006;
        this.KERNEL_ARG_ULONG       =   8007;
        this.KERNEL_ARG_FLOAT       =   8008;

        // n = 2,3,4,8,16 (only 4 for testing)

        this.KERNEL_ARG_CHAR4       =   8400;
        this.KERNEL_ARG_UCHAR4      =   8401;
        this.KERNEL_ARG_SHORT4      =   8402;
        this.KERNEL_ARG_USHORT4     =   8403;
        this.KERNEL_ARG_INT4        =   8404;
        this.KERNEL_ARG_UINT4       =   8405;
        this.KERNEL_ARG_LONG4       =   8406;
        this.KERNEL_ARG_ULONG4      =   8407;
        this.KERNEL_ARG_FLOAT4      =   8408;

        // special types

        this.KERNEL_ARG_IMAGE2D     =   100;
        this.KERNEL_ARG_IMAGE3D     =   101;
        this.KERNEL_ARG_SMAPLER     =   102;
        this.KERNEL_ARG_EVENT       =   104;    

        this.getError = function() { return this.SUCCESS; };
        this.getPlatformIDs = function() { return [11, 22]; };
        this.getDeviceIDs = function(platform_id, device_type) { return [33, 44]; };
        this.createContext = function (context_properties, device_id, notify, userData) { return new WebCLContext(); }; // device_ids is int or array
        this.createContextFromType = function(context_properties, device_type, notify, userData) { return new WebCLContext(); }
        this.createCommandQueue = function(context, device_ids, properties) { return new WebCLQueue(); };
        this.createProgramWithSource = function(context, kernelSource) { return new WebCLProgram(); };
        this.buildProgram = function(program, opts, notify, userData) { return this.SUCCESS; };
        this.buildProgram = function(program, device_ids, opts, notify, userData) { return this.SUCCESS; }; // device_ids is int or array
        this.createKernel = function(program, kernelName) { return new WebCLKernel(); };
        this.createKernelsInProgram = function(program) { return new WebCLKernel(); };
        this.createBuffer = function(context, flags, size, host_ptr) { return new WebCLMemObject(); };
        
        this.createUserEvent = function(context) { return WebCLEvent() };
        this.setUserEventStatus = function(event, execution_status) { return this.SUCCESS; };
        this.enqueueTask = function(queue, kernel, event_list) { return WebCLEvent() }; 

        // from Image, Canvas, ImageData, CanvasPixelArray, 
        this.createImage2D = function(context, flags, obj) { return new WebCLImage(); };

        // from Uint8Array
        this.createImage2D = function(context, flags, uint8Array, nComponents) { return new WebCLImage(); };
        this.createImage2D = function(context, flags, uint8Array) { return new WebCLImage(); };
        this.createImage3D = function(context, flags, width, height, nComponents, uint8Array) { return new WebCLImage(); };
        
        this.createSampler = function(context, normalized_coords, address_mode, filter_mode) { return new WebCLSampler(); };
        
        this.enqueueWriteBuffer = function(queue, buffer, blocking_write, offset, buffer_size, ptr, event_wait_list) { return new WebCLEvent(); };
        this.enqueueWriteImage  = function(queue, image,  blocking_write, origin, region, jsImage, event_wait_list) { return new WebCLEvent(); };

        // setKernelArg: forms to be deprecated
        this.setKernelArg = function(kernel, arg_index, arg_value, arg_size) { return this.SUCCESS; }; // __local: val (ignored) and size

        // setKernelArg: new forms
        this.setKernelArg = function(kernel, arg_index, arg_value, arg_type) { return this.SUCCESS; };  // <type>, const <type>
        this.setKernelArgGlobal = function(kernel, arg_index, arg_value) { return this.SUCCESS; };      // __global <type>*, const __global <type>*
        this.setKernelArgConstant = function(kernel, arg_index, arg_value) { return this.SUCCESS; };    // __constant <type>*, const __constant <type>*
        this.setKernelArgLocal = function(kernel, arg_index, arg_size) { return this.SUCCESS; };        // __local <type>*, const __local <type>*

        this.enqueueNDRangeKernel = function(queue, kernel, work_dim, global_work_offset, global_work_size, local_work_size, event_wait_list) { return new WebCLEvent(); };
        this.finish = function (queue, cb, userData) { if(cb !== null) cb(userData); return this.SUCCESS; };
        this.enqueueReadBuffer = function(queue, buffer, blocking_read, offset, buffer_size, ptr, event_wait_list) { return new WebCLEvent(); };
        this.enqueueReadImage  = function(queue, image,  blocking_read, origin, region, jsImage, event_wait_list) { return new WebCLEvent(); };
        this.releaseCLResource = function(input) { return this.SUCCESS; };
        this.releaseCLResource = function(program) { return this.SUCCESS; };
        this.releaseCLResource = function(kernel) { return this.SUCCESS; };
        this.releaseCLResource = function(queue) { return this.SUCCESS; };
        this.releaseCLResource = function(context) { return this.SUCCESS; };
        this.unloadCompiler = function() { return this.SUCCESS; };

        this.getCommandQueueInfo = function(queue, queue_info_type) { return new WebCLCommandQueueInfo(); };
        this.getContextInfo = function(context,cl_context_name){ return new WebCLContextInfo(); };
        this.getDeviceInfo = function(device_ids, device_info_type) { return new WebCLDeviceInfo(); };
        this.getEventInfo = function(event, event_info_type) { return new WebCLEventInfo(); };
        this.getEventProfilingInfo = function(event, event_profling_info_type) { return new WebCLEventProfilingInfo(); };
        this.getKernelInfo = function(kernel, cl_kernel_info_type){return new WebCLKernelInfo(); };
        this.getKernelWorkGroupInfo = function(kernel, device_id, param_name) { return new WebCLKernelWorkGroupInfo(); };
        this.getPlatformInfo = function(device_ids, device_info_type) { return new WebCLPlatformInfo(); };
        this.getProgramInfo = function(program, paramName) { return new WebCLProgramInfo(); };
        this.getProgramBuildInfo = function(program, device_id, paramName) { return new WebCLProgramBuildInfo(); };
        this.getSamplerInfo = function(sampler, paramName) { return new WebCLSamplerInfo(); };

        // GL CL Interop    
        this.createSharedContext = function(device_type, notify, userData) { return new WebCLContext(); };
        this.createFromGLBuffer = function(context, flags, glBuffer) { return new WebCLMemObject(); };
        this.enqueueAcquireGLObjects = function(queue, mem_objects, event_wait_list) { return new WebCLEvent(); };
        this.enqueueReleaseGLObjects = function(queue, mem_objects, event_wait_list) { return new WebCLEvent(); };
    }

    function WebCLContext() {}
    function WebCLQueue() {}
    function WebCLProgram() {}
    function WebCLKernel() {}
    function WebCLMemObject() {}
    function WebCLImage() {}
    function WebCLSampler() {}
    function WebCLEvent() {}
    function WebCLEventList() { return new Array(2); }

    function WebCLDeviceInfo() {}
    function WebCLEventInfo() {}
    function WebCLEventProfilingInfo() {}
    function WebCLCommandQueueInfo() {}
    function WebCLContextInfo() {}
    function WebCLKernelInfo() {}
    function WebCLKernelWorkGroupInfo() {}
    function WebCLPlatformInfo() {}
    function WebCLProgramInfo() {}
    function WebCLProgramBuildInfo() {}
    function WebCLSamplerInfo() {}
}
