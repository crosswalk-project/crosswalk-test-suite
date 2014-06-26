
import sys, os, itertools, shutil, getopt, re, time 
import const

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from datetime import *  
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

Manifest_Row = 0
Device_Ip = ""
Pack_Type = "xpk"

def do_Selfcom(self_combin_file,out_file):
    try:
        file = open(self_combin_file)
        allpairs_in = open(out_file,'a+')
        while 1:
            line = file.readline()
            if not line:
                break
            allpairs_in.writelines(line + "\n")
        file.close()
        allpairs_in.close()
        return
    except Exception,e: 
        print Exception,":",e 


def gen_Manifest_Json(output_file):
    try:
        global Manifest_Row 
        file = open(output_file)
        fp_manifest = open(const.path + "/manifest_all.txt",'w+')
        manifest="{\n  "
        name_list=[]
        get_self=""
        line = file.readline().strip('\n\r')
        items = line.split("	")
        counters = len(items)
        try:
            os.mkdir(const.path + "/tcs")
        except:
            print  "make tcs folder error"
        for i in items:
            name_list.append(i)
        while 1:
            line = file.readline()
            if not line:
                break
            line = line.strip('\n\r')
            items = line.split("	")
            counters = len(items)
            os.mkdir(const.path + "/tcs/manifest" + str(Manifest_Row+1))
            fp = open(const.path + "/tcs/manifest"+str(Manifest_Row+1) + "/manifest.json",'w')
            for i in range(0,len(items)):
              if ((name_list[i])!="icon" and (name_list[i])!="app"):
                    if (items[i].find("000")!=-1):
                        items[i] = items[i].replace("000"," ")
                        get_self = get_self + "\"" + name_list[i] + "\"" + " : " + "\"" +items[i].replace("null","") + "\",\n"
                    else:
                        get_self = get_self + "\"" + name_list[i].strip() + "\"" + " : " + "\""+items[i].replace("null","") + "\",\n"
              else:
                    items[i] = items[i].replace("comma",",")
                    get_self = get_self + "\"" + name_list[i] + "\"" + " : "+items[i].replace("null","") + ",\n" 
            get_self = "{\n" + get_self[:-2] + "\n}" 
            fp.writelines(get_self)
            print (get_self)
            fp_manifest.writelines("manifest" + str(Manifest_Row+1) + "\n--------------------------------\n" +
             get_self+"\n--------------------------------\n")
            Manifest_Row = Manifest_Row+1
            fp.close()
            get_self=""
            #beging copy folder
            app_Folder(const.path_tcs)
            get_Configxml(const.path_tcs + "/manifest" +str(Manifest_Row) + "/config.xml", "manifest" +str(Manifest_Row))
            #beging packing
            print "Manifest ------------------------->" + str(Manifest_Row)
            manifest_Packing("manifest" + str(Manifest_Row),Pack_Type)
            #launch the app
            launcher_WebApp(Pack_Type,str(Manifest_Row))
            do_Clear(const.path_tcs + "/manifest" +str(Manifest_Row))
        file.close()
        fp_manifest.close()
        return "Generate manifest.json O.K"
    except Exception,e: 
        print Exception,"------------------------->:",e 
        return "Generate manifest.json error"
        
def fileline_count(fp):
     return len(open(fp).readlines()) 


