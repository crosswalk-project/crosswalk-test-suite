import sys, os, os.path, shutil, time
import commands
import thread, Queue

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement as SE
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

ConstPath = os.environ['HOME'] + "/tct/opt/wrt-manifest-android-tests"
Devices = []

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

def caseExecute(caseInput, device, resultList, flag, summaryList):
    try:
        totalNum = summaryList["TOTAL"]
        failNum = summaryList["FAIL"]
        passNum = summaryList["PASS"]

        manifestLog = open(ConstPath + "/device_" + device + "/report/manifest_"+ flag + ".txt", 'a+')

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
            caseDir = ConstPath + "/device_" + device + "/tcs/manifest" + str(totalNum)
            os.mkdir(caseDir)
            fp = open(caseDir + "/manifest.json", 'w+')
            for i in range(len(items)):
                items[i] = items[i].replace("null","")
                if sectionList[i] not in ("icons", "icon", "xwalk_launch_screen", "xwalk_permissions", "display"):
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
            updateConfigXml(ConstPath + "/device_" + device + "/tcs/manifest" + str(totalNum) + "/config.xml", "manifest" + str(totalNum))
            #genarate package and execute
            os.chdir(ConstPath + "/device_" + device + "/tools/crosswalk/")
            data = {"id":"","result":"","entry":"","message":"","start":"","end":"","set":""}
            caseStart = time.strftime("%Y-%m-%d %H:%M:%S")
            status, info = genPackage(caseDir)
            message = message + "Packer Log:\n" + info + "\n"
            if flag == "negative":
                if status == 0:
                    message = message + "Generate apk succeed\n"
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    message = message + "Generate apk failed\n"
                    result = "PASS"
                    passNum = passNum + 1
            else:
                if status != 0:
                    message = message + "Generate apk failed\n"
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    result, feedback = tryRunApp(device)
                    if result == "PASS":
                        passNum = passNum + 1
                    else:
                        failNum = failNum + 1
                    message = message + feedback + "\n"
            caseEnd = time.strftime("%Y-%m-%d %H:%M:%S")
            data["id"] = "manifest" + str(totalNum)
            data["result"] = result
            data["entry"] = caseValue
            data["message"] = message
            data["start"] = caseStart
            data["end"] = caseEnd
            data["set"] = flag
            resultList.append(data)
            print "Case Result :" + result
            print "##########"
            os.system("rm -rf " + ConstPath + "/device_" + device + "/tcs/manifest" + str(totalNum) + "&>/dev/null")
        summaryList["TOTAL"] = totalNum
        summaryList["FAIL"] = failNum
        summaryList["PASS"] = passNum
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

def processMain(device, queue):
    queue.get()
    resultList = []
    summaryList = {"PASS":0,"FAIL":0,"TOTAL":0}
    totalNum = 0
    Start = time.strftime("%Y-%m-%d %H:%M:%S")
    for flag in ["positive", "negative"]:
        for seedIn in os.listdir(ConstPath + "/device_" + device + "/allpairs/" + flag + "/"):
            os.system("rm -rf " + ConstPath + "/device_" + device + "/self &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/allpairs/selfcomb* &>/dev/null")
            os.system("mkdir -p " + ConstPath + "/device_" + device + "/self")
            processTest(ConstPath + "/device_" + device + "/allpairs/" + flag + "/" + seedIn, device, flag, resultList, summaryList)
    End = time.strftime("%Y-%m-%d %H:%M:%S")
    genResultXml(resultList, device, Start, End)
    genSummaryXml(summaryList, device, Start, End)
    queue.task_done()
    #thread.exit_thread()

