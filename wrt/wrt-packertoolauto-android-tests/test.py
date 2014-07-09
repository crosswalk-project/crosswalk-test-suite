import sys, os, os.path, time 
import commands
from ConfigParser import ConfigParser

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement as SE
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

global Start
global End
global ConstPath
global total
global passNum
global failNum

def lineCount(fp):
    fileTmp = open(fp)
    count = len(fileTmp.readlines())
    fileTmp.close()
    return count

def genCombFile(sourceFile, expect):
    print "Generate output.txt file ------------------------->Start"
    try:
        cmdItems = ""
        cmdValues = ""
        row = 0

        optCount = lineCount(sourceFile)
        lists = [[] for x in range(optCount)]

        inputTxt= open(sourceFile)
        outputTxt = open(ConstPath + "/allpairs/output.txt", 'a+')
        for line in inputTxt:
            line = line.strip('\n\r')
            items = line.split("=")
            cmdItems = cmdItems + items[0] + "\t"
        outputTxt.write(cmdItems + "expect" + "\t" + "name" + "\t" + "dir" + "\t" + "package" + "\n")

        packIndex = cmdItems.split("\t").index("package")
        nameIndex = cmdItems.split("\t").index("name")
        dirIndex = cmdItems.split("\t").index("target-dir")
        inputTxt.seek(0)
        for line in inputTxt:
            line = line.strip('\n\r')
            items = line.split("=")
            valueString = items[1]
            values = valueString.split(",")
            for value in values:
                lists[row].append(value)
            row = row + 1
        allPairs = all_pairs(lists)
        for x,y in enumerate(allPairs):
            for v in y:
                cmdValues = cmdValues +  v + "\t"
            cmdValues = cmdValues + expect + "\t" + y[nameIndex] + "\t" + y[dirIndex] + "\t" + y[packIndex] + "\n"
        outputTxt.write(cmdValues)
        print "Generate ouput.txt file ------------------------->End"
    except Exception,e:
        print Exception,":",e
        sys.exit(1)
    finally:
        inputTxt.close()
        outputTxt.close()

def genCases():
    print "Genarate case.txt file ------------------------->Start"
    try:
        caseList = []
        caseFile = open(ConstPath + "/allpairs/case.txt", "a+")
        caseFile.truncate()

        inputFile = open(ConstPath + "/allpairs/output.txt")
        lines = inputFile.readlines() 
        inputFile.close()

        optionList = lines[0].strip("\n").split("\t")[:-4]
        for line in lines[1:]:
            case = "python make_apk.py "
            valueList = line.strip("\n").split("\t")
            values = valueList[:-4]
            for num in range(len(optionList)):
                case = case + "--%s=%s " % (optionList[num], valueList[num])
            caseList.append(case.rstrip() + "\t" + valueList[-4] + "\t" + valueList[-3] + "\t" + valueList[-2] + "\t" + valueList[-1] + "\n")

        caseFile.writelines(caseList)
        print "Genarate case.txt file ------------------------->End"
    except Exception,e:
        print Exception,"Generate Cases error:",e
    finally:
        caseFile.close()