def del_Seed(in_file,order_count):
    try:
        caseline = "" 
        row = 0
        file = open(in_file)
        items = []
        self_file = []
        s_name = p_name = ""
        if (os.path.isdir("self")):
            shutil.rmtree("self")
        os.mkdir(const.path + "/self")
        while 1:
            p_name = s_name
            line = file.readline()
            if not line:
                break
            line = line.strip('\n\r')
            items = line.split(":")
            s_name = items[0].split("-")[0]
            if ((p_name!=s_name) and (p_name!="")):
                fp=open(const.path + "/self/" + s_name + "_input.txt",'a+')
                fp.writelines(line + "\n")
            else:
                fp= open(const.path + "/self/" + s_name + "_input.txt",'a+')
                fp.writelines(line + "\n")
            if (s_name!=p_name):
                self_file.append(s_name)
        fp.close()
        file.close()
        if (os.path.isfile(const.selfcomb_file)):
            os.remove(const.selfcomb_file)
        for i in range (0,len(self_file)):
            line_count = fileline_count(const.path + "/self/" + self_file[i] + "_input.txt")
            if (int(order_count) < line_count):
                line_count = order_count
            if (line_count >= 2):
                lists = [[] for m in range(line_count)]
                open_input_file = open(const.path + "/self/" + self_file[i] + "_input.txt",'a+')
                while 1:
                    line = open_input_file.readline()
                    if not line:
                        break
                    line = line.strip('\n\r')
                    items = line.split(":")
                    get_item= items[1].split(",")
                    for g in get_item:
                        lists[row].append(g)
                    row = row + 1
                input_pair = all_pairs( lists )
                open_input_file.close()
                output_pair = open(const.path + "/self/" + self_file[i] + "_output.txt",'a+')
                for e, v in enumerate(input_pair):
                      for c in range(0,len(v)):
                          caseline = caseline + v[c]
                      caseline = caseline  + ","
                output_pair.writelines(self_file[i] + ":" + caseline[:-1])
                output_pair.close()
            else:
                open_input_file = open(const.path + "/self/" + self_file[i] + "_input.txt",'r')
                output_pair = open(const.path + "/self/" + self_file[i] + "_output.txt",'a+')
                while 1:
                    line = open_input_file.readline()
                    if not line:
                        break
                    line = line.strip('\n\r')
                    output_pair.writelines(line)
                output_pair.close()
                open_input_file .close()
              
        #1*********input_seed -> selfcomb.txt
        # if more self combination, each self generate itself output file,finally all self_input generate one selfcomb.txt
            do_Selfcom(const.path + "/self/" + self_file[i] + "_output.txt",const.selfcomb_file)
        
        #2*********selfcomb -> output file  by allpairs
        print gen_selfcomb_File(const.selfcomb_file,order_count)

        #3*********output -> manifest.json
        print gen_Manifest_Json(const.output_file)
        return "Manifest.json output ------------------------->O.K"
    except Exception,e: 
        print Exception,":",e 
        return "Manifest.json output ------------------------->Error"

def gen_selfcomb_File(comb_file,order_count):
    try:
        os.system("rm ./allpairs/output.txt")
        open_output_file= open(const.output_file,'a+')
        caseline = "" 
        get_items = ""
        get_case = ""
        row = 0
        line_count = fileline_count(comb_file)
        if (line_count >= 2):
            lists = [[] for m in range(line_count)]
            open_input_file= open(comb_file)
            while 1:
                  line = open_input_file.readline()
                  if not line:
                        break
                  line = line.strip('\n\r')
                  items = line.split(":")
                  get_items = get_items + items[0].split("-")[0] + "\t"
            open_output_file.writelines(get_items.rstrip("\t") + "\n")
            open_input_file.close()
            open_input_file= open(comb_file)
            for i in range(0,len(lists)):
                    line = open_input_file.readline()
                    if not line:
                        break
                    line = line.strip('\n\r')
                    items = line.split(":")#items[0]=field;#item[1]=value
                    value = line[len(items[0])+1:]
                    get_item= value.split(",")
                    for g in get_item:
                        lists[row].append(g)
                    row = row + 1
                    print  lists
            input_pair = all_pairs( lists )
            for e, v in enumerate(input_pair):
                for c in range(0,len(v)):
                    get_case = get_case +  v[c]+"\t"
                open_output_file.writelines(get_case.rstrip("\t") + "\n")
                get_case=""  
            open_output_file.close()
        return "Generate selfcombination file ------------------------->O.K"
    except:
        return "Generate selfcombination file ------------------------->error"

def make_webapp_folder(sourceDir,targetDir):
    print "copy source file...."
    try:
        for file in os.listdir(targetDir):
            for fp in os.listdir(sourceDir):
                sourceFile = os.path.join(sourceDir, fp) 
                targetFile = os.path.join(targetDir, file) 
                #copy resource to the manifest
                if os.path.isfile(sourceFile):
                    shutil.copy(sourceFile, targetFile)
    except:
        print "manifest resource copy error"


def app_Folder(path_tcs):
    try:
        print "<-------------------------> Copy WebApp Resource ------------------------->"
        for file in os.listdir(path_tcs):
            copy_Files(const.path_resource,os.getcwd()+"/tcs/"+file)
        return "Webapp folder copy ------------------------->O.K",path_tcs
    except Exception,e: 
        print Exception,":",e 
        return "Webapp folder copy ------------------------->error",path_tcs

