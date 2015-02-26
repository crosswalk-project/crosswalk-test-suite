#!/usr/bin/env python
import sys, os, itertools, shutil, getopt, re, time 
import const
import pdb, traceback
import subprocess
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from datetime import *  
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

Manifest_Row = 0
Device_Ip = ""
Device_Ip_List = []
Device_SSH_List = []
Pack_Type = "xpk"
Test_Flag = "positive"
Test_Device_Type = "ssh"
test_start_time = datetime.now().strftime('%m-%d-%H:%M:%S')
Tizen_User=os.environ['TIZEN_USER']
reload(sys)
sys.setdefaultencoding( "utf-8" )

def doCMD(cmd):
    # Do not need handle timeout in this short script, let tool do it
    print "-->> \"%s\"" % cmd
    output = []
    cmd_return_code = 1
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    while True:
        output_line = cmd_proc.stdout.readline().strip("\r\n")
        cmd_return_code = cmd_proc.poll()
        if output_line == '' and cmd_return_code != None:
            break
        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)

    return (cmd_return_code, output)

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

def getUSERID():
    if Test_Device_Type=="sdb":
        cmd = "sdb -s %s shell id -u %s" % (getEnv_Id, Tizen_User)  
    else:
        cmd = "ssh %s \"id -u %s\"" % (getEnv_Id, Tizen_User)
    return doCMD(cmd)
    
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
                cmd_line=" ./tcs/Crosswalk-Manifest-Check" + str(i) +" -o ./opt/wrt-manifest-tizen-tests/Crosswalk-Manifest-Check" + str(i) + "."+ pakeType +" key.pem "
                if (pakeType=="xpk"):
                    os.system(cmd_packing + cmd_line)
                else:
                    os.chdir(os.getcwd() + "/tcs/Crosswalk-Manifest-Check" + str(i))
                    os.system("zip -rq ../../opt/wrt-manifest-tizen-tests/Crosswalk-Manifest-Check"+ str(i) +"." + pakeType+" ./")
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
    except Exception,e:
        print Exception,"Packing webapp error:",e   

        
