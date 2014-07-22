import sys, os, shutil, time
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
        print Exception,"Update selfcomb.txt error:",e
        print "Update selfcomb.txt ---------------->Error"
        sys.exit(1)

def caseExecute(caseInput):
    try:
        global totalNum
        global failNum
        global passNum
        global ResultList

        manifestLog = open(ConstPath + "/report/manifest_"+ Flag + ".txt", 'a+')

        caseIn = open(caseInput)
        line = caseIn.readline().strip('\n\r')
        sectionList = line.split("\t")

        for line in caseIn:
            totalNum = totalNum + 1
            caseValue = ""
            message = ""
            print "##########"
            print "Case" + str(totalNum) + " :"
            print "Generate manifest.json ---------------->Start"
            items = line.strip('\n\r').split("\t")
            caseDir = ConstPath + "/tcs/manifest" + str(totalNum)
            os.mkdir(caseDir)
            fp = open(caseDir + "/manifest.json", 'w+')
            for i in range(len(items)):
                items[i] = items[i].replace("null","")
                if sectionList[i] not in ("icons", "icon", "xwalk_launch_screen", "xwalk_permissions"):
                    items[i] = items[i].replace("000", " ")
                    caseValue = caseValue + '"' + sectionList[i] + '" : "' + items[i] + '",\n'
                else:
                    items[i] = items[i].replace("comma", ",")
                    caseValue = caseValue + '"' + sectionList[i] + '" : ' + items[i] + ",\n"
            caseValue = "{\n" + caseValue[:-2] + "\n}"
            fp.write(caseValue)
            fp.close()
            print "Generate manifest.json ---------------->O.K"
            print caseValue
            manifestLog.write("manifest" + str(totalNum) + "\n--------------------------------\n" + caseValue + "\n--------------------------------\n")
            #copy source and config
            os.system("cp -rf " + ConstPath + "/resource/* " + caseDir)
            updateConfigXml(ConstPath + "/tcs/manifest" + str(totalNum) + "/config.xml", "manifest" + str(totalNum))
            #genarate package and execute
            os.chdir(ConstPath + "/tools/crosswalk/")
            data = {"id":"","result":"","entry":"","message":"","start":"","end":"","set":""}
            caseStart = time.strftime("%Y-%m-%d %H:%M:%S")
            status = genPackage(caseDir)
            if Flag == "negative":
                if status == 0:
                    failNum = failNum + 1
                    result = "FAIL"
                    message = "generate apk succeed"
                else:
                    passNum = passNum + 1
                    result = "PASS"
            else:
                if status != 0:
                    failNum = failNum + 1
                    result = "FAIL"
                    message = "generate apk error"
                else:
                    result, message = tryRunApp()
            caseEnd = time.strftime("%Y-%m-%d %H:%M:%S")
            data["id"] = "manifest" + str(totalNum)
            data["result"] = result
            data["entry"] = caseValue
            data["message"] = message
            data["start"] = caseStart
            data["end"] = caseEnd
            data["set"] = Flag
            ResultList.append(data)
            print "Case Result :" + result
            print "##########"
            os.system("rm -rf " + ConstPath + "/tcs/manifest" + str(totalNum) + "&>/dev/null")

        caseIn.close()
        manifestLog.close()
        print "Execute case ---------------->O.K"
    except Exception,e: 
        print Exception,":",e
        print "Execute case ---------------->Error"
        sys.exit(1)

def lineCount(fp):
    fileTmp = open(fp)
    count = len(fileTmp.readlines())
    fileTmp.close()
    return count

def processMain(seedIn):
    try:
        print "Input Seed :" + seedIn
        print "Excute " + Flag + " cases ------------------------->Start"
        row = 0
        sectionList = []

        fp = open(seedIn)
        for line in fp:
            items = line.strip('\n\r').split(":")
            sectionName = items[0].split("-")[0]
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
                inputTxt = open(ConstPath + "/self/" + section + "_input.txt", 'r+')
                for line in inputTxt:
                    items = line.strip('\n\r').split(":")
                    values = items[1].split(",")
                    lists[row].extend(values)
                    row = row + 1
                pairs = all_pairs(lists)
                inputTxt.close()
                outTxt = open(ConstPath + "/self/" + section + "_output.txt", 'a+')
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
        print "Excute " + Flag + " cases ------------------------->Error"
        print Exception,":",e
        sys.exit(1)

def genPackage(direc):
    try:
        print "Generate APK ---------------->Start"
        toolstatus = commands.getstatusoutput("python make_apk.py")[0]
        if toolstatus != 0:
            print "Crosswalk Binary is not ready, Please attention"
            sys.exit(1)
        cmd ="python make_apk.py --name=test --package=org.xwalk.test --arch=x86 --manifest="
        manifestPath = direc + "/manifest.json"
        status = commands.getstatusoutput(cmd + manifestPath)[0]
        if status != 0:
            print "Generate APK ---------------->Error"
        else:
            print "Generate APK ---------------->O.K"
        return status
    except Exception,e:
        print Exception,":",e
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

def updateConfigXml(manifest, name):
    try:
        print "Update config.xml ---------------->Start"
        line = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><widget xmlns=\"http://www.w3.org/ns/widgets\" id=\"http://example.org/exampleWidget\" version=\"1.1\" height=\"200\" widtht=\"200\" viewmode=\"fullscreen\"><name short=\"manifest\">" + name + "</name></widget>"
        fp = open(manifest, 'w+')
        fp.write(line)
        fp.close()
        print "Update config.xml ---------------->O.k"
    except Exception,e:
        print "Update config.xml ---------------->Error"
        print Exception,":",e
        sys.exit(1)