def copy_Files(sourceDir, targetDir):
    try:
        copyFileCounts = 0
        for f in os.listdir(sourceDir):  
            sourceF = os.path.join(sourceDir, f)  
            targetF = os.path.join(targetDir, f)  
            if os.path.isfile(sourceF):  
                #create folder 
                if not os.path.exists(targetDir): 
                    os.makedirs(targetDir)  
                copyFileCounts = copyFileCounts + 1  
                #if not exist to copy
                if not os.path.exists(targetF):  
                    #copy file
                    open(targetF, "wb").write(open(sourceF, "rb").read())  
                else:  
                    print ("file exist do not copy")  
            if os.path.isdir(sourceF):
                copy_Files(sourceF, targetF)  
        return "Copy File O.k",sourceDir,"------------------------->", targetDir
    except Exception,e: 
        print Exception,":",e 
        return "Copy File error",sourceDir,"------------------------->", targetDir


def do_Clear(sourceDir):
    try:
        if (os.path.exists(sourceDir)):
            if (os.path.isdir(sourceDir)):
                shutil.rmtree(sourceDir)
                return "Clear :"+sourceDir,"------------------------->O.K"
            else:
                for file in os.listdir(sourceDir):
                    os.remove(sourceDir)
    except IOError,e: 
        print Exception,"Clear :"+ sourceDir + " ------------------------->error",e 

def Usage():
    print "<-------------------------test.py usage:------------------------->"
    print "-h,--help: print help message"
    print "-m, --manual: input out.txt to generate manifest.json"
    print "-o, --order: input allpairs order default 2"
    print "-p, --pack: pack xpk or wgt default wgt"
    print "--foo: Test option "


def get_Configxml(in_file,write_name):
    try:
        line = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><widget xmlns=\"http://www.w3.org/ns/widgets\" id=\"http://example.org/exampleWidget\" version=\"1.1\" height=\"200\" widtht=\"200\" viewmode=\"fullscreen\"><name short=\"manifest\">" + write_name + "</name></widget>"
        file = open(in_file,'w+')
        file.writelines(line + "\n")
        file.close()
    except Exception,e: 
        print Exception,"Generate the report error:",e    
        
def get_Result():
    print "<------------------------- Beging Generate Report ------------------------->"
    try:
        input_sPass = 'Pass'
        auto_sPass = 'Pass'        
        sBlock_count = 0
        input_sPass_count = 0
        input_sFail_count = 0
        auto_sPass_count = 0
        auto_sFail_count = 0        
        sResult = []
        os.system("rm -rf ./result/*.dlog")
        file = open("./report.html",'w')
        tree = ElementTree()
        file.writelines("<html><head><title>Report</title></head><body><h1>Report</h1><div><table style=\"BORDER-RIGHT: 1px ; BORDER-TOP: 1px ; BORDER-LEFT: 1px ; BORDER-BOTTOM: 1px \" cellSpacing=1 cellPadding=1 width=\"100%\" border=1  rules=\"rows\">")
        
        resultList = os.listdir(const.path_result)
        if (len(resultList) <=0):
            print "Result folder have no file"
            sys.exit(1)
        for resultfile in resultList:
            sResult = testcase_Result(const.path_result + "/"+resultfile)
            if input_sPass in (sResult[2].replace("\\n"," ")):
                    input_sPass_count = input_sPass_count + 1
            else:
                    input_sFail_count = input_sFail_count + 1
            if auto_sPass in (sResult[1].replace("\\n"," ")):
                    auto_sPass_count = auto_sPass_count + 1
            else:
                    auto_sFail_count = auto_sFail_count + 1                    
        file.writelines("Input_Pass: " + str(input_sPass_count) + "<br>Input_Fail: " + str(input_sFail_count) + "<br>Auto_Pass: " + str(auto_sPass_count) + "<br>Auto_Fail: " + str(auto_sFail_count) +  "<br>Block: " + str(sBlock_count) + "<th>TestcaseID</th><th>Auto_Result</th><th>Input_Result</th><th>Link</th>")            
        resultList = os.listdir(const.path_result)
        if (len(resultList) <=0):
            print "Result folder have no file"
            sys.exit(1)
        else:
            resultList.sort(key=None)
        for resultfile in resultList:
            sResult = testcase_Result(const.path_result + "/"+resultfile)
            file.writelines("<tr><td >" + sResult[0] + "</td><td>" + sResult[1] + "</td><td>" + sResult[2] +"</td><td><a href=result/" +  resultfile+" >" + resultfile + "</a></td></tr>")
            if input_sPass in (sResult[2].replace("\\n"," ")):
                    input_sPass_count = input_sPass_count + 1
            else:
                    input_sFail_count = input_sFail_count + 1
            if auto_sPass in (sResult[1].replace("\\n"," ")):
                    auto_sPass_count = auto_sPass_count + 1
            else:
                    auto_sFail_count = auto_sFail_count + 1

        file.writelines("</table></div></body></html>")
        file.close
        print "<------------------------- Generate Report End------------------------->"        
    except Exception,e: 
        print Exception,"Generate the report error:",e    
    
