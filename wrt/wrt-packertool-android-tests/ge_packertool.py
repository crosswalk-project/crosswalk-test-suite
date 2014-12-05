#!/usr/bin/env python
import sys, os, os.path, time, shutil
import commands,glob

import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2


SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
ARCH = "x86"
totalNum = 0

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


def processTest(seedIn, flag):
    try:
        fileName = os.path.basename(seedIn)
        name = os.path.splitext(fileName)[0]
        print "Input Seed :" + fileName
        print "Excute " + flag + " cases ------------------------->Start"
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
                    values = ":".join(items[1:]).split(",")
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
        genCases(ConstPath + "/allpairs/selfcomb.txt", name, flag)

        #3*********output -> command
        genCmd(ConstPath + "/allpairs/" + name + "_case.txt", flag)

        print "Excute " + flag + " cases ------------------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Excute " + flag + " cases ------------------------->Error"
        sys.exit(1)

def genCases(selfcomb, name, flag):
    try:
        print "Genarate " + flag + " case.txt file ---------------->Start"
        caseFile = open(ConstPath + "/allpairs/" + name + "_case.txt", 'w+')
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

def genCmd(caseInput, flag):
    try:
        global ARCH, totalNum

        print "Excute cases ------------------------->Start"
        packageLog = open(ConstPath + "/report/packertool_"+ flag + ".txt", 'a+')
        caseIn = open(caseInput)
        pgName = open(ConstPath + "/report/pgName.txt", 'a+')
        targetDir = open(ConstPath + "/report/targetDir.txt", 'a+')
        line = caseIn.readline().strip('\n\r')
        sectionList = line.split("\t")

        fp = open(ConstPath + "/arch.txt")
        if fp.read().strip("\n\t") != "x86":
            ARCH = "arm"
        fp.close()
        
        if not os.path.exists(ConstPath + "/tcs/" + ARCH):
            if ARCH in os.listdir(ConstPath + "/tcs"):
                shutil.rmtree(ConstPath + "/tcs/" + ARCH)
                os.mkdir(ConstPath + "/tcs/" + ARCH)
            else:
                os.mkdir(ConstPath + "/tcs/" + ARCH)

        for line in caseIn:
            message = ""
            totalNum = totalNum + 1
            
            caseDir = ConstPath + "/tcs/" + ARCH + "/cmd" + str(totalNum) + "-" + flag 
            if not os.path.exists(caseDir):
                os.mkdir(caseDir)
            fp = open(caseDir + "/cmd.txt", 'w+')

            items = line.strip("\t\n").split("\t")
            command = "python make_apk.py "
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

            if not "arch" in sectionList:
                command = command + " --arch=" + ARCH

            if "target-dir" in sectionList:
                dirIndex = sectionList.index("target-dir")
                if items[dirIndex] != "DEFAULT":
                    direc = items[dirIndex]
                    targetDir.write("cmd" + str(totalNum) + "-" + flag + "\t" + direc + "\n")
                else:
                    direc = "./"
            else:
                direc = "./"

            if direc.startswith("/"):
                apkDir = direc
            else:
                apkDir = ConstPath + "/tools/crosswalk/" + direc
            os.system("rm -rf " + apkDir + "/*.apk")

            if "name" in sectionList:
                index = sectionList.index("name")
                name = items[index]

            if "package" in sectionList:
                index = sectionList.index("package")
                package = items[index]
                pgName.write("cmd" + str(totalNum) + "-" + flag + "\t" + package + "\n")

            packageLog.write("Packertool" + str(totalNum) + "\n--------------------------------\n" + command + "\n--------------------------------\n")
            fp.write(command)
            fp.close()
            print "##########"
            print "Case" + str(totalNum) + " :"
            print "Packer Tool Command:"
            print command
            
        packageLog.close()
        caseIn.close()
        pgName.close()
        print "Excute cases ------------------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Execute case ---------------->Error"
        sys.exit(1)

def sourceInit():
    try:
        if os.path.exists(ConstPath + "/tcs") or os.path.exists(ConstPath + "/apks") or os.path.exists(ConstPath + "/report"):
            try:
                shutil.rmtree(ConstPath + "/tcs")
                shutil.rmtree(ConstPath + "/apks")
                shutil.rmtree(ConstPath + "/report")
            except Exception,e:
                os.system("rm -rf " + ConstPath + "/tcs/* &>/dev/null")
                os.system("rm -rf " + ConstPath + "/apks/* &>/dev/null")
                os.system("rm -rf " + ConstPath + "/report/* &>/dev/null")
                #os.system("rm -rf " + ConstPath + "/report &>/dev/null")
            if os.path.exists(ConstPath + "/tests.py"):
                os.remove(ConstPath + "/tests.py")
            os.mkdir(ConstPath + "/tcs")
            os.mkdir(ConstPath + "/report")
            txt_list = glob.glob(ConstPath + "/allpairs/*.txt")
            for item in txt_list:
                os.remove(item)
        else:
            os.mkdir(ConstPath + "/tcs")
            os.mkdir(ConstPath + "/report")
        
        
        Start = time.strftime("%Y-%m-%d %H:%M:%S")
        print "Start time: " + Start
        for flag in ["positive", "negative"]:
            for seedIn in os.listdir(ConstPath + "/allpairs/" + flag + "/"):
                if os.path.exists(ConstPath + "/self"):
                    txt_list = glob.glob(ConstPath + "/self/*.txt")
                    for item in txt_list:
                        os.remove(item)
                else:
                    os.mkdir(ConstPath + "/self")
                
                if os.path.exists(ConstPath + "/allpairs/selfcomb.txt"):
                    try:
                        os.remove(ConstPath + "/allpairs/selfcomb.txt")
                    except Exception,e:
                        os.system("rm -rf " + ConstPath + "/allpairs/selfcomb.txt &>/dev/null")

                processTest(ConstPath + "/allpairs/" + flag + "/" + seedIn, flag)
        End = time.strftime("%Y-%m-%d %H:%M:%S")
        print "End time: " + End
    except Exception,e:
        print Exception,":",e
        sys.exit(1)


if __name__=="__main__":
    sourceInit()