def processTest(seedIn, device, flag, resultList, summaryList):
    try:
        fileName = os.path.basename(seedIn)
        name = os.path.splitext(fileName)[0]
        print "Input Seed : " + fileName
        print "Test Device : " + device
        print "Excute " + flag + " cases ------------------------->Start"
        row = 0
        sectionList = []

        fp = open(seedIn)
        for line in fp:
            items = line.strip('\n\r').split(":")
            sectionName = items[0].split("-")[0]
            if sectionName not in sectionList:
                sectionList.append(sectionName)
            inputTxt = open(ConstPath + "/device_" + device + "/self/" + sectionName + "_input.txt", "a+")
            inputTxt.write(line)
            inputTxt.close()
        fp.close()

        for section in sectionList:
            caseline = ""
            counters = lineCount(ConstPath + "/device_" + device + "/self/" + section + "_input.txt")
            if counters >= 2:
                lists = [[] for m in range(counters)]
                inputTxt = open(ConstPath + "/device_" + device + "/self/" + section + "_input.txt", 'r+')
                for line in inputTxt:
                    items = line.strip('\n\r').split(":")
                    values = ":".join(items[1:]).split(",")
                    lists[row].extend(values)
                    row = row + 1
                pairs = all_pairs(lists)
                inputTxt.close()
                outTxt = open(ConstPath + "/device_" + device + "/self/" + section + "_output.txt", 'a+')
                for e, v in enumerate(pairs):
                    for c in range(len(v)):
                        caseline = caseline + v[c] + ","
                outTxt.write(section + ":" + caseline[:-1] + "\n")
                outTxt.close()
            else:
                shutil.copy(ConstPath + "/device_" + device + "/self/" + section + "_input.txt", ConstPath + "/device_" + device + "/self/" + section + "_output.txt")

        #1*********XX_output.txt -> selfcomb.txt
            genSelfcom(ConstPath + "/device_" + device + "/self/" + section + "_output.txt", ConstPath + "/device_" + device + "/allpairs/selfcomb.txt")

        #2*********selfcomb.txt -> caseXX.txt
        genCases(ConstPath + "/device_" + device + "/allpairs/selfcomb.txt", name, device, flag)

        #3*********output -> manifest.json
        caseExecute(ConstPath + "/device_" + device + "/allpairs/" + name + "_case.txt", device, resultList, flag, summaryList)

        print "Excute " + flag + " cases ------------------------->O.K"
        print
    except Exception,e:
        print "Excute " + flag + " cases ------------------------->Error"
        print Exception,":",e
        sys.exit(1)

def genPackage(direc):
    try:
        print "Generate APK ---------------->Start"
        toolstatus = commands.getstatusoutput("python make_apk.py")[0]
        if toolstatus != 0:
            print "Crosswalk Binary is not ready, Please attention"
            sys.exit(1)
        cmd ="python make_apk.py --package=org.xwalk.test --arch=x86 --manifest="
        manifestPath = direc + "/manifest.json"
        status, message = commands.getstatusoutput(cmd + manifestPath)
        if status != 0:
            print "Generate APK ---------------->Error"
        else:
            print "Generate APK ---------------->O.K"
        return status, message
    except Exception,e:
        print Exception,":",e
        sys.exit(1)

def genCases(selfcomb, name, device, flag):
    try:
        print "Genarate " + flag + " case.txt file ---------------->Start"
        caseFile = open(ConstPath + "/device_" + device + "/allpairs/" + name + "_case.txt", 'w+')
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
        print "Genarate " + flag + " case.txt file ---------------->O.k"
    except Exception,e:
        print "Generate " + flag + " case.txt file ---------------->Error"
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

def tryRunApp(device):
    try:
        result = "PASS"
        message = ""
        print "Install APK ---------------->Start"
        instatus = commands.getstatusoutput("adb -s " + device + " install *apk")
        if instatus[0] == 0:
            print "Install APK ---------------->O.K"
            message = message + "Install apk succeed\n"
            print "Find Package in device ---------------->Start"
            pmstatus = commands.getstatusoutput("adb -s " + device + " shell pm list packages |grep org.xwalk.test")
            if pmstatus[0] == 0:
                print "Find Package in device ---------------->O.K"
                message = message + "Find package in device succeed\n"
                print "Launch APK ---------------->Start"
                launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n org.xwalk.test/.TestActivity")
                if launchstatus[0] != 0:
                    print "Launch APK ---------------->Error"
                    message = message + "Launch apk failed\n"
                    os.system("adb -s " + device + " uninstall org.xwalk.test")
                    result = "FAIL"
                else:
                    print "Launch APK ---------------->O.K"
                    message = message + "Launch apk succeed\n"
                    print "Stop APK ---------------->Start"
                    stopstatus = commands.getstatusoutput("adb -s " + device + " shell am force-stop org.xwalk.test")
                    if stopstatus[0] == 0:
                        print "Stop APK ---------------->O.K"
                        message = message + "Stop apk succeed\n"
                        print "Uninstall APK ---------------->Start"
                        unistatus = commands.getstatusoutput("adb -s " + device + " uninstall org.xwalk.test")
                        if unistatus[0] == 0:
                            print "Uninstall APK ---------------->O.K"
                            message = message + "Uninstall apk succeed\n"
                        else:
                            print "Uninstall APK ---------------->Error"
                            message = message + "Uninstall apk failed\n"
                            result = "FAIL"
                    else:
                        print "Stop APK ---------------->Error"
                        result = "FAIL"
                        message = message + "Stop apk failed\n"
                        os.system("adb -s " + device + " uninstall org.xwalk.test")
            else:
                print "Find Package in device ---------------->Error"
                message = message + "Find package in device failed\n"
                os.system("adb -s " + device + " uninstall org.xwalk.test")
                result = "FAIL"
        else:
            print "Install APK ---------------->Error"
            result = "FAIL"
            message = message + "Install apk failed\n"
        os.system("rm -rf *apk &>/dev/null")
        return result,message
    except Exception,e:
        print Exception,":",e
        print "Try run webapp ---------------->Error"
        sys.exit(1)

