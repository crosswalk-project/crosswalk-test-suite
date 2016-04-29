#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Yun, Liu<yunx.liu@intel.com>

import sys, os, os.path, shutil, time
import comm, glob
import thread, Queue

import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

totalNum = 0
result = ""
comm.setUp()

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

def genmanifest(caseInput, flag):
    try:
        manifestLog = open(comm.ConstPath + "/report/manifest_"+ flag + ".txt", 'a+')

        caseIn = open(caseInput)
        line = caseIn.readline().strip('\n\r')
        sectionList = line.split("\t")

        global totalNum 
        for line in caseIn:
            totalNum = totalNum + 1
            caseValue = ""
            print "##########"
            print "Case" + str(totalNum) + " :"
            print "Generate manifest.json ---------------->Start"
            items = line.strip('\n\r').split("\t")
            caseDir = comm.ConstPath + "/tcs/manifest" + str(totalNum) + "-" + flag 
            if not os.path.exists(caseDir):
                os.mkdir(caseDir)
            fp = open(caseDir + "/manifest.json", 'w+')
            for i in range(len(items)):
                items[i] = items[i].replace("null","")
                if sectionList[i] not in ("icons", "icon", "xwalk_launch_screen", "xwalk_permissions", "xwalk_target_platforms", "xwalk_app_version"):
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
            comm.doCopy(comm.ConstPath + "/resource", caseDir)
            fp_manifest = open(caseDir + "/manifest.json", 'r')
            fp_icon = fp_manifest.read().strip("\n\t")
            if "icons" not in fp_icon:
                shutil.rmtree(caseDir + "/icon/")
            if "icons" in fp_icon and "icon.bmp" not in fp_icon:
                os.remove(caseDir + "/icon/icon.bmp")
            if "icons" in fp_icon and "icon.gif" not in fp_icon:
                os.remove(caseDir + "/icon/icon.gif")
            if "icons" in fp_icon and "icon.jpg" not in fp_icon:
                os.remove(caseDir + "/icon/icon.jpg")
            if "icons" in fp_icon and "icon.png" not in fp_icon:
                os.remove(caseDir + "/icon/icon.png")
            if "icons" in fp_icon and "icon.webp" not in fp_icon:
                os.remove(caseDir + "/icon/icon.webp")
            if "icons" in fp_icon and ".crosswalk.ico" not in fp_icon:
                os.remove(caseDir + "/icon/.crosswalk.ico")
            if os.path.exists(caseDir + "/icon/") and len(os.listdir(caseDir + "/icon/")) == 0:
                shutil.rmtree(caseDir + "/icon/")
            if ".index.html" not in fp_icon:
                os.remove(caseDir + "/.index.html")
            if "index.html" not in fp_icon:
                os.remove(caseDir + "/index.html")
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


def processTest(seedIn, flag):
    try:
        fileName = os.path.basename(seedIn)
        name = os.path.splitext(fileName)[0]
        print "Input Seed : " + fileName
        print "Excute " + flag + " cases ------------------------->Start"
        row = 0
        sectionList = []

        fp = open(seedIn)
        for line in fp:
            items = line.strip('\n\r').split(":")
            sectionName = items[0].split("-")[0]
            if sectionName not in sectionList:
                sectionList.append(sectionName)
            inputTxt = open(comm.ConstPath + "/self/" + sectionName + "_input.txt", "a+")
            inputTxt.write(line)
            inputTxt.close()
        fp.close()

        for section in sectionList:
            caseline = ""
            counters = lineCount(comm.ConstPath + "/self/" + section + "_input.txt")
            if counters >= 2:
                lists = [[] for m in range(counters)]
                inputTxt = open(comm.ConstPath + "/self/" + section + "_input.txt", 'r+')
                for line in inputTxt:
                    items = line.strip('\n\r').split(":")
                    values = ":".join(items[1:]).split(",")
                    lists[row].extend(values)
                    row = row + 1
                pairs = all_pairs(lists)
                inputTxt.close()
                outTxt = open(comm.ConstPath + "/self/" + section + "_output.txt", 'a+')
                for e, v in enumerate(pairs):
                    for c in range(len(v)):
                        caseline = caseline + v[c] + ","
                outTxt.write(section + ":" + caseline[:-1] + "\n")
                outTxt.close()
            else:
                shutil.copy(comm.ConstPath + "/self/" + section + "_input.txt", comm.ConstPath + "/self/" + section + "_output.txt")

        #1*********XX_output.txt -> selfcomb.txt
            #os.remove(ConstPath + "/allpairs/selfcomb.txt")
            genSelfcom(comm.ConstPath + "/self/" + section + "_output.txt", comm.ConstPath + "/allpairs/selfcomb.txt")

        #2*********selfcomb.txt -> caseXX.txt
        genCases(comm.ConstPath + "/allpairs/selfcomb.txt", name, flag)

        #3*********output -> manifest.json
        genmanifest(comm.ConstPath + "/allpairs/" + name + "_case.txt", flag)

        print "Excute " + flag + " cases ------------------------->O.K"
        print
    except Exception,e:
        print "Excute " + flag + " cases ------------------------->Error"
        print Exception,":",e
        sys.exit(1)


