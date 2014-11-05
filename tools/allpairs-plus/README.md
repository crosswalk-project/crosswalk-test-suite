allpairs-plus
===============

## Introduction

allpairs-plus tool here is based the pairwise tool of "all pairs", to use minimal test cases that achieves maximal coverage, we improves all pairs with new "parameter self-combination" method in best practices, it split the parameter to sub-parameters, and extend the tool from one-dimensional to two-dimensional.

Pairwise tool is an effective data-driven test case generation technique, which is based on the observation that most faults are caused by interactions of two factors.By using this method, you can get remarkable test cases coverage.

## Parameter Self-combination Method

Pairwise tool - all pairs disadvantages:

Parameter is the basic unit for pair combination, when a parameter has wide choice of value set, its difficult to list all of them in input seed file manually.
All of the parameters in the seed file must participate into the combination, but sometimes, we need to setting switch of it
So we improves Pairwise with new "parameter self-combination" method in best practices, split the parameter to sub-parameters, and extend Pairwise testing from one-dimensional to two-dimensional.

Check below for more details.

![image](https://github.com/cicili/tools/blob/master/allpairs-plus/doc/self-combination-method.png)

## Tool Instructions

### Tool Input

input/input_seed.txt

* Basic usage
```
 <parameterA>: <valueA1>, <valueA2>, <valueAY>
  ......
 <parameterX>: <valueX1>, <valueX2>, <valueXY>
```

* Advanced usage - parameter self-combination
```
 <parameterA-sub1>: <valueA11>, <valueA12>, <valueA1Y>
  ......
 <parameterA-subN>: <valueAN1>,<valueAN2>, <valueANY>
  ......
 <parameterX>: <valueX1>, <valueX2>, <valueXY>
```

 * Condition
```
 Parameter name must unique, and its case sensitive     
 Delimiter is ',' in seed file
 If parameter value have conflict with delimiter, use 'comma' instead
```
 
### Tool Output

Output: output/output.txt

```
 ParameterA		ParameterB		...	ParameterX
 <valueA1>		<valueB1>		...	<valueX1>
 ...			...			...	...
 <valueAi>		<valueBj>		...	<valueXk>
```
```Delimiter is TAB```

### Tool Execution

Run Pairwise tool

    $ python allpairs-plus.py
    

# Tools Packages Usage 

* doc - document or flow chart for allpairs-plus tool
* input - input data
* output - output data
  * selfcomb.txt - self-combination result, this is a intermediate result for reference
  * output.txt - output data
* metacomm - this folder is for allpairs
  * Which get from [allpairs](http://sourceforge.net/projects/allpairs/files/allpairs/) after it has been installed