def launcher_WebApp(pakeType,Manifest_Row,Device_ID,Device_Type,Manifest_Name):        
    try:

        auto_result = "FAIL"
        fail_message = ""
        print "get_tytp=",Device_Type
        if (Device_Type=="sdb"):
          print "use sdb device-------------->"
          cmd_pushxpk = "sdb -s " + Device_ID +" push " + const.name + "-" + const.version +"." + pakeType + ".zip " +  const.device_path 
          cmd_unzipxpk = "sdb -s " + Device_ID +" shell unzip -od " + const.device_path + "  " + const.device_path + const.name + "-" + const.version + "." + pakeType + ".zip "
          cmd_installapp="sdb -s " + Device_ID +" shell \"su - " + Tizen_User + " -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;" + const.device_path + "/opt/wrt-manifest-tizen-tests/appinstall.sh "+ const.device_path +"/opt/wrt-manifest-tizen-tests/" + str(Manifest_Row) +  "." + pakeType +"'\""
          print "------------push webapp----------->",cmd_pushxpk
          os.system("sdb -s " + Device_ID +" root on")
          get_push = get_runback(cmd_pushxpk,"push","")
          
          print "------------unzip webapp---------->",Device_ID     
          get_unzip = get_runback(cmd_unzipxpk,"unzip","")

          cmd_chmod = "sdb -s " + Device_ID +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/appinstall.sh"
          os.system(cmd_chmod)
          cmd_chmod = "sdb -s " + Device_ID +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/applaunch.sh"
          os.system(cmd_chmod)        
          cmd_chmod = "sdb -s " + Device_ID +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh"
          os.system(cmd_chmod)
          cmd_chmod = "sdb -s " + Device_ID +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb.sh"
          os.system(cmd_chmod)
          cmd_chmod = "sdb -s " + Device_ID +" shell chmod 777 "+const.device_path+"/opt/wrt-manifest-tizen-tests/checkdb_new.sh"
          os.system(cmd_chmod)

          #install app
          get_cmdback = get_runback(cmd_installapp,"install","")
          print "----------------->get",get_cmdback,"\n"

          get_cmdback1= get_cmdback[0]
          print "----------------->getback",get_cmdback1,"\n"
          get_pkgid = get_cmdback1[(get_cmdback1.find("pkgid")+6):(get_cmdback1.find("pkgid")+38)]
          get_install_flag = get_cmdback1.find("val[ok]")

          if ((get_install_flag>0) & (Test_Flag=="positive")): #install ok and test =positive
                print "Install---------> OK "
                fail_message = "install ok"
                auto_result = "Pass"
                #launcher app
                Pkgids = get_pkgid
                cmd_launchapp="sdb -s " + Device_ID +" shell \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/applaunch.sh xwalk." + Pkgids +"'\""
                get_cmdback = get_runback(cmd_launchapp,"launch",Pkgids)
                print "pkgids = ",Pkgids
                if ((get_cmdback[0].strip("\r\n"))=="Launch ok"):
                    print "Launch---------> OK"
                    fail_message = "launch webapp ok"
                    #uninstall app
                    cmd_uninstallapp="sdb -s " + Device_ID +" shell \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;bash "+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids + "'\""
                    get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")
                    print "uninstall===",cmd_uninstallapp,"|",str(get_cmdback)
                    if ((str(get_cmdback).find("val[ok]")>0)):
                         print "Uninstall-------> OK"
                         auto_result = "Pass"
                         fail_message = "uninstall and db check ok"
                    else:
                        fail_message = "uninstall and db check fail"
                        auto_result = "FAIL"
                        print "Uninstall-------> Fail"
                else:
                  fail_message = "launch fail"
          elif ((Test_Flag=="positive")): # positive install ok but test fail
               auto_result = "FAIL"
               fail_message = "install fail"
               print "Positive test ----------> install fail" 

               cmd_uninstallapp="sdb -s " + Device_ID +" shell \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;"+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids +"'\""
               get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")
               auto_result = "FAIL"
          elif ((Test_Flag=="negative")): #install ok and test =negative
                  auto_result = "Pass"
                  fail_message = "negative install fail: Pass"
                  print "Negative test-------> Install fail: Pass"
          else:
                auto_result = "FAIL"
                fail_message = "install fail"
                print "-------------Install/Launch/Uninstall Fail-------------------"
                #key input pass or faile
          print "---------- Webapp Crosswalk-Manifest-Check" + str(Manifest_Row) + "." + pakeType +" test end------------>\n"
          os.system("sdb -s " + Device_ID +" shell rm -rf "+const.device_path+"/opt/wrt-manifest-tizen-tests")
          os.system("sdb -s " + Device_ID +" shell rm -rf "+const.device_path+"/wrt-manifest-tizen-tests*")
        else:
          print "use ssh device-------------->"
          cmd_pushxpk = "scp " + const.name + "-" + const.version +"." + pakeType + ".zip " + Device_ID + ":"+ const.device_path 
          cmd_unzipxpk = "ssh " + Device_ID +" 'unzip -od " + const.device_path + "  " + const.device_path + const.name + "-" + const.version + "." + pakeType + ".zip'"
          cmd_installapp="ssh " + Device_ID +" \"su - " + Tizen_User + " -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;bash " + const.device_path + "/opt/wrt-manifest-tizen-tests/appinstall.sh "+const.device_path +"/opt/wrt-manifest-tizen-tests/" + str(Manifest_Row) +  "." + pakeType +"'\""
          print "------------push webapp----------->",Device_ID
          get_push = get_runback(cmd_pushxpk,"push","")
          print "------------unzip webapp----------->",Device_ID       
          get_unzip = get_runback(cmd_unzipxpk,"unzip","")
          #install app
          get_cmdback = get_runback(cmd_installapp,"install","")
          get_cmdback1= get_cmdback[0]
          get_pkgid = get_cmdback1[(get_cmdback1.find("pkgid")+6):(get_cmdback1.find("pkgid")+38)]
          get_install_flag = get_cmdback1.find("val[ok]")

          if ((get_install_flag>=0) & (Test_Flag=="positive")): #install ok and test =positive
                  print "Install---------> OK "
                  fail_message = "install ok"
                  #launcher app
                  Pkgids = get_pkgid
                  cmd_launchapp="ssh " + Device_ID +" \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;bash "+const.device_path+"/opt/wrt-manifest-tizen-tests/applaunch.sh xwalk." + Pkgids +"'\""

                  get_cmdback = get_runback(cmd_launchapp,"launch",Pkgids)

                  if ((get_cmdback[0].strip("\r\n"))=="Launch ok"):
                      print "Launch---------> OK"
                      fail_message = "launch webapp ok"
                      #uninstall app
                      cmd_uninstallapp="ssh " + Device_ID +"  \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;bash "+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids + "'\""
                      get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")

                      if ((str(get_cmdback).find("val[ok]")>0)):
                           print "Uninstall-------> OK"
                           auto_result = "Pass"
                           fail_message = "uninstall and db check ok"
                      else:
                          fail_message = "uninstall and db check fail"
                          auto_result = "FAIL"
                          print "Uninstall-------> Fail"
                  else:
                    fail_message = "launch fail"
          elif (Test_Flag=="positive"): # positive install ok but test fail
                  auto_result = "FAIL"
                  fail_message = "install fail"
                  print "Positive test ----------> install fail" 
                  Pkgids = get_pkgid
                  cmd_uninstallapp="ssh " + Device_ID +"  \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;bash "+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids + "'\""
                  get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")
                  auto_result = "FAIL"
          elif ((get_install_flag>=0) & (Test_Flag=="negative")): #install ok and test =negative
                  auto_result = "FAIL" 
                  fail_message = "negative test install ok: Fail"
                  print "Negative test-------> Install ok: Fail"
                  Pkgids = get_pkgid
                  cmd_uninstallapp="ssh " + Device_ID +"  \"su - "+ Tizen_User +" -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/"+Userid+"/dbus/user_bus_socket;bash "+const.device_path+"/opt/wrt-manifest-tizen-tests/appuninstall.sh " + Pkgids + "'\""
                  get_cmdback = get_runback(cmd_uninstallapp,"uninstall","")
          elif (Test_Flag=="negative"): #install ok and test =negative
                  auto_result = "Pass"
                  fail_message = "negative install fail: Pass"
                  print "Negative test-------> Install fail: Pass"                  
          else:
                auto_result = "FAIL"
                fail_message = "install fail"
                print "-------------Install/Launch/Uninstall Fail-------------------"
          print "---------- Webapp Crosswalk-Manifest-Check" + str(Manifest_Row) + "." + pakeType +" test end------------>\n"

          os.system("ssh " + Device_ID +" 'rm -rf "+const.device_path+"/opt/wrt-manifest-tizen-tests'")
          os.system("ssh  " + Device_ID +" 'rm -rf "+const.device_path+"/wrt-manifest-tizen-tests*'")
            
    except Exception,e: 
        print Exception,"Launch webapp error:",e 
        print traceback.format_exc() 
    finally:
        return auto_result
                
