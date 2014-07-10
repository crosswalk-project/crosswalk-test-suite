
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
Test_Flag = "positive"
test_start_time = datetime.now().strftime('%m-%d-%H:%M:%S')

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


def gen_Manifest_Json(output_file,in_file):
    try:
        global Manifest_Row
        file = open(output_file)
        if (Test_Flag=="positive"):
            fp_manifest = open(const.report_path + "/manifest_all_positive.txt" ,'w+')
        else:
            fp_manifest = open(const.report_path + "/manifest_all_negative.txt" ,'a+')
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
            print "\n-----------------------------------------------------------"
            print get_self
            fp_manifest.writelines("manifest" + str(Manifest_Row+1) + "\n--------------------------------\n" +
             get_self+"\n--------------------------------\n")
            Manifest_Row = Manifest_Row+1
            fp.close()
            #start copy folder
            app_Folder(const.path_tcs)
            get_Configxml(const.path_tcs + "/manifest" +str(Manifest_Row) + "/config.xml", "manifest" +str(Manifest_Row))
            #start packing
            manifest_Packing("manifest" + str(Manifest_Row),Pack_Type)
            #launch the app
            launcher_WebApp(Pack_Type,str(Manifest_Row),get_self)
            do_Clear(const.path_tcs + "/manifest" +str(Manifest_Row))
            get_self=""
        file.close()
        fp_manifest.close()
        return "<--------------- Generate manifest.json O.K ------------------>"
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
            do_Clear(const.path +"/self")
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
        gen_selfcomb_File(const.selfcomb_file,order_count, in_file)

        #3*********output -> manifest.json
        if (Test_Flag=="negative"):
            print gen_Manifest_Json(const.output_file_ne, in_file)
        else:
            print gen_Manifest_Json(const.output_file, in_file)
        log_Log(" Generate output.txt file ok"+ "\n") 
        return "Manifest.json output ------------------------->O.K"
    except Exception,e: 
        print Exception,":",e
        log_Log(" Generate output.txt file error" + e + "\n") 
        return "Manifest.json output ------------------------->Error"

def gen_selfcomb_File(comb_file,order_count,in_file):
    try:
        #if (os.path.isfile("./allpairs/output.txt") & (Test_Flag=="positive")):
        do_Clear("./allpairs/output.txt")
        do_Clear("./allpairs/output_negative.txt")
        if (Test_Flag=="negative"):
            open_output_file= open(const.output_file_ne,'a+')
        else:
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
                    #print  lists
            input_pair = all_pairs( lists )
            for e, v in enumerate(input_pair):
                for c in range(0,len(v)):
                    get_case = get_case +  v[c]+"\t"
                open_output_file.writelines(get_case.rstrip("\t") + "\n")
                get_case=""  
            open_output_file.close()
        log_Log(" Generate selfcombination file ok"+ "\n")    
        return "Generate selfcombination file ------------------------->O.K"
    except:
        log_Log(" Generate selfcombination file error"+ "\n") 
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
            else:
                os.remove(sourceDir)
    except IOError,e: 
        print Exception,"Clear :"+ sourceDir + " ------------------------->error",e 

def Usage():
    print "<-------------------------test.py usage:------------------------->"
    print "-h,--help: print help message"
    print "-n, --negative seed test"
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

def endWith(s,*endstring):
        array = map(s.endswith,endstring)
        if True in array:
                return True
        else:
                return False
def get_Result():
    try:
        auto_sPass = 'PASS'        
        sBlock_count = 0
        auto_sPass_count = 0
        total_case = 0
        auto_sFail_count = 0        
        sResult = []
        os.system("rm -rf ./result/*.dlog")
        tree = ElementTree()
        resultList = os.listdir(const.path_result)
        if (len(resultList) <=0):
            print "Result folder have no file"
            sys.exit(1)
        for resultfile in resultList:
          if (endWith(resultfile,'.xml')):
            sResult = testcase_Result(const.path_result + "/"+resultfile)
            total_case = total_case +1
            if auto_sPass in (sResult[1].replace("\\n"," ")):
                    auto_sPass_count = auto_sPass_count + 1
            else:
                    auto_sFail_count = auto_sFail_count + 1                    
       
        resultList = os.listdir(const.path_result)
        pass_rate = auto_sPass_count / float(total_case) *100
        fail_rate = auto_sFail_count / float(total_case) *100
        block_rate = sBlock_count / float(total_case) *100
        insert_to_Summary("./report/summary.xml",total_case,auto_sPass_count,pass_rate,auto_sFail_count,fail_rate, sBlock_count,block_rate)
        log_Log(" Generate report file ok" + "\n") 
        print "<------------------------- Generate Report OK------------------------->"        
    except Exception,e:
        log_Log(" Generate report file ok" + e + "\n")  
        print Exception,"Generate the report error:",e    
    