def caseExecute():
    print "Excute cases ------------------------->Start"
    try:
        global Start
        global End
        global total
        global passNum
        global failNum
        passNum = 0
        failNum = 0
        index = 0
        total = lineCount(ConstPath + "/allpairs/case.txt")
        print "Total Num:",total
        caseResult = []
        os.chdir(ConstPath + "/tools/crosswalk")
        caseFile = open(ConstPath + "/allpairs/case.txt")

        Start = time.strftime("%Y-%m-%d %H:%M:%S")
        for cmd in caseFile:
            data = {"id":"","result":"","cmd":"","start":"","end":""}
            caseResult.append(data)
            result = "PASS"
            print "###"
            casenum = "Case" + str(index + 1)
            data["start"] = time.strftime("%Y-%m-%d %H:%M:%S")
            case = cmd.strip("\n").split("\t")
            command = case[0]
            expect = case[-4]
            name = case[-3]
            direc = case[-2]
            package = case[-1]
            print casenum + ":"
            print "Case Packer Tool Command:"
            print command
            print "Genarate APK ---------------->Start"
            packfeed = commands.getstatusoutput(command)
            if packfeed[0] != 0:
                print "Genarate APK ---------------->Failed"
                if expect == "PASS":
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    passNum = passNum + 1
            else:
                print "Genarate APK ---------------->Succeed"
                if expect == "FAIL":
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    print "Install APK ---------------->Start"
                    insfeed = commands.getstatusoutput("adb install " + direc + "*apk")
                    if insfeed[0] == 0:
                        print "Install APK ---------------->Succeed"
                        instatus = checkNamePackage(name,package)
                        if instatus == 0:
                            print "Uninstall APK ---------------->Start"
                            unifeed = commands.getstatusoutput("adb uninstall " + package)
                            if unifeed[0] != 0:
                                print "Uninstall APK ---------------->Failed"
                                result = "FAIL"
                                failNum = failNum + 1
                            else:
                                passNum = passNum + 1
                                print "Uninstall APK ---------------->Succeed"
                        else:
                            print "Install APK ---------------->Failed"
                            commands.getstatusoutput("adb uninstall " + package)
                            result = "FAIL"
                            failNum = failNum + 1
                    else:
                        print "Install APK ---------------->Failed"
                        result = "FAIL"
                        failNum = failNum + 1

            print "Case Result:",result
            os.system("rm -rf " + direc + "*apk")
            os.system("rm -rf *apk")
            data["end"] = time.strftime("%Y-%m-%d %H:%M:%S")
            data["id"] = casenum
            data["result"] = result
            data["cmd"] = command
            index = index + 1
            print "###"

        End = time.strftime("%Y-%m-%d %H:%M:%S")
        print "Excute cases ------------------------->End"
        genResultXml(caseResult)
        genSummaryXml(caseResult)
    except Exception,e:
        print Exception,"Execute Case error:",e
    finally:
        caseFile.close()

def checkNamePackage(name, package):
    os.chdir(ConstPath + "/tools/build-tools")
    result = 0
    output1 = commands.getstatusoutput("adb shell pm list packages |grep " + package)
    if output1[0] == 0:
        print "Find Package in device ---------------->Succeed"
        output2 = commands.getstatusoutput("adb shell pm path " + package)
        if output2[0] == 0:
            print "Get the path of package ---------------->Succeed"    
            path = output2[1].strip("\n\r").split(":")[1]
            apk = path.split("/")[-1]
            output3 = commands.getstatusoutput("adb pull " + path)
            if output3[0] == 0:
                print "Pull APK from device ---------------->Succeed"
                output4 = commands.getstatusoutput("./aapt dump badging " + apk)
                if output4[0] == 0:
                    print "Dump APK ---------------->Succeed"
                    if output4[1].find("label='" + name + "'") == -1:
                        print "Check APK Name ---------------->Failed"
                        result = 1
                    else:
                        print "Check APK Name ---------------->Succeed"
                else:
                    print "Dump APK ---------------->Failed"
                    result = 1
            else:
                print "Pull APK from device ---------------->Failed"
                result = 1
        else:
            print "Get the path of package ---------------->Failed"
            result = 1       
    else:
        print "Find Package in device ---------------->Failed"
        result = 1

    os.system("rm -rf *apk")
    os.chdir(ConstPath + "/tools/crosswalk")
    return result
    

def addTitie(fp,title):
    tmp = open(fp, "r+")
    lines = tmp.readlines()
    tmp.seek(0)
    tmp.truncate()
    lines.insert(0,title)
    tmp.writelines(lines)
    tmp.close()

