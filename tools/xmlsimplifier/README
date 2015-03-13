This tools is for simplify the complex tests.xml.

Usage:
        simplifier.py -h | --help
        simplifier.py -f <file> [-o <output>] [-p <platform>] [-e <execution>]

Arguments:
  file     the complex test file which need to simplify
  output   output file
  platform platform
  execution execution type


Options:
  -f, --file         Specify an test definition file (tests.xml)
  -o, --output       Specify an output file
  -p, --platform     Specify a platform
  -e, --execution    Specify a execution type

HOW TO:
    1.Pre-condition
    The script will use xmllint to format xml, so you should install xmllint first:
    $ sudo apt-get install xmllint


    2.How to  Config
    you can config all the attributes and element nodes in testcases which need to keep in the simplify tests.xml .
    For example:
    for auto case :
        [auto]
        #keeped attribute
        attribute = id,execution_type,purpose,onload_delay
        #keeped element nodes
        element_nodes = description,test_script_entry

    for manual case :
        [manual]
        #keeped attribute
        attribute = id,execution_type,purpose,onload_delay
        #keeped element nodes
        element_nodes = description,pre_condition,steps,step,step_desc,expected,test_script_entry


    3.HOW to USE
    If you want the simple tests.xml replaced the old one,you can use:
    $ simplifier.py -f <tests.xml>
    You also can specify an output file name for the simple tests.xml:
    $ simplifier.py -f <tests.xml> -o <output>
    If you need select platfrom or execution type, you can use:
    $ simplifier.py -f <tests.xml> -o <output> -p <platform>
    $ simplifier.py -f <tests.xml> -o <output> -e <execution>
    If you need select platfrom and execution type, you can use:   
    $ simplifier.py -f <tests.xml> -o <output> -p <platform> -e <execution>