def testcase_Result(resultfile):
    try:
        tree = ElementTree()
        tree.parse(resultfile)
        root = tree.getroot()
        en = root.getiterator("testcase")
        enid=en[0]
        e_auto = root.getiterator("auto_result")
        return enid.attrib["id"],e_auto[0].text
    except Exception,e: 
        print Exception,"Get the result -------------------------> error:",e       

def insert_to_Summary(sumaryfile,total_case,pass_case,pass_rate,fail_case,fail_rate,block_case,block_rate):
    try:
        tree = ElementTree()
        tree.parse(sumaryfile)
        root = tree.getroot()
        ntotal_case = root.getiterator("total_case")
        ntotal_case[0].text = str(total_case)
        npass_case = root.getiterator("pass_case")
        npass_case[0].text = str(pass_case)
        npass_case_rate = root.getiterator("pass_rate")
        npass_case_rate[0].text = str(pass_rate)
        nfail_case = root.getiterator("fail_case")
        nfail_case[0].text = str(fail_case)
        nfail_case_rate = root.getiterator("fail_rate")
        nfail_case_rate[0].text = str(fail_rate)
        nblock_case = root.getiterator("block_case")
        nblock_case[0].text = str(block_case) 
        nblock_case_rate = root.getiterator("block_rate")
        nblock_case_rate[0].text = str(block_rate)
        test_end_time = datetime.now().strftime('%m-%d-%H:%M:%S')
        ntest_start_time = root.getiterator("start_at")
        ntest_start_time[0].text = str(test_start_time )
        ntest_end_time = root.getiterator("end_at")
        ntest_end_time[0].text = str(test_end_time )
        tree.write(sumaryfile)
    except Exception,e: 
        print Exception,"Insert to report/summart.xml -------------------------> error:",e
        


def result_manifest_XML(webappFile,auto_Result,manifest_cont):
    try:
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
                    #auto_result = cnode.getiterator("auto_result")
                    auto_result[0].text = auto_Result
                else:
                    if (len(cnode)==0):
                        SubElement(mtestcase,"testcase", {'component':'Runtime Core','purpose':'Check if packaged web application can be installed/launched/uninstalled successfully','execution_type' : 'auto', 'id' : webappFile.split(".")[0]})
                        result_node = mtestcase.find("testcase")
                        SubElement(result_node,"auto_result")
                        SubElement(result_node,"testcommand")
                        auto_node = result_node.find("auto_result")
                        auto_node.text = auto_Result
                        testcommand_node = result_node.find("testcommand")
                        testcommand_node.text = manifest_cont.decode("utf-8")
        tree.write(const.path_result + "/" + webappFile)
    except Exception,e: 
        print Exception,"Generate manifest.xml error:",e 

