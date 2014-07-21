import sys, os, os.path, time, shutil
import commands

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement as SE
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

totalNum = 0
failNum = 0
passNum = 0
Flag = "positive"
ConstPath = os.getcwd()
Start = time.strftime("%Y-%m-%d %H:%M:%S")
ResultList = []
Direc = "./"

def lineCount(fp):
    fileTmp = open(fp)
    count = len(fileTmp.readlines())
    fileTmp.close()
    return count

def genSelfcom(combIn, combOut):
    try:
        fp = open(combIn)
        comb = open(combOut, 'a+')
        comb.write(fp.read())
        fp.close()
        comb.close()
        print "Update selfcomb.txt ---------------->O.k"
        return
    except Exception,e:
        print Exception,":",e
        print "Update selfcomb.txt ---------------->Error"
        sys.exit(1)

def processMain(seedIn):
    try:
        print "Input Seed :" + os.path.basename(seedIn)
        print "Excute " + Flag + " cases ------------------------->Start"
        row = 0
        sectionList = []

        fp = open(seedIn)
        for line in fp:
            items = line.strip('\n\r').split(":")
            sectionName = items[0].split("--")[0]
            if sectionName not in sectionList:
                sectionList.append(sectionName)
            inputTxt = open(ConstPath + "/self/" + sectionName + "_input.txt", "a+")
            inputTxt.write(line)
            inputTxt.close()
        fp.close()

        for section in sectionList:
            caseline = ""
            counters = lineCount(ConstPath + "/self/" + section + "_input.txt")
            if counters >= 2:
                lists = [[] for m in range(counters)]
                inputTxt = open(ConstPath + "/self/" + section + "_input.txt")
                for line in inputTxt:
                    items = line.strip('\n\r').split(":")
                    values = items[1].split(",")
                    lists[row].extend(values)
                    row = row + 1
                inputTxt.close()
                pairs = all_pairs(lists)
                outTxt = open(ConstPath + "/self/" + section + "_output.txt", 'w+')
                for e, v in enumerate(pairs):
                    for c in range(len(v)):
                        caseline = caseline + v[c] + ","
                outTxt.write(section + ":" + caseline[:-1] + "\n")
                outTxt.close()
            else:
                shutil.copy(ConstPath + "/self/" + section + "_input.txt", ConstPath + "/self/" + section + "_output.txt")

        #1*********XX_output.txt -> selfcomb.txt
            genSelfcom(ConstPath + "/self/" + section + "_output.txt", ConstPath + "/allpairs/selfcomb.txt")
        
        #2*********selfcomb.txt -> caseXX.txt
        genCases(ConstPath + "/allpairs/selfcomb.txt")

        #3*********output -> manifest.json
        caseExecute(ConstPath + "/allpairs/case_" + Flag + ".txt")

        print "Excute " + Flag + " cases ------------------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Excute " + Flag + " cases ------------------------->Error"
        sys.exit(1)

def genCases(selfcomb):
    try:
        print "Genarate " + Flag + " case.txt file ---------------->Start"
        caseFile = open(ConstPath + "/allpairs/case_" + Flag + ".txt", 'w+')
        names = ""
        row = 0
        counters = lineCount(selfcomb)
        lists = [[] for m in range(counters)]
        fobj = open(selfcomb)
        for line in fobj:
            items = line.strip('\n\r').split(":")
            names = names + items[0] + "\t"
        caseFile.write(names.rstrip("\t") + "\n")

        fobj.seek(0)
        for line in fobj:
            items = line.strip('\n\r').split(":")
            values = items[1:]
            lists[row].extend(":".join(values).split(","))
            row = row + 1
        fobj.close()
        pairs = all_pairs(lists)
        for e, v in enumerate(pairs):
            case = ""
            for c in range(0,len(v)):
                case = case + v[c] +"\t"
            caseFile.write(case.rstrip("\t") + "\n")
        caseFile.close()
        print "Genarate " + Flag + " case.txt file ---------------->O.k"
    except Exception,e:
        print "Generate " + Flag + " case.txt file ---------------->Error"
        print Exception,":",e
        sys.exit(1)