def testcase_Result(resultfile):
    try:
        tree = ElementTree()
        tree.parse(resultfile)
        root = tree.getroot()
        en = root.getiterator("testcase")
        enid=en[0]
        e_auto = root.getiterator("auto_result")
        e_input = root.getiterator("input_result")
        return enid.attrib["id"],e_auto[0].text,e_input[0].text
    except Exception,e: 
        print Exception,"Get the result -------------------------> error:",e       


def test_XML(webappFile,auto_Result,input_Result):
    try:
        print "<------------------------- Beging Generate manifest.xml ------------------------->"
        tree = ElementTree()
        tree.parse(const.path_result + "/" + webappFile)
        root = tree.getroot()
        rset = root.getchildren() 
        for mset in rset:
            testcase = mset.findall("set")
            for mtestcase in testcase:
                cnode = mtestcase.getiterator("testcase")
                if (len(cnode)==1):
                    auto_result =  root.getiterator("auto_result")
                    input_result =  root.getiterator("input_result")
                    #auto_result = cnode.getiterator("auto_result")
                    auto_result[0].text = auto_Result
                    input_result[0].text = input_Result
                else:
                    if (len(cnode)==0):
                        SubElement(mtestcase,"testcase", {'component':'core','purpose':'Check if Packaged Web Application can be installed/launch/uninstall successfully','execution_type' : 'auto', 'id' : webappFile.split(".")[0]})
                        result_node = mtestcase.find("testcase")
                        SubElement(result_node,"auto_result")
                        SubElement(result_node,"input_result")
                        SubElement(result_node,"testcommand")
                        auto_node = result_node.find("auto_result")
                        auto_node.text = auto_Result
                        input_node = result_node.find("input_result")
                        input_node.text = input_Result
                        testcommand_node = result_node.find("testcommand")
                        testcommand_node.text = "appinstall/launch/uninstall " +  webappFile.split(".")[0] + "." + Pack_Type 
        tree.write(const.path_result + "/" + webappFile)
        print "Generater result manifest.xml ------------------------->O.K"
    except Exception,e: 
        print Exception,"Generate testkit.xml error:",e 
        print "testkit.xml generate error"
        sys.exit(1)

def testcase_XML(webappName):
    tree = ElementTree()
    tree.parse(const.path + "/tests.result.xml")
    root = tree.getroot()
    lst_node = root.getiterator("set")
    for node in lst_node:
        SubElement(node,"testcase", {'component':'core','purpose':'Check if Packaged Web Application can be installed/launch/uninstall successfully','execution_type' : 'auto', 'id' : "manifest" + webappName})
    tree.write(const.path +"/tests.result.xml")  