def genResultXml(resultList, device, Start, End):
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
        setNegitive = SE(suite, "set", {"name":"negative","set_debug_msg":""})

        #testcase element
        for case in resultList:
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
            stdOut = SE(resultInfo, "stdout")
            if case["result"] == "FAIL":
                stdOut.text = "[message]\n" + case["message"].decode("utf-8")
            else:
                stdOut.text = "[message]"
            SE(resultInfo, "stderr")

        tree.write(ConstPath + "/device_" + device + "/report/wrt-manifest-android-tests.xml")
        updateXmlTitle(ConstPath + "/device_" + device + "/report/wrt-manifest-android-tests.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/testresult.xsl"?>\n<?xml-stylesheet type="text/xsl" href="testresult.xsl"?>\n')

        print "Generate test.result.xml ---------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Generate test.result.xml ---------------->Error"
        sys.exit(1)

def genSummaryXml(summaryList, device, Start, End):
    try:
        print "Generate summary.xml ---------------->Start"
        passNum = summaryList["PASS"]
        failNum = summaryList["FAIL"]
        totalNum = summaryList["TOTAL"]
        tree = ElementTree()
        root = Element("result_summary", {"plan_name":""})
        tree._setroot(root)
        env = SE(root,"environment",{"build_id":"","cts_version":"","device_id":"","device_model":"","device_name":"","host":"","resolution":"","screen_size":"","manufacturer":""})
        env.set("device_id", device)
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
        tree.write(ConstPath + "/device_" + device + "/report/summary.xml")
        updateXmlTitle(ConstPath + "/device_" + device + "/report/summary.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/summary.xsl"?>\n')
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

def sourceInit(Devices):
    #os.system("rm -rf " + ConstPath + "/device_* " + "&>/dev/null")
    for device in Devices:
        device = device.strip("\n\t")
        if os.path.exists(ConstPath + "/device_" + device):
            os.system("rm -rf " + ConstPath + "/device_" + device + "/allpairs/*txt &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/report/summary.xml &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/report/*manifest* &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/allpairs/negative/* &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/allpairs/positive/* &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/allpairs/tcs/* &>/dev/null")
        else:
            os.system("mkdir -p " + ConstPath + "/device_" + device)
            os.system("cp -rf "+ ConstPath + "/report/ "+ ConstPath + "/device_" + device + "/")
            os.system("mkdir -p " + ConstPath + "/device_" + device + "/tcs")
            os.system("mkdir -p " + ConstPath + "/device_" + device + "/tools")
            os.system("cp -rf " + ConstPath + "/tools/crosswalk " + ConstPath + "/device_" + device + "/tools")
            os.system("mkdir -p " + ConstPath + "/device_" + device + "/allpairs/negative")
            os.system("mkdir -p " + ConstPath + "/device_" + device + "/allpairs/positive")

def seedDistribute(Devices):
    cDevices = len(Devices)
    fp = os.popen("find " + ConstPath + "/allpairs/ -name '*txt' |awk -F 'allpairs' '{print $2}'")
    lines = fp.readlines()
    fp.close()
    txtCount = len(lines)
    for index in range(txtCount):
        deviceIndex = index % cDevices
        device = Devices[deviceIndex]
        line = lines[index].strip("\n\t")
        os.system("cp " + ConstPath + "/allpairs" + line + " " + ConstPath + "/device_" + device + "/allpairs" + line)

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
        global Devices
        DeviceQueue = Queue.Queue()

        devicesConform()
        if "DEVICE_ID" in os.environ:
            for device in os.environ["DEVICE_ID"].split(","):
                Devices.append(device)
                DeviceQueue.put(device)
        else:
            print "Can't read DEVICE_ID in os.environ"
            sys.exit(1)

        sourceInit(Devices)
        seedDistribute(Devices)
        for device in Devices:
            thread.start_new_thread(processMain, (device,DeviceQueue))
        DeviceQueue.join()
    except Exception,e:
        print Exception,":",e
        sys.exit(1)

if __name__ == "__main__":
    main()