def tryRunApp():
    try:
        global failNum
        global passNum
        result = "PASS"
        message = ""
        print "Install APK ---------------->Start"
        instatus = commands.getstatusoutput("adb install *apk")
        if instatus[0] == 0:
            print "Install APK ---------------->O.K"
            print "Find Package in device ---------------->Start"
            pmstatus = commands.getstatusoutput("adb shell pm list packages |grep org.xwalk.test")
            if pmstatus[0] == 0:
                print "Find Package in device ---------------->O.K"
                print "Launch APK ---------------->Start"
                launchstatus = commands.getstatusoutput("adb shell am start -n org.xwalk.test/.testActivity")
                if launchstatus[0] != 0:
                    print "Launch APK ---------------->Error"
                    os.system("adb uninstall org.xwalk.test")
                    failNum = failNum + 1
                    result = "FAIL"
                    message = "launch app error"
                else:
                    print "Launch APK ---------------->O.K"
                    print "Stop APK ---------------->Start"
                    stopstatus = commands.getstatusoutput("adb shell am force-stop org.xwalk.test")
                    if stopstatus[0] == 0:
                        print "Stop APK ---------------->O.K"
                        print "Uninstall APK ---------------->Start"
                        unistatus = commands.getstatusoutput("adb uninstall org.xwalk.test")
                        if unistatus[0] == 0:
                            print "Uninstall APK ---------------->O.K"
                            passNum = passNum + 1
                        else:
                            print "Uninstall APK ---------------->Error"
                            failNum = failNum + 1
                            result = "FAIL"
                            message = "uninstall apk error"
                    else:
                        print "Stop APK ---------------->Error"
                        failNum = failNum + 1
                        result = "FAIL"
                        message = "stop apk error"
                        os.system("adb uninstall org.xwalk.test")
            else:
                print "Find Package in device ---------------->Error"
                os.system("adb uninstall org.xwalk.test")
                failNum = failNum + 1
                result = "FAIL"
                message = "can't find package in device"
        else:
            print "Install APK ---------------->Error"
            result = "FAIL"
            failNum = failNum + 1
            message = "install apk error"
        os.system("rm -rf *apk &>/dev/null")
        return result,message
    except Exception,e:
        print Exception,":",e
        print "Try run webapp ---------------->Error"
        sys.exit(1)

def genResultXml():
    try:
        print "Generate test.result.xml ---------------->Start"
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
        suite = SE(root, "suite", {"category":"Runtime_Core","launcher":"xwalk",\
        "name":"wrt-manifest-android-tests"})
        setPositive = SE(suite, "set", {"name":"positive","set_debug_msg":""})
        setNegitive = SE(suite, "set", {"name":"negitive","set_debug_msg":""})

        #testcase element
        for case in ResultList:
            setElement = setPositive
            if case["set"] == "negative":
                setElement = setNegitive
            pur = "Check if packaged web application can be installed/launched/uninstalled successfully"
            testcase = SE(setElement, "testcase", {"component":"Runtime Core",\
            "execution_type":"auto","id":case["id"],"purpose":pur,"result":case["result"]})
            desc = SE(testcase, "description")
            entry = Element("test_script_entry")
            entry.text = case["entry"].decode("utf-8")
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

        tree.write(ConstPath + "/report/wrt-manifest-android-tests.xml")
        updateXmlTitle(ConstPath + "/report/wrt-manifest-android-tests.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/testresult.xsl"?>\n<?xml-stylesheet type="text/xsl" href="testresult.xsl"?>\n')
        
        print "Generate test.result.xml ---------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Generate test.result.xml ---------------->Error"
        sys.exit(1)

def genSummaryXml():
    try:
        print "Generate summary.xml ---------------->Start"
        tree = ElementTree()
        root = Element("result_summary", {"plan_name":""})
        tree._setroot(root)
        env = SE(root,"environment",{"build_id":"","cts_version":"","device_id":"","device_model":"","device_name":"","host":"","resolution":"","screen_size":"","manufacturer":""})
        summary = SE(root, "summary")
        startTime = SE(summary, "start_at")
        endTime = SE(summary, "end_at")
        startTime.text = Start
        endTime.text = End
        suite = SE(root, "suite", {"name":"wrt-manifest-android-tests"})
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
        print "Generate summary.xml ---------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Generate summary.xml ---------------->Error"
        sys.exit(1)

def devicesConform():
    try:
        deviceList = os.popen("adb devices").readlines()
        if len(deviceList) == 2:
            print "No test devices connected, Please attention"
            sys.exit(1)
    except Exception,e:
        print Exception,"Device Connect error:",e
        sys.exit(1)

def updateXmlTitle(fp,title):
    fobj = open(fp, "r+")
    lines = fobj.readlines()
    fobj.seek(0)
    fobj.truncate()
    lines.insert(0,title)
    fobj.writelines(lines)
    fobj.close()

def main():
    try:
        global End
        global Flag
        os.system("rm -rf " + ConstPath + "/allpairs/negative/*~ &>/dev/null")
        os.system("rm -rf " + ConstPath + "/allpairs/positive/*~ &>/dev/null")
        os.system("rm -rf " + ConstPath + "/allpairs/case*txt &>/dev/null")
        os.system("rm -rf " + ConstPath + "/report/manifest* &>/dev/null")
        os.system("rm -rf " + ConstPath + "/self &>/dev/null")
        os.system("rm -rf " + ConstPath + "/tcs &>/dev/null")
        os.system("mkdir -p " + ConstPath + "/self")
        os.system("mkdir -p " + ConstPath + "/tcs")
        devicesConform()

        #positive case
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
        os.system("rm -rf " + ConstPath + "/tcs &>/dev/null")

if __name__ == "__main__":
    main()