def manifest_Packing(pakeNo,pakeType):
    try:
        print "Packing ------------------------->" + pakeNo
        print do_Clear("./opt")
        os.system("rm -rf *.zip")
        os.makedirs("./opt/wrt-manifest-tizen-tests")
        shutil.copy("./tests_sample.xml","./testkit.xml")
        shutil.copy("./testkit.xml","./opt/wrt-manifest-tizen-tests/")
        shutil.copy("./appinstall.sh","./opt/wrt-manifest-tizen-tests/")
        shutil.copy("./applaunch.sh","./opt/wrt-manifest-tizen-tests/")
        shutil.copy("./appuninstall.sh","./opt/wrt-manifest-tizen-tests/")
        cmd_packing="python ./allpairs/make_xpk.py "
        if (pakeNo =="all"):#all is not support now,please use default 
            for i in range (1,(Manifest_Row+1)):
                cmd_line=" ./tcs/manifest" + str(i) +" -o ./opt/wrt-manifest-tizen-tests/manifest" + str(i) + "."+ pakeType +" key.pem"
                if (pakeType=="xpk"):
                    os.system(cmd_packing + cmd_line)
                else:
                    os.chdir(os.getcwd() + "/tcs/manifest" + str(i))
                    os.system("zip -rq ../../opt/wrt-manifest-tizen-tests/manifest"+ str(i) +"." + pakeType+" ./")
                    os.chdir(const.path)
        else:
             cmd_line=" ./tcs/" + str(pakeNo) +" -o ./opt/wrt-manifest-tizen-tests/" + str(pakeNo)+"."+ pakeType +" key.pem"
             if (pakeType=="xpk"):
                    os.system(cmd_packing + cmd_line)
             else:
                    os.chdir(os.getcwd()+"/tcs/" + str(pakeNo))
                    os.system("zip -rq ../../opt/wrt-manifest-tizen-tests/" + str(pakeNo) +"." + pakeType+" ./")
                    os.chdir(const.path)
        os.system("zip -rq " + const.name + "-"+const.version +"." + pakeType+".zip ./opt")
        print "Packing-------------------------> O.K"
    except Exception,e: 
        print Exception,"Packing webapp error:",e   

        
def launcher_WebApp(pakeType,Manifest_Row):        
    try:
        dt_now = datetime.now()
        auto_resu = "Fail"
        dt_format = dt_now.strftime('%m_%d_%H_%M_%S')
        print "<------------------------- Launch WebApp ------------------------->"
        os.system("sdb -s " + Device_Ip +" root on")
        cmd_pushxpk = "sdb -s " + Device_Ip +" push " + const.name + "-" + const.version +"." + pakeType + ".zip"+" /opt/usr/media/tct/"
        cmd_unzipxpk = "sdb -s " + Device_Ip +" shell unzip -od /opt/usr/media/tct/ /opt/usr/media/tct/" + const.name + "-" + const.version + "." + pakeType + ".zip"
        cmd_installapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;/opt/usr/media/tct/opt/wrt-manifest-tizen-tests/appinstall.sh manifest" + Manifest_Row +  "." + pakeType +"'\""
        os.system(cmd_pushxpk)
        os.system(cmd_unzipxpk)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 /opt/usr/media/tct/opt/wrt-manifest-tizen-tests/appinstall.sh"
        os.system(cmd_chmod)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 /opt/usr/media/tct/opt/wrt-manifest-tizen-tests/applaunch.sh"
        os.system(cmd_chmod)        
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 /opt/usr/media/tct/opt/wrt-manifest-tizen-tests/appuninstall.sh"
        os.system(cmd_chmod)
        shutil.copy("./tests_sample.xml","./result/manifest" + Manifest_Row +".xml")
        test_XML("manifest" + Manifest_Row + ".xml",auto_resu,"Fail")
        #install app
        get_cmdback=get_runback(cmd_installapp)
        if ((get_cmdback[0].strip("\r\n")=="Install ok")):
            print "Install---------> OK "
            #launcher app
            Pkgids = get_cmdback[1].strip("\r\n")
            cmd_launchapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;/opt/usr/media/tct/opt/wrt-manifest-tizen-tests/applaunch.sh " + Pkgids +"'\""
            get_cmdback=get_runback(cmd_launchapp)
            if ((get_cmdback[0].strip("\r\n"))=="Launch ok"):
                print "Launch--------->OK"
                #uninstall app
                cmd_uninstallapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;/opt/usr/media/tct/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids +"'\""
                get_cmdback=get_runback(cmd_uninstallapp)
                if ((get_cmdback[0].strip("\r\n"))=="Uninstall Pass"):
                     print "Uninstall------->OK"
                     auto_resu = "Pass"
        else:
            print "Install Fail"
        #key input pass or faile
        test_XML("manifest" + Manifest_Row + ".xml",auto_resu , get_Input_Result())
        testcase_XML(Manifest_Row)
        os.system("sdb -s " + Device_Ip +" shell rm -rf /opt/usr/media/tct/opt/wrt-manifest-tizen-tests")
        os.system("sdb -s " + Device_Ip +" shell rm -rf /opt/usr/media/tct/wrt-manifest-tizen-tests*")
    except Exception,e: 
        print Exception,"Launch webapp error:",e 
        sys.exit(1)    
        