def testreport_auto_XML(webappName,auto_Result,tcs_manifest,tcs_message):
    try:
        tree = ElementTree()
        tree.parse(const.report_file)
        root = tree.getroot()
        lst_node = root.getiterator("set")
        if (Test_Flag=="positive"):
              SubElement(lst_node[0],"testcase", {'component':'Runtime Core','purpose':'Check if packaged web application can be installed/launched/uninstalled successfully','execution_type' : 'auto', 'id' : "manifest"+webappName ,'result': auto_Result})
              cnode = root.getiterator("testcase")
              desnode = cnode[-1]
              SubElement(desnode,"description")
              entrynode = desnode[-1]
              SubElement(entrynode,"test_script_entry")
              entryentrynode = root.getiterator("test_script_entry")
              entr = entryentrynode[-1]
              entr.text = tcs_manifest.decode("utf-8")
              SubElement(desnode,"result_info")
              resultinfonode = root.getiterator("result_info")
              result_info = resultinfonode[-1]
              result_info.text = tcs_message
              SubElement(result_info,"actual_result")
              actualresultnode = root.getiterator("actual_result")      
              actualresult = actualresultnode[-1]
              actualresult.text = auto_Result
              tree.write(const.report_file)
        else:
              SubElement(lst_node[1],"testcase", {'component':'Runtime Core','purpose':'Check if packaged web application can be installed/launched/uninstalled successfully','execution_type' : 'auto', 'id' : "manifest"+webappName ,'result': auto_Result})
              cnode = root.getiterator("testcase")
              desnode = cnode[-1]
              SubElement(desnode,"description")
              entrynode = desnode[-1]
              SubElement(entrynode,"test_script_entry")
              entryentrynode = root.getiterator("test_script_entry")
              entr = entryentrynode[-1]
              entr.text = tcs_manifest.decode("utf-8") 
              SubElement(desnode,"result_info")
              resultinfonode = root.getiterator("result_info")
              result_info = resultinfonode[-1]
              result_info.text = tcs_message
              SubElement(result_info,"actual_result")
              actualresultnode = root.getiterator("actual_result")      
              actualresult = actualresultnode[-1]
              actualresult.text = auto_Result
              tree.write(const.report_file)         
    except Exception,e: 
        print Exception,"Generate test error:",e 

def manifest_Packing(pakeNo,pakeType):
    try:
        print "-------------- Packing WebApp: "+ pakeNo +" -----------------"
        do_Clear("./opt")
        os.system("rm -rf *.zip")
        os.makedirs("./opt/wrt-manifest-tizen-tests")
        shutil.copy(const.sh_path +"/appinstall.sh","./opt/wrt-manifest-tizen-tests/")
        shutil.copy(const.sh_path +"/applaunch.sh","./opt/wrt-manifest-tizen-tests/")
        shutil.copy(const.sh_path +"/appuninstall.sh","./opt/wrt-manifest-tizen-tests/")
        shutil.copy(const.sh_path +"/checkdb.sh","./opt/wrt-manifest-tizen-tests/")
        shutil.copy(const.sh_path +"/checkdb_new.sh","./opt/wrt-manifest-tizen-tests/")
        cmd_packing="python ./allpairs/make_xpk.py "
        if (pakeNo =="all"):#all is not support now,please use default 
            for i in range (1,(Manifest_Row+1)):
                cmd_line=" ./tcs/manifest" + str(i) +" -o ./opt/wrt-manifest-tizen-tests/manifest" + str(i) + "."+ pakeType +" key.pem "
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
        do_Clear("key.pem")
        log_Log(" Packing webapp " + pakeNo + " ok "+ "\n") 
    except Exception,e:
        log_Log(" Packing webapp " + pakeNo + " error " + e +"\n")  
        print Exception,"Packing webapp error:",e   

        