def caseExecute(caseInput):
    try:
        global totalNum
        global failNum
        global passNum
        global ResultList
        global Flag
        global Direc
        print "Excute cases ------------------------->Start"
        caseIn = open(caseInput)
        line = caseIn.readline().strip('\n\r')
        sectionList = line.split("\t")

        os.chdir(ConstPath + "/tools/crosswalk")
        toolstatus = commands.getstatusoutput("python make_apk.py")
        if toolstatus[0] != 0:
            print "Crosswalk Binary is not ready, Please attention"
            sys.exit(1)

        for line in caseIn:
            totalNum = totalNum + 1
            items = line.strip("\t\n").split("\t")
            command = "python make_apk.py "
            data = {"id":"","result":"","entry":"","start":"","end":"","set":""}
            data["start"] = time.strftime("%Y-%m-%d %H:%M:%S")
            for i in range(len(sectionList)):
                items[i] = items[i].replace("000", " ")
                command = command + "--" + sectionList[i] + "=" + '"' + items[i] + '" '
            command = command.strip()
            if "target-dir" in sectionList:
                dirIndex = sectionList.index("target-dir")
                Direc = items[dirIndex]
            else:
                Direc = "./"
            nameIndex = sectionList.index("name")
            packIndex = sectionList.index("package")
            name = items[nameIndex]
            package = items[packIndex]
            print "##########"
            print "Case" + str(totalNum) + " :"
            print "Packer Tool Command:"
            print command
            print "Genarate APK ---------------->Start"
            packstatus = commands.getstatusoutput(command)
            if Flag == "negative":
                if packstatus[0] == 0:
                    print "Genarate APK ---------------->O.K"
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    print "Genarate APK ---------------->Error"
                    result = "PASS"
                    passNum = passNum + 1
            else:
                if packstatus[0] != 0:
                    print "Genarate APK ---------------->Error"
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    print "Genarate APK ---------------->O.K"
                    result = tryRunApp(name, package)

            data["end"] = time.strftime("%Y-%m-%d %H:%M:%S")
            data["id"] = "Case" + str(totalNum)
            data["result"] = result
            data["entry"] = command
            data["set"] = Flag
            ResultList.append(data)
            os.system("rm -rf " + ConstPath + "/tools/crosswalk/" + Direc + "/*apk")
            print "Case Result :",result
            print "##########"
        caseIn.close()
        print "Excute cases ------------------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Execute case ---------------->Error"
        sys.exit(1)

def tryRunApp(name, package):
    try:
        global failNum
        global passNum
        result = "PASS"
        message = ""
        print "Install APK ---------------->Start"
        instatus = commands.getstatusoutput("adb install " + ConstPath + "/tools/crosswalk/" + Direc + "/*apk")
        if instatus[0] == 0:
            print "Install APK ---------------->O.K"
            print "Find Package in device ---------------->Start"
            pmstatus = commands.getstatusoutput("adb shell pm list packages |grep " + package)
            if pmstatus[0] == 0:
                print "Find Package in device ---------------->O.K"
                print "Launch APK ---------------->Start"
                launchstatus = commands.getstatusoutput("adb shell am start -n " + package + "/." + name + "Acivity")
                if launchstatus[0] != 0:
                    print "Launch APK ---------------->Error"
                    os.system("adb uninstall " + package)
                    failNum = failNum + 1
                    result = "FAIL"
                else:
                    print "Launch APK ---------------->O.K"
                    print "Stop APK ---------------->Start"
                    stopstatus = commands.getstatusoutput("adb shell am force-stop " + package)
                    if stopstatus[0] == 0:
                        print "Stop APK ---------------->O.K"
                        print "Uninstall APK ---------------->Start"
                        unistatus = commands.getstatusoutput("adb uninstall " + package)
                        if unistatus[0] == 0:
                            print "Uninstall APK ---------------->O.K"
                            passNum = passNum + 1
                        else:
                            print "Uninstall APK ---------------->Error"
                            failNum = failNum + 1
                            result = "FAIL"
                    else:
                        print "Stop APK ---------------->Error"
                        failNum = failNum + 1
                        result = "FAIL"
                        os.system("adb uninstall " + package)
            else:
                print "Find Package in device ---------------->Error"
                os.system("adb uninstall " + package)
                failNum = failNum + 1
                result = "FAIL"
        else:
            print "Install APK ---------------->Error"
            result = "FAIL"
            failNum = failNum + 1
        os.system("rm -rf " + ConstPath + "/tools/crosswalk/" + Direc + "/*apk" + "&>/dev/null")
        return result
    except Exception,e:
        print Exception,":",e
        print "Try run webapp ---------------->Error"
        sys.exit(1)