def get_runback(cmdline):
    read_line=os.popen(cmdline).readlines()  
    return read_line     

def get_Input_Result():
    try:
        print "--------------------------------------------------------------------"
        getinput = raw_input("Input result(f,p,enter),enter:Pass,F:Fail,P:Pass--->") 
        getinput =getinput.strip("")
        while not getinput in("f","p","F","P",""):
            print "--------------------------------------------------------------------"
            getinput = raw_input("Input result(f,p,Enter),Enter:Pass,F:Fail,P:Pass--->")    
        if (getinput.lower() =="p" or getinput =="" ):
            getinput = "Pass"    
        if (getinput.lower() =="f"):
            getinput = "Fail"
        return getinput
    except Exception,e: 
        print Exception,"Input result error:",e 
        sys.exit(1)


def get_Sdb_Devices():
    try:
        content_device = 1
        getDeviceList = []
        retdeviceList = []
        getDevice = os.popen("sdb devices").readlines(1)
        if (len(getDevice)>2):
            print "2 or more devices connect!"
            for i in range (0,len(getDevice)):
                getDeviceList.append(getDevice[i].split("\t")[0])
                if i>=1:
                    print "Device",i,":",getDeviceList[i].strip("\n")
            content_device = raw_input("input 1 or 2... to choice the device:")
            while (not content_device.isdigit()) or (content_device=="0") or (int(content_device) > len(getDeviceList)):
                content_device = raw_input("input 1 or 2... to choice the device:")
            if int(content_device) in range(len(getDeviceList)):
                print "getdevice=",getDeviceList[int(content_device)]
                retdeviceList = getDeviceList[int(content_device)],len(getDeviceList)
                return retdeviceList
        else:
            getDevice = getDevice[1].split("\t")[0]  
            getDevice = getDevice.strip('\n\r')
            retdeviceList = str(getDevice),1
            return retdeviceList
        #return getDevice
    except Exception,e: 
        print Exception,"Can not get sdb device:",e 
        sys.exit(1)
    
def main(argv):
    try:
        global Device_Ip 
        global Pack_Type
        shutil.copy("./tests_sample.xml","./tests.result.xml")
        print do_Clear(const.path_tcs)
        if (os.path.isdir(const.path_result)):
            os.system("rm -rf " + const.path_result +"/*")
        else:
            os.makedirs(const.path_result)
        print do_Clear(const.path + "/self")
        Device_Ip = get_Sdb_Devices()[0]
        opts, args = getopt.getopt(argv[1:], 'hm:o:p:', ['help','output=', 'order=','pack='])
        if (len(opts) ==0):
             print "Auto generate manifest.json------------------------->",opts
             #input_seed -> selfcomb.txt->manifest.json
             del_Seed(const.seed_file,const.allpairs_order)
        for o, a in opts:
            if o in ('-h', '--help'):
                Usage()
                sys.exit(1)
            elif o in ('-m', '--output'):
                gen_Manifest_Json(a)
                do_Clear(const.path + "/self")
                sys.exit(1)
            elif o in ('-o', '--order'):
                allpairs_order_get = a
                print "Auto generate manifest.json------------------------->"
                #input_seed -> selfcomb.txt->manifest.json
                del_Seed(const.seed_file,allpairs_order_get)
                #manifest folder -> webapp
                print app_Folder(const.path_tcs)
                print do_Clear(const.path + "/self")
                sys.exit(0)
            elif o in ('--foo', ):
                sys.exit(0)
            elif o in ('-p','--pack' ):
                print "Auto generate manifest.json------------------------->",opts
                #input_seed -> selfcomb.txt->manifest.json
                Pack_Type = a
                print "Pack_Type------------------------->",Pack_Type                
                del_Seed(const.seed_file,const.allpairs_order)
                sys.exit(0)
            else:
                print "***unhandled option***"
                sys.exit(3)
    except Exception,e: 
        print Exception,":",e 
        print "clear file failed"
        Usage()
        sys.exit(2)
    finally:
        get_Result()
        print do_Clear(const.path + "/opt")                 
        print do_Clear(const.path + "/self")
        print do_Clear(const.path_tcs)
        os.system("rm -rf *.zip") 
        os.system("rm -rf testkit.xml") 
        os.system("rm -rf *.pem")

if __name__=="__main__":
    main(sys.argv)