def genCases(selfcomb, name, flag):
    try:
        print "Genarate " + flag + " case.txt file ---------------->Start"
        caseFile = open(comm.ConstPath + "/allpairs/" + name + "_case.txt", 'w+')
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


def sourceInit():
    try:
        if os.path.exists(comm.ConstPath + "/tcs"):
            shutil.rmtree(comm.ConstPath + "/tcs")
        if os.path.exists(comm.ConstPath + "/apks"):
            shutil.rmtree(comm.ConstPath + "/apks")
        if not os.path.exists(comm.ConstPath + "/allpairs/deb/negative/"):
            os.mkdir(comm.ConstPath + "/allpairs/deb/negative")
        if not os.path.exists(comm.ConstPath + "/allpairs/ios/negative/"):
            os.mkdir(comm.ConstPath + "/allpairs/ios/negative")
        if os.path.exists(comm.ConstPath + "/report"):
            shutil.rmtree(comm.ConstPath + "/report")
            if os.path.exists(comm.ConstPath + "/tests.py"):
                os.remove(comm.ConstPath + "/tests.py")
            os.mkdir(comm.ConstPath + "/tcs")
            os.mkdir(comm.ConstPath + "/report")
            txt_list = glob.glob(comm.ConstPath + "/allpairs/*.txt")
            for item in txt_list:
                os.remove(item)
        else:
            os.mkdir(comm.ConstPath + "/tcs")
            os.mkdir(comm.ConstPath + "/report")

        Start = time.strftime("%Y-%m-%d %H:%M:%S")
        print "Start time: " + Start
        for flag in ["positive", "negative"]:
            for seedIn in os.listdir(comm.ConstPath + "/allpairs/common/" + flag + "/"):
                if os.path.exists(comm.ConstPath + "/self"):
                    txt_list = glob.glob(comm.ConstPath + "/self/*.txt")
                    for item in txt_list:
                        os.remove(item)
                else:
                    os.mkdir(comm.ConstPath + "/self")
                
                if os.path.exists(comm.ConstPath + "/allpairs/selfcomb.txt"):
                    os.remove(comm.ConstPath + "/allpairs/selfcomb.txt")
                processTest(comm.ConstPath + "/allpairs/common/" + flag + "/" + seedIn, flag)
            for seedIn in os.listdir(comm.ConstPath + "/allpairs/" + comm.PLATFORMS + "/" + flag + "/"):
                if os.path.exists(comm.ConstPath + "/self"):
                    txt_list = glob.glob(comm.ConstPath + "/self/*.txt")
                    for item in txt_list:
                        os.remove(item)
                else:
                    os.mkdir(comm.ConstPath + "/self")
                
                if os.path.exists(comm.ConstPath + "/allpairs/selfcomb.txt"):
                    os.remove(comm.ConstPath + "/allpairs/selfcomb.txt")
                processTest(comm.ConstPath + "/allpairs/" + comm.PLATFORMS + "/" + flag + "/" + seedIn, flag)
        End = time.strftime("%Y-%m-%d %H:%M:%S")
        print "End time: " + End
    except Exception,e:
        print Exception,":",e
        sys.exit(1)

if __name__ == "__main__":
    sourceInit()