def get_runback(cmdline,step,pkgids):
    try:
        read_line = os.popen(cmdline).readlines()
        return read_line     
    except Exception,e: 
        print Exception,"get runback error:",e
        return "Exception-->",read_line,e
         

def get_from_DB(cmdline,manifest):
    try:
        read_line = os.popen(cmdline).readlines()
        pkgid = read_line[1].split("\t")[1]
        pkgid = pkgid[7:-1]
        name =  read_line[1].split("\t")[2]
        name = name[6:-1]
        if (manifest.find(name)>=0):
            print "get name",name,pkgid
            return "GET",pkgid
    except Exception,e: 
        print Exception,"Get db record error:",e
        print traceback.format_exc()
        return "NONE"
 
        
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


def app_Folder(path_tcs,path_tcs_manifest):
    try:
        copy_Files(const.path_resource,os.getcwd()+"/tcs/" + path_tcs_manifest)
        return "Webapp folder copy ------------------------->O.K",path_tcs
    except Exception,e: 
        print Exception,":",e 
        return "Webapp folder copy ------------------------->error",path_tcs
                        
def run_test_result(manifest_file,manifest_name):
    try:
        global Pack_Type
        global Test_Flag
        get_result = "fail"
        do_Clear(const.path + "/self")
        do_Clear(const.report_path + "/manifest_all_positive.txt")
        do_Clear(const.report_path + "/manifest_all_negative.txt")
        os.system("rm -f " + const.seed_negative + "/*~")
        os.system("rm -f " + const.seed_positive + "/*~") 
        os.system("rm -rf ./device_*")
        global getEnv_Id
        global Userid
        getEnv_Id = os.environ.get('DEVICE_ID')
        if ((not getEnv_Id) or len(getEnv_Id)<10):
            print (" get env error\n")
            sys.exit(1)
        user_info = getUSERID()
        re_code = user_info[0]
        if re_code == 0 :
            Userid = user_info[1][0]
        else:
            print "[Error] cmd commands error : %s"%str(user_info[1])
            sys.exit(1)

        Test_Device_Type = os.environ.get('CONNECT_TYPE')



        #add resource
        app_Folder(const.path_tcs,manifest_file)
        #pack to xpk
        manifest_Packing(manifest_file,"xpk")
        #launch test
        get_result = launcher_WebApp("xpk",manifest_file,getEnv_Id,Test_Device_Type,manifest_name)
        
        do_Clear(const.path + "/opt")                 
        do_Clear(const.path + "/self")
        os.system("rm -rf *.zip")
        print "get_run_result----------------->",get_result
        return get_result

    except Exception,e: 
        print Exception,":",e 
        print traceback.format_exc() 

