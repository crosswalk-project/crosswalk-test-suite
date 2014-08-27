import sys, os, os.path, time, shutil
import commands, Queue, thread

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement as SE
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

Devices = []
ConstPath = os.environ['HOME'] + "/tct/opt/wrt-packertool-android-tests"

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

def processMain(device, queue):
    queue.get()
    resultList = []
    summaryList = {"PASS":0,"FAIL":0,"TOTAL":0}
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

def processTest(seedIn, device, flag, resultList, summaryList):
    try:
        fileName = os.path.basename(seedIn)
        name = os.path.splitext(fileName)[0]
        print "Input Seed :" + fileName
        print "Test Device : " + device
        print "Excute " + flag + " cases ------------------------->Start"
        row = 0
        sectionList = []

        fp = open(seedIn)
        for line in fp:
            items = line.strip('\n\r').split(":")
            sectionName = items[0].split("--")[0]
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
                inputTxt = open(ConstPath + "/device_" + device + "/self/" + section + "_input.txt")
                for line in inputTxt:
                    items = line.strip('\n\r').split(":")
                    values = ":".join(items[1:]).split(",")
                    lists[row].extend(values)
                    row = row + 1
                inputTxt.close()
                pairs = all_pairs(lists)
                outTxt = open(ConstPath + "/device_" + device + "/self/" + section + "_output.txt", 'w+')
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
    except Exception,e:
        print Exception,":",e
        print "Excute " + flag + " cases ------------------------->Error"
        sys.exit(1)

def genCases(selfcomb, name, device, flag):
    try:
        print "Genarate " + flag + " case.txt file ---------------->Start"
        caseFile = open(ConstPath + "/device_" + device + "/allpairs/" + name + "_case.txt", 'w+')
        names = ""
        row = 0
        fobj = open(selfcomb)
        for line in fobj:
            items = line.strip('\n\r').split(":")
            names = names + items[0] + "\t"
        caseFile.write(names.rstrip("\t") + "\n")
        counters = lineCount(selfcomb)
        fobj.seek(0)
        if counters >= 2:
            lists = [[] for m in range(counters)]

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
        else:
            line = fobj.readline()
            fobj.close()
            values = line.strip("\t\n").split(":")[1:]
            for case in ":".join(values).split(","):
                caseFile.write(case + "\n")
        caseFile.close()
        print "Genarate " + flag + " case.txt file ---------------->O.k"
    except Exception,e:
        print "Generate " + flag + " case.txt file ---------------->Error"
        print Exception,":",e
        sys.exit(1)

def caseExecute(caseInput, device, resultList, flag, summaryList):
    try:
        totalNum = summaryList["TOTAL"]
        failNum = summaryList["FAIL"]
        passNum = summaryList["PASS"]

        print "Excute cases ------------------------->Start"
        manifestLog = open(ConstPath + "/device_" + device + "/report/packertool_"+ flag + ".txt", 'a+')
        caseIn = open(caseInput)
        line = caseIn.readline().strip('\n\r')
        sectionList = line.split("\t")

        os.chdir(ConstPath + "/device_" + device + "/tools/crosswalk")
        toolstatus = commands.getstatusoutput("python make_apk.py")
        if toolstatus[0] != 0:
            print "Crosswalk Binary is not ready, Please attention"
            sys.exit(1)

        for line in caseIn:
            message = ""
            totalNum = totalNum + 1
            items = line.strip("\t\n").split("\t")
            command = "python make_apk.py "
            data = {"id":"","result":"","entry":"","start":"","end":"","set":"","message":""}
            data["start"] = time.strftime("%Y-%m-%d %H:%M:%S")
            for i in range(len(sectionList)):
                if items[i] == "DEFAULT":
                    continue
                elif items[i] == "NULL":
                    command = command + "--" + sectionList[i] + '=""'
                else:
                    items[i] = items[i].replace("000", " ")
                    items[i] = items[i].replace("comma", ",")
                    command = command + "--" + sectionList[i] + "=" + '"' + items[i] + '" '
            command = command.strip()

            if "target-dir" in sectionList:
                dirIndex = sectionList.index("target-dir")
                if items[dirIndex] != "DEFAULT":
                    direc = items[dirIndex]
                else:
                    direc = "./"
            else:
                direc = "./"
            if direc.startswith("/"):
                apkDir = direc
            else:
                apkDir = ConstPath + "/device_" + device + "/tools/crosswalk/" + direc

            if "name" in sectionList:
                index = sectionList.index("name")
                name = items[index]

            if "package" in sectionList:
                index = sectionList.index("package")
                package = items[index]

            manifestLog.write("Packertool" + str(totalNum) + "\n--------------------------------\n" + command + "\n--------------------------------\n")
            print "##########"
            print "Case" + str(totalNum) + " :"
            print "Packer Tool Command:"
            print command
            print "Genarate APK ---------------->Start"
            packstatus = commands.getstatusoutput(command)
            message = message + "Packer Log:\n" + packstatus[1] + "\n"
            if flag == "negative":
                if packstatus[0] == 0:
                    print "Genarate APK ---------------->O.K"
                    message = message + "Generate apk succeed\n"
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    print "Genarate APK ---------------->Error"
                    message = message + "Generate apk failed\n"
                    result = "PASS"
                    passNum = passNum + 1
            else:
                if packstatus[0] != 0:
                    print "Genarate APK ---------------->Error"
                    message = message + "Generate apk failed\n"
                    result = "FAIL"
                    failNum = failNum + 1
                else:
                    print "Genarate APK ---------------->O.K"
                    message = message + "Generate apk succeed\n"
                    result,feedback = tryRunApp(name, package, device, apkDir)
                    if result == "PASS":
                        passNum = passNum + 1
                    else:
                        failNum = failNum + 1
                    message = message + feedback + "\n"
            data["end"] = time.strftime("%Y-%m-%d %H:%M:%S")
            data["id"] = "Packertool" + str(totalNum)
            data["result"] = result
            data["entry"] = command
            data["set"] = flag
            data["message"] = message
            resultList.append(data)
            os.system("rm -rf " + apkDir + "/*apk")
            print "Case Result :",result
            print "##########"
        summaryList["TOTAL"] = totalNum
        summaryList["FAIL"] = failNum
        summaryList["PASS"] = passNum
        manifestLog.close()
        caseIn.close()
        print "Excute cases ------------------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Execute case ---------------->Error"
        sys.exit(1)