def launcher_WebApp(pakeType,Manifest_Row, tcs_manifest):        
    try:
        dt_now = datetime.now()
        auto_result = "FAIL"
        fail_message = ""
        dt_format = dt_now.strftime('%m_%d_%H_%M_%S')
        cmd_pushxpk = "sdb -s " + Device_Ip +" push " + const.name + "-" + const.version +"." + pakeType + ".zip " +  const.device_path + " >/dev/null"
        cmd_unzipxpk = "sdb -s " + Device_Ip +" shell unzip -od " + const.device_path + "  " + const.device_path + const.name + "-" + const.version + "." + pakeType + ".zip >/dev/null"
        cmd_installapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;" + const.device_path + "/opt/wrt-manifest-tizen-tests/appinstall.sh "+ const.device_path +"/opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row +  "." + pakeType +"'\""
        os.system(cmd_pushxpk)
        os.system(cmd_unzipxpk)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/appinstall.sh"
        os.system(cmd_chmod)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/applaunch.sh"
        os.system(cmd_chmod)        
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh"
        os.system(cmd_chmod)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb.sh"
        os.system(cmd_chmod)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb_new.sh"
        os.system(cmd_chmod)
        shutil.copy("./tests_sample.xml","./result/manifest" + Manifest_Row +".xml")
        result_manifest_XML("manifest" + Manifest_Row + ".xml",auto_result,tcs_manifest)
        #install app
        cmd_checkdb="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb.sh '\""
        get_dbcount_before = get_runback(cmd_checkdb,"install","")[0].strip("\n\r")
        get_cmdback = get_runback(cmd_installapp,"install","")
        get_dbcount_after = get_runback(cmd_checkdb,"install","")[0].strip("\n\r")
        add_webapp = int(get_dbcount_after) - int(get_dbcount_before)
        cmd_checkdb_new = "sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb_new.sh " + str(int(get_dbcount_after)-1) + "'\""
        get_fromdb = get_from_DB(cmd_checkdb_new,tcs_manifest)
        log_Log(" check DB--------->" + Manifest_Row + " get DB= " + str(get_fromdb) + "\n")
        if ((add_webapp==1) & (get_fromdb[0]=="GET") & (Test_Flag=="positive")): #install ok and test =positive
              print "Install---------> OK "
              log_Log(" install--------->" + Manifest_Row + " OK"+ "\n") 
              fail_message = "install ok"
              auto_result = "PASS"
              #launcher app
              Pkgids = get_fromdb[1]
              cmd_launchapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/applaunch.sh " + Pkgids +"'\""
              get_cmdback = get_runback(cmd_launchapp,"launch",Pkgids)
              if ((get_cmdback[0].strip("\r\n"))=="Launch ok"):
                  print "Launch---------> OK"
                  log_Log(" launch--------->" + Manifest_Row + " OK"+ "\n")
                  fail_message = "launch webapp ok"
                  #uninstall app
                  cmd_uninstallapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids +"'\""
                  cmd_checkdb="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb.sh " + Pkgids +"'\""
                  get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")
                  get_dbcount_uninstall = get_runback(cmd_checkdb,"install","")[0].strip("\n\r")
                  uninstall_webapp = int(get_dbcount_before) - int(get_dbcount_uninstall)

                  if (uninstall_webapp==0):
                       print "Uninstall-------> OK"
                       log_Log(" uninstall--------->" + Manifest_Row + " OK"+ "\n") 
                       auto_result = "PASS"
                       fail_message = "uninstall and db check ok"
                  else:
                      fail_message = "uninstall and db check fail"
                      print "Uninstall-------> Fail"
                      shutil.move("opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row + "." + pakeType ,const.path_result)
              else:
                fail_message = "launch fail"
                shutil.move("opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row + "." + pakeType ,const.path_result)
        elif ((add_webapp==1) & (Test_Flag=="positive")): # positive install ok but test fail
              auto_result = "FAIL"
              fail_message = "install ok but check db fail"
              log_Log(" install--------->" + Manifest_Row + " check DB fail"+ "\n")
              print "Positive test ----------> install OK but check DB fail" 
              shutil.move("opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row + "." + pakeType ,const.path_result)
              Pkgids = get_fromdb[1]
              cmd_uninstallapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids +"'\""
              get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")               
        elif ((add_webapp==0) & (Test_Flag=="positive")): #install ok and test =positive
              auto_result = "FAIL"
              fail_message = "install and db check fail"
              shutil.move("opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row + "." + pakeType ,const.path_result)
              log_Log(" install--------->" + Manifest_Row + " fail"+ "\n")
              print "Positive test ----------> install or check DB fail"
        elif ((add_webapp==1) & (Test_Flag=="negative")): #install ok and test =negative
              auto_result = "FAIL" 
              shutil.move("opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row + "." + pakeType ,const.path_result)
              log_Log(" negative test install ok:--------->" + Manifest_Row + " fail"+ "\n")
              fail_message = "negative test install ok: Fail"  
              print "Negative test-------> Install ok: Fail"
              Pkgids = get_fromdb[1]
              cmd_uninstallapp="sdb -s " + Device_Ip +" shell \"su - app -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids +"'\""
              get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")  
        elif ((add_webapp==0) & (Test_Flag=="negative")): #install ok and test =negative
              auto_result = "PASS" 
              log_Log(" negative test install fail :--------->" + Manifest_Row + " pass"+ "\n")
              fail_message = "negative install fail: Pass"
              print "Negative test-------> Install fail: Pass"                        
        else:
            auto_result = "FAIL"
            shutil.move("opt/wrt-manifest-tizen-tests/manifest" + Manifest_Row + "." + pakeType ,const.path_result)
            log_Log(" other fail:--------->" + Manifest_Row + "\n")
            fail_message = "install fail"
            print "-------------Install/Launch/Uninstall Fail-------------------"
        #key input pass or faile
        print "---------- Webapp manifest" + Manifest_Row + "." + pakeType +" test end------------>\n"
        log_Log(" test webapp " + Manifest_Row + " ok "+ "\n")                    
    except Exception,e: 
        log_Log(" test webapp " + Manifest_Row + " error " + e + "\n") 
        print Exception,"Launch webapp error:",e 
    finally:
        result_manifest_XML("manifest" + Manifest_Row + ".xml",auto_result , tcs_manifest)
        testreport_auto_XML(Manifest_Row, auto_result ,tcs_manifest,fail_message)         
        os.system("sdb -s " + Device_Ip +" shell rm -rf "+const.device_path+"/opt/wrt-manifest-tizen-tests")
        os.system("sdb -s " + Device_Ip +" shell rm -rf "+const.device_path+"/wrt-manifest-tizen-tests*")
        return
                
def get_runback(cmdline,step,pkgids):
    try:
        read_line = os.popen(cmdline).readlines()
        return read_line     
    except Exception,e: 
        print Exception,"get runback error:",e 
         
def get_Input_Result():
    try:
        print "--------------------------------------------------------------------"
        getinput = raw_input("Input result(f,p,enter),enter:PASS,F:FAIL,P:PASS--->") 
        getinput =getinput.strip("")
        while not getinput in("f","p","F","P",""):
            print "--------------------------------------------------------------------"
            getinput = raw_input("Input result(f,p,Enter),Enter:PASS,F:FAIL,P:PASS--->")    
        if (getinput.lower() =="p" or getinput =="" ):
            getinput = "PASS"    
        if (getinput.lower() =="f"):
            getinput = "FAIL"
        return getinput
    except Exception,e: 
        print Exception,"Input result error:",e 

def get_from_DB(cmdline,manifest):
    try:
        read_line = os.popen(cmdline).readlines()
        log_Log(" get DB ="+ str(read_line))
        get_id = read_line[0].split("|")[0]
        get_manifest = manifest.strip("\n\r\t").split(",")
        for i in range(0,len(get_manifest)):
          find_name = get_manifest[i].find("name")
          if (find_name>=0):
            get_manifest_name = get_manifest[i].split(":")[1][2:-1]
            get_db_name = read_line[0].find(get_manifest_name)
            if (get_db_name>=0):
                print "Check From DB ------------------------->"
                return "GET",get_id
            elif ((str(get_manifest_name).find("<"))>=0 & (str(get_db_name).find("003C")>=0)):
                print "Check From DB ------------------------->"
                return "GET",get_id
            else:
                return "NONE"
          return "NONE"
    except Exception,e: 
        print Exception,"Get db record error:",e 
  


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
                    print "Device",i,":",getDeviceList[i].strip("\t")
            content_device = raw_input("input 1 or 2... to choice the device:")
            while (not content_device.isdigit()) or (content_device=="0") or (int(content_device) > len(getDeviceList)-1):
                content_device = raw_input("input 1 or 2... to choice the device:")
            if int(content_device) in range(len(getDeviceList)):
                retdeviceList = getDeviceList[int(content_device)],len(getDeviceList)
                log_Log(" get sdb device=" + retdeviceList[0] + "\n")
                return retdeviceList
        else:
            getDevice = getDevice[1].split("\t")[0]  
            getDevice = getDevice.strip('\n\r')
            retdeviceList = str(getDevice),1
            log_Log(" get sdb device=" + retdeviceList[0] + "\n")
            return retdeviceList
        #return getDevice
    except Exception,e: 
        print Exception,"Can not get sdb device:",e
        log_Log(" get sdb device error\n") 
        sys.exit(1)

        
def add_style_Report(file_name,style_file):
    try:
        fp = file(file_name)
        lines = []
        for line in fp:
           lines.append(line)
        fp.close()
        lines.insert(0, "<?xml version=\"1.0\" encoding=\"UTF-8\"?><?xml-stylesheet type=\"text/xsl\" href=\"./style/" + style_file +"\"?>")
        s = ''.join(lines)
        fp = file(file_name, 'w')
        fp.write(s)
        fp.close()
    except Exception,e: 
        print Exception,"Add sytle to report error:",e 

def log_Log(message):
    try:
        log_time = datetime.now().strftime('%m-%d-%H:%M:%S')
        logfile.write(log_time +": "+ message)
    except Exception,e: 
        print Exception,"Add log to log.txt error:",e 
     
def main(argv):
    try:
        global Device_Ip 
        global Pack_Type
        global Test_Flag
        global logfile
        shutil.copy("./tests.report.xml",const.report_file)
        logfile = file(const.log_path,"w+")
        do_Clear(const.path_tcs)
        log_Log(" test start\n")
        log_Log(" init summart file\n")
        insert_to_Summary(const.report_summary_file,"0","0","0","0","0","0","0")
        if (os.path.isdir(const.path_result)):
            os.system("rm -rf " + const.path_result +"/*")
        else:
            os.makedirs(const.path_result)
        do_Clear(const.path + "/self")
        do_Clear(const.report_path + "/manifest_all_positive.txt")
        do_Clear(const.report_path + "/manifest_all_negative.txt")
        os.system("rm -f " + const.seed_negative + "/*~")
        os.system("rm -f " + const.seed_positive + "/*~")        
        Device_Ip = get_Sdb_Devices()[0]
        os.system("sdb -s " + Device_Ip +" root on")
        cmd_createtct = "sdb -s " + Device_Ip +" push " + const.sh_path +"/checktct_folder.sh /home/app/content/ >/dev/null"
        os.system(cmd_createtct)
        cmd_chmod = "sdb -s " + Device_Ip +" shell chmod 777 /home/app/content/checktct_folder.sh"
        os.system(cmd_chmod)
        cmd_createtctfolder = "sdb -s " + Device_Ip +" shell /home/app/content/checktct_folder.sh "
        os.system(cmd_createtctfolder)
        log_Log(" create tct folder \n") 
        opts, args = getopt.getopt(argv[1:], 'h:o:p:n', ['help','order=','pack='])
        if (len(opts) ==0):
             print "Auto generate manifest.json------------------------->",opts
             #input_seed -> selfcomb.txt->manifest.json
             del_Seed(const.seed_file,const.allpairs_order)
             Test_Flag = "negative"
             for negativeseed in os.listdir(const.seed_negative):
                 if (fileline_count(const.seed_negative+"/" + negativeseed) >=1) :
                     do_Clear(const.path_tcs)
                     do_Clear(const.path + "/opt")                 
                     do_Clear(const.path + "/self")
                     del_Seed(const.seed_negative + "/" + negativeseed,const.allpairs_order)
        for o, a in opts:
            if o in ('-h', '--help'):
                Usage()
                sys.exit(1)
            elif o in ('-n'):
                print ("**************negative**********" )
                Test_Flag = "negative"
                if (Test_Flag=="negative"):
                  del_Seed(const.seed_file_na,const.allpairs_order)
                else:
                  del_Seed(const.seed_file,const.allpairs_order)                
            elif o in ('-o', '--order'):
                allpairs_order_get = a
                print "Auto generate manifest.json------------------------->"
                #input_seed -> selfcomb.txt->manifest.json
                #del_Seed(const.seed_file,allpairs_order_get)
                #manifest folder -> webapp
                app_Folder(const.path_tcs)
                do_Clear(const.path + "/self")
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
        log_Log(" test fail\n")
        Usage()
        sys.exit(2)
    finally:
        get_Result()
        add_style_Report(const.report_file,"testresult.xsl")
        add_style_Report(const.report_summary_file,"summary.xsl")
        log_Log(" test end\n")        
        logfile.close()
        do_Clear(const.path + "/opt")                 
        do_Clear(const.path + "/self")
        do_Clear(const.path_tcs)
        os.system("rm -rf *.zip") 
        os.system("rm -rf *.pem")

if __name__=="__main__":
    main(sys.argv)