def genResultXml(caseResult):
    try:
        resultFile = open(ConstPath + "/report/wrt-packertoolauto-android-tests.xml", "w+")
        resultFile.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/testresult.xsl"?>\n<?xml-stylesheet type="text/xsl" href="testresult.xsl"?>')
        resultFile.close()
        tree = ElementTree()
        root = Element("test_definition")
        tree._setroot(root)

        env = Element("environment", {"build_id":"","device_id":"","device_name":"","host":"",\
        "lite_version":"","manufacturer":"","resolution":"","screen_size":""})
        root.append(env)

        #summary element
        summary = Element("summary", {"test_plan_name":""})
        root.append(summary)
        tStart = SE(summary, "start_at")
        tEnd = SE(summary, "end_at")
        tStart.text = Start
        tEnd.text = End

        #suite element
        suite = SE(root, "suite", {"category":"Crosswalk_Packer_Tool","launcher":"xwalk",\
        "name":"wrt-packertoolauto-android-tests"})
        setElement = SE(suite, "set", {"name":"packertool","set_debug_msg":""})

        #testcase element
        for case in caseResult:
            pur = "Check if packer tool work properly"
            testcase = SE(setElement, "testcase", {"component":"Crosswalk Packer Tool",\
            "execution_type":"auto","id":case["id"],"purpose":pur,"result":case["result"]},)
            desc = SE(testcase, "description")
            entry = Element("test_script_entry")
            entry.text = "pack command: " + case["cmd"]
            desc.append(entry)
            resultInfo = SE(testcase, "result_info")
            actualResult = SE(resultInfo, "actual_result")
            actualResult.text = case["result"]
            caseStart = SE(resultInfo, "start")
            caseStart.text = case["start"]
            caseEnd = SE(resultInfo, "end")
            caseEnd.text = case["end"] 
            SE(resultInfo, "stdout")
            SE(resultInfo, "stderr")

        tree.write(ConstPath + "/report/wrt-packertoolauto-android-tests.xml")
        addTitie(ConstPath + "/report/wrt-packertoolauto-android-tests.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/testresult.xsl"?>\n<?xml-stylesheet type="text/xsl" href="testresult.xsl"?>\n')
        
        print "Generate test.result.xml file ------------------------->O.K"
    except Exception,e:
        print Exception,"Generate test.result.xml error:",e

def genSummaryXml(caseResult):
    try:
        tree = ElementTree()
        root = Element("result_summary", {"plan_name":""})
        tree._setroot(root)
        env = SE(root,"environment",{"build_id":"","cts_version":"","device_id":"","device_model":"","device_name":"","host":"","resolution":"","screen_size":"","manufacturer":""})
        summary = SE(root, "summary")
        startTime = SE(summary, "start_at")
        endTime = SE(summary, "end_at")
        startTime.text = Start
        endTime.text = End
        suite = SE(root, "suite", {"name":"wrt-packertoolauto-android-tests"})
        total_case = SE(suite, "total_case")
        total_case.text = str(total)
        pass_case = SE(suite, "pass_case")
        pass_case.text = str(passNum)
        pass_rate = SE(suite, "pass_rate")
        pass_rate.text = str(float(passNum) / total * 100)
        fail_case = SE(suite, "fail_case")
        fail_case.text = str(failNum)
        fail_rate = SE(suite, "fail_rate")
        fail_rate.text = str(float(failNum) / total * 100)
        SE(suite, "block_case")
        SE(suite, "block_rate")
        SE(suite, "na_case")
        SE(suite, "na_rate")
        tree.write(ConstPath + "/report/summary.xml")
        addTitie(ConstPath + "/report/summary.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/summary.xsl"?>\n')
        print "Generate summary.xml file ------------------------->O.K"
    except Exception,e:
        print Exception,"Generate summary.xml error:",e

def devicesConform():
    try:
        deviceList = os.popen("adb devices").readlines()
        if (len(deviceList) == 2):
            print "No test devices connected, Please attention"
            sys.exit(1)
	
    except Exception,e: 
        print Exception,"Device Connect error:",e
        sys.exit(1)

def main():
    try:
        global ConstPath
        ConstPath = os.getcwd()
        devicesConform()
        fp = open(ConstPath + "/allpairs/output.txt", "a+")
        fp.truncate()
        fp.close()

        for seedFile in os.listdir(ConstPath + "/allpairs"):
            expect = "PASS"
            if seedFile.startswith("input"):
                if seedFile.find("negative") != -1:
                    expect = "FAIL"
                genCombFile(ConstPath + "/allpairs/" + seedFile, expect)
            else:
                continue

        genCases()
        caseExecute()
    except Exception,e:
        print Exception,":",e
        sys.exit(1)

if __name__=="__main__":
    main()