def tryRunApp(name, package, device, apkDir):
    try:
        result = "PASS"
        message = ""
        print "Install APK ---------------->Start"
        androidName = package.split(".")[-1].split("_")
        acivityName = ''.join([i.capitalize() for i in androidName if i])
        instatus = commands.getstatusoutput("adb -s " + device + " install " + apkDir + "/*apk")
        if instatus[0] == 0:
            print "Install APK ---------------->O.K"
            message = message + "Install apk succeed\n"
            print "Find Package in device ---------------->Start"
            pmstatus = commands.getstatusoutput("adb -s " + device + " shell pm list packages |grep " + package)
            if pmstatus[0] == 0:
                print "Find Package in device ---------------->O.K"
                message = message + "Find package in device succeed\n"
                print "Launch APK ---------------->Start"
                launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n " + package + "/." + acivityName + "Activity")
                if launchstatus[0] != 0:
                    print "Launch APK ---------------->Error"
                    message = message + "Launch apk failed\n"
                    os.system("adb uninstall " + package)
                    result = "FAIL"
                else:
                    print "Launch APK ---------------->O.K"
                    message = message + "Launch apk succeed\n"
                    print "Stop APK ---------------->Start"
                    stopstatus = commands.getstatusoutput("adb -s " + device + " shell am force-stop " + package)
                    if stopstatus[0] == 0:
                        print "Stop APK ---------------->O.K"
                        message = message + "Stop apk succeed\n"
                        print "Uninstall APK ---------------->Start"
                        unistatus = commands.getstatusoutput("adb -s " + device + " uninstall " + package)
                        if unistatus[0] == 0:
                            print "Uninstall APK ---------------->O.K"
                            message = message + "Stop apk succeed\n"
                        else:
                            print "Uninstall APK ---------------->Error"
                            message = message + "Stop apk failed\n"
                            result = "FAIL"
                    else:
                        print "Stop APK ---------------->Error"
                        message = message + "Stop apk failed\n"
                        result = "FAIL"
                        os.system("adb -s " + device + " uninstall " + package)
            else:
                print "Find Package in device ---------------->Error"
                message = message + "Find package in device failed\n"
                os.system("adb -s " + device + " uninstall " + package)
                result = "FAIL"
        else:
            message = message + "Install apk failed\n"
            print "Install APK ---------------->Error"
            result = "FAIL"
        os.system("rm -rf " + apkDir + "/*apk" + "&>/dev/null")
        return result,message
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

def genResultXml(resultList, device, Start, End):
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
        "name":"wrt-packertool-android-tests"})
        setPositive = SE(suite, "set", {"name":"positive","set_debug_msg":""})
        setNegitive = SE(suite, "set", {"name":"negitive","set_debug_msg":""})

        #testcase element
        for case in resultList:
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
            stdOut = SE(resultInfo, "stdout")
            if case["result"] == "FAIL":
                stdOut.text = "[message]\n" + case["message"].decode("utf-8")
            else:
                stdOut.text = "[message]"
            SE(resultInfo, "stderr")

        tree.write(ConstPath + "/device_" + device + "/report/wrt-packertool-android-tests.xml")
        updateXmlTitle(ConstPath + "/device_" + device + "/report/wrt-packertool-android-tests.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./style/testresult.xsl"?>\n<?xml-stylesheet type="text/xsl" href="testresult.xsl"?>\n')

        print "Generate test.result.xml file ------------------------->O.K"
    except Exception,e:
        print Exception,"Generate test.result.xml error:",e

def genSummaryXml(summaryList, device, Start, End):
    try:
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
        suite = SE(root, "suite", {"name":"wrt-packertool-android-tests"})
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

def sourceInit(Devices):
    #os.system("rm -rf " + ConstPath + "/device_* " + "&>/dev/null")
    for device in Devices:
        device = device.strip("\n\t")
        if os.path.exists(ConstPath + "/device_" + device):
            os.system("rm -rf " + ConstPath + "/device_" + device + "/allpairs/*txt &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/report/summary.xml &>/dev/null")
            os.system("rm -rf " + ConstPath + "/device_" + device + "/report/*packertool* &>/dev/null")
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
            thread.start_new_thread(processMain, (device, DeviceQueue))
        DeviceQueue.join()
    except Exception,e:
        print Exception,":",e
        sys.exit(1)

if __name__=="__main__":
    main()
