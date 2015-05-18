#pragma OPENCL EXTENSION cl_khr_fp16 : enable
__kernel void kernelHalf(
        float input,
        __global half* output)
{
    output[0] = convert_half(input);
}