def updateXmlTitle(fp,title):
    fobj = open(fp, "r+")
    lines = fobj.readlines()
    fobj.seek(0)
    fobj.truncate()
    lines.insert(0,title)
    fobj.writelines(lines)
    fobj.close()

def genResultXml():
    try:
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
        setPositive = SE(suite, "set", {"name":"positive","set_debug_msg":""})
        setNegitive = SE(suite, "set", {"name":"negitive","set_debug_msg":""})

        #testcase element
        for case in ResultList:
            setElement = setPositive
            if case["set"] == "negative":
                setElement = setNegitive
            pur = "Check if packer tool work properly"
            testcase = SE(setElement, "testcase", {"component":"Crosswalk Packer Tool",\
            "execution_type":"auto","id":case["id"],"purpose":pur,"result":case["result"]},)
            desc = SE(testcase, "description")
            entry = Element("test_script_entry")
            entry.text = "pack command: " + case["entry"].decode("utf-8")
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
        updateXmlTitle(ConstPath + "/report/wrt-packertoolauto-android-tests.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/testresult.xsl"?>\n<?xml-stylesheet type="text/xsl" href="testresult.xsl"?>\n')
        
        print "Generate test.result.xml file ------------------------->O.K"
    except Exception,e:
        print Exception,"Generate test.result.xml error:",e

def genSummaryXml():
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
        total_case.text = str(totalNum)
        pass_case = SE(suite, "pass_case")
        pass_case.text = str(passNum)
        pass_rate = SE(suite, "pass_rate")
        pass_rate.text = str(float(passNum) / totalNum * 100)
        fail_case = SE(suite, "fail_case")
        fail_case.text = str(failNum)
        fail_rate = SE(suite, "fail_rate")
        fail_rate.text = str(float(failNum) / totalNum * 100)
        SE(suite, "block_case")
        SE(suite, "block_rate")
        SE(suite, "na_case")
        SE(suite, "na_rate")
        tree.write(ConstPath + "/report/summary.xml")
        updateXmlTitle(ConstPath + "/report/summary.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/summary.xsl"?>\n')
        print "Generate summary.xml file ------------------------->O.K"
    except Exception,e:
        print Exception,"Generate summary.xml error:",e

def devicesConform():
    try:
        deviceList = os.popen("adb devices").readlines()
        if len(deviceList) == 2:
            print "No test devices connected, Please attention"
            sys.exit(1)
    except Exception,e: 
        print Exception,"Device Connect error:",e
        sys.exit(1)

def main():
    try:
        global End
        global Flag
        os.system("rm -rf " + ConstPath + "/allpairs/negative/*~ &>/dev/null")
        os.system("rm -rf " + ConstPath + "/allpairs/positive/*~ &>/dev/null")
        os.system("rm -rf " + ConstPath + "/allpairs/positive/case*txt &>/dev/null")
        os.system("rm -rf " + ConstPath + "/tools/crosswalk/*apk &>/dev/null")
        os.system("rm -rf " + ConstPath + "/self &>/dev/null")
        os.system("mkdir -p " + ConstPath + "/self")
        devicesConform()

        #positive test
        for seed in os.listdir(ConstPath + "/allpairs/positive/"):
            os.system("rm -rf " + ConstPath + "/allpairs/selfcomb.txt &>/dev/null")
            os.system("rm -rf " + ConstPath + "/self &>/dev/null")
            os.system("mkdir -p " + ConstPath + "/self")
            processMain(ConstPath + "/allpairs/positive/" + seed)

        #negative case
        Flag = "negative"
        for seed in os.listdir(ConstPath + "/allpairs/negative/"):
            os.system("rm -rf " + ConstPath + "/allpairs/selfcomb.txt &>/dev/null")
            os.system("rm -rf " + ConstPath + "/self &>/dev/null")
            os.system("mkdir -p " + ConstPath + "/self")
            processMain(ConstPath + "/allpairs/negative/" + seed)

        End = time.strftime("%Y-%m-%d %H:%M:%S")
        genResultXml()
        genSummaryXml()
    except Exception,e:
        print Exception,":",e
        sys.exit(1)
    finally:
        os.system("rm -rf " + ConstPath + "/self &>/dev/null")

if __name__=="__main__":
    main()
