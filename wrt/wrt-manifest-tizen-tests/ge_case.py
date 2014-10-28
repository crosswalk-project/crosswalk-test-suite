#!/usr/bin/env python
import sys, os, itertools, shutil, getopt, re, time 
import const
import pdb, traceback
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from datetime import *  
import metacomm.combinatorics.all_pairs2
import unittest
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

Manifest_Row = 0
Device_Ip = ""
Device_Ip_List = []
Device_SSH_List = []
Pack_Type = "xpk"
Test_Flag = "positive"
Test_Device_Type = "ssh"
test_start_time = datetime.now().strftime('%m-%d-%H:%M:%S')
reload(sys)
sys.setdefaultencoding( "utf-8" )
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



        
def fileline_count(fp):
     return len(open(fp).readlines()) 



def del_Seed1(in_file):
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
            row = 0
        #2*********selfcomb -> output file  by allpairs
        gen_selfcomb_File1(const.selfcomb_file, in_file)

        #3*********output -> manifest.json
        gen_Manifest_Json1(const.output_file, in_file)
        return "Manifest.json output ------------------------->O.K"
    except Exception,e: 
        print Exception,":",e
        return "Manifest.json output ------------------------->Error"

def gen_Manifest_Json1(output_file,in_file):
    try:
        global Manifest_Row
        global Pack_Type
        manifest="{\n  "
        file = open(output_file)
        if (Test_Flag=="positive"):
            testfile = open("test.py" ,'w+')
        testfile.writelines("#!/usr/bin/env python \n# coding=utf-8 \nimport random,os,sys,unittest,run_test,codecs \nreload(sys) \nsys.setdefaultencoding( \"utf-8\" ) \nclass TestCaseUnit(unittest.TestCase): \n ")
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
            os.mkdir(const.path + "/tcs/Crosswalk-Manifest-Check" + str(Manifest_Row+1))
            fp = open(const.path + "/tcs/Crosswalk-Manifest-Check"+str(Manifest_Row+1) + "/manifest.json",'w')


            for i in range(0,len(items)):
              if ((name_list[i])!="icons" and (name_list[i])!="xwalk_permissions"  and (name_list[i])!="xwalk_launch_screen"):
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
            print "\n-----------------------------------------------------------",items[0]
            print get_self
            testfile.writelines("\n  def test_case_" + str(Manifest_Row+1) +"(self):\n     self.assertEqual(\"Pass\", run_test.run_test_result(\"Crosswalk-Manifest-Check" + str(Manifest_Row+1) +"\"," + "\""+items[0].decode("utf-8") +"\"" + "))" + "\n " )
            Manifest_Row = Manifest_Row+1


            get_self=""
        testfile.writelines("\nif __name__ == '__main__':\n    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseUnit)\n    suite = unittest.TestSuite([suite1])\n    unittest.TextTestRunner(verbosity=2).run(suite) " )
        file.close()
        testfile.close()
        return "<--------------- Generate manifest.json O.K ------------------>"
    except Exception,e: 
        print Exception,"------------------------->:",e 
        print traceback.format_exc()
        return "Generate manifest.json error"

def gen_selfcomb_File1(comb_file,in_file):
    try:
        #if (os.path.isfile("./allpairs/output.txt") & (Test_Flag=="positive")):
        do_Clear("./allpairs/output.txt")
        #do_Clear("./allpairs/output_negative.txt")
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
        return "Generate selfcombination file ------------------------->O.K"
    except:
        print traceback.format_exc()

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
                #else:  
                #    print ("file exist do not copy")  
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
         
def main(argv):
    try:
        global Pack_Type
        global Test_Flag
        global Test_Device_Type

        do_Clear(const.path_tcs)
        do_Clear(const.path + "/self")
        do_Clear(const.report_path + "/manifest_all_positive.txt")
        do_Clear(const.report_path + "/manifest_all_negative.txt")
        os.system("rm -f " + const.seed_negative + "/*~")
        os.system("rm -f " + const.seed_positive + "/*~") 
        opts, args = getopt.getopt(argv[1:], 'h:o:p:n', ['help','order=','pack='])
        if (len(opts) ==0):
            print "Auto generate manifest.json------------------------->",opts
            #input_seed -> selfcomb.txt->manifest.json
            del_Seed1(const.seed_file)
        for o, a in opts:
            if o in ('-h', '--help'):
                Usage()
                sys.exit(1)
            elif o in ('-n'):
                print ("**************negative**********" )
                Test_Flag = "negative"
                if (Test_Flag=="negative"):
                  del_Seed(const.seed_file_na)
                else:
                  del_Seed(const.seed_file)                
            elif o in ('-o', '--order'):
                allpairs_order_get = a
                print "Auto generate manifest.json------------------------->"
                #create all manifest.json->positive.txt and nagative.txt
                print "------------------>"
                #del_Seed1(const.seed_file)
                #import testfile
                #suite1 = unittest.TestLoader().loadTestsFromTestCase(testfile.TestCaseUnit) 
                #manifest folder -> webapp
                #app_Folder(const.path_tcs)
                do_Clear(const.path + "/self")

            elif o in ('--foo', ):
                sys.exit(0)
            elif o in ('-p','--pack' ):
                print "Auto generate manifest.json------------------------->",opts
                #input_seed -> selfcomb.txt->manifest.json
                Pack_Type = a
                print "Pack_Type------------------------->",Pack_Type                

                sys.exit(0)
            else:
                print "***unhandled option***"
                sys.exit(3)
    except Exception,e: 
        print Exception,":",e 
        print traceback.format_exc() 
        Usage()
        sys.exit(2)
    finally:

        do_Clear(const.path + "/opt")                 
        do_Clear(const.path + "/self")
        os.system("rm -rf *.zip") 
        os.system("rm -rf *.pem")

if __name__=="__main__":
    main(sys.argv)

