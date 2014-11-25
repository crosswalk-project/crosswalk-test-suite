#!/usr/bin/env python

import sys, os, itertools, shutil, getopt, re 
import conf
import pdb, traceback
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

def usage():
        print 'allpairs-plus.py usage:'
        print '-h: print help message.'
        print '-b: use baseline file as part of output, e.g. baseline.txt'

def do_Selfcom(self_combin_file,out_file):
    try:
        file = open(self_combin_file)
        allpairs_in = open(out_file,'a+')
        while 1:
            line = file.readline().replace("null","")
            line = line.replace(",,",",")
            if (line[-1:]==","):
              line = line[:-1]
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


def del_Seed(in_file):
    try:
        caseline = "" 
        old_list = []
        format_list =[]
        de=""
        row = 0
        file = open(in_file)
        items = []
        self_file = []
        s_name = p_name = ""
        if (os.path.isdir("self")):
            do_Clear(conf.path +"/self")
        os.mkdir(conf.path + "/self")
        while 1:
            p_name = s_name
            line = file.readline()
            if not line:
                break
            line = line.strip('\n\r')
            items = line.split(":")
            s_name = items[0].split("-")[0]
            if ((p_name!=s_name) and (p_name!="")):
                fp=open(conf.path + "/self/" + s_name + "_input.txt",'a+')
                fp.writelines(line + "\n")
            else:
                fp= open(conf.path + "/self/" + s_name + "_input.txt",'a+')
                fp.writelines(line + "\n")
            if (s_name!=p_name):
                self_file.append(s_name)
        fp.close()
        file.close()
        if (os.path.isfile(conf.selfcomb_file)):
            os.remove(conf.selfcomb_file)
        for i in range (0,len(self_file)):
            line_count = fileline_count(conf.path + "/self/" + self_file[i] + "_input.txt")

            if (line_count >= 2):
                lists = [[] for m in range(line_count)]
                open_input_file = open(conf.path + "/self/" + self_file[i] + "_input.txt",'a+')
                while 1:
                    line = open_input_file.readline()
                    if not line:
                        break
                    line = line.strip('\n\r')
                    items = line.split(":")
                    get_item = items[1].split(",")
                    get_item1 = get_item
                    if (str(get_item).find("null"))>1:
                        for element in range(0,len(get_item)):
                           if get_item[element]=="null":
                               old_list = old_list + get_item
                    for g in get_item:
                        lists[row].append(g)
                    row = row + 1
                input_pair = all_pairs( lists )
                 
                open_input_file.close()
                output_pair = open(conf.path + "/self/" + self_file[i] + "_output.txt",'a+')
                for e, v in enumerate(input_pair):
                      for c in range(0,len(v)):
                          caseline = caseline + v[c]
                      caseline = caseline.replace("null","")  + ","
                get_output_item = caseline[:-1].split(",")
                get_output_item = old_list + get_output_item
                format_list =  ','.join(dele_list(get_output_item))
                #print "get-----",get_output_item
                output_pair.writelines(self_file[i] + ":" + format_list)
                output_pair.close()
            else:
                open_input_file = open(conf.path + "/self/" + self_file[i] + "_input.txt",'r')
                output_pair = open(conf.path + "/self/" + self_file[i] + "_output.txt",'a+')
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
            do_Selfcom(conf.path + "/self/" + self_file[i] + "_output.txt",conf.selfcomb_file)
            row = 0
            caseline = ""
            format_list=[]
            get_output_item = []
            old_list = []
        #2*********selfcomb -> output file  by allpairs
        gen_selfcomb_File(conf.selfcomb_file, in_file)

    except Exception,e: 
        print Exception,":",e
        print traceback.format_exc()
        
def dele_list(old_list):
    try:
        newList = []
        for x in old_list:
            if x not in newList :
                newList.append(x)
        return newList
    except Exception,e: 
        print Exception,":",e
        print traceback.format_exc()        

def gen_selfcomb_File(comb_file,in_file):
    try:
        open_output_file= open(conf.output_file,'a+')
        caseline = "" 
        get_items = ""
        get_case = ""
        get_out_put = ""
        row = 0
        line_count = fileline_count(comb_file)
        if (line_count >= 1):
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
            if len(lists)>1:
                input_pair = all_pairs( lists )
                for e, v in enumerate(input_pair):
                    for c in range(0,len(v)):
                        get_case = get_case +  v[c] + "\t"
                    get_out_put  = get_case.replace("null","").replace("comma",",").strip("\t")
                    open_output_file.writelines(get_out_put + "\n")
                    #print get_case.replace("null","").rstrip("\t") 
                    get_case=""  
                open_output_file.close()
            return "Generate selfcombination file ------------------------->O.K"
    except:
        print traceback.format_exc()


def do_Clear(sourceDir):
    try:
        if (os.path.exists(sourceDir)):
            if (os.path.isdir(sourceDir)):
                shutil.rmtree(sourceDir)
            else:
                os.remove(sourceDir)
    except IOError,e: 
        print Exception,"Clear :"+ sourceDir + " ------------------------->error",e 

def integrate_baseline(baseline_file):
        output_bl = open(baseline_file)
        output_bl_list = output_bl.readlines()
        output = open(conf.output_file)
        output_list = output.readlines()
	col_outbl = len(output_bl_list[0].split("\t"))
	col_out = len(output_list[0].split("\t"))

	# Only exist parameter changed
	if col_outbl==col_out: 
           print ">>>>>>> Only exist parameters changed"
           for var in output_list:
                if var not in output_bl_list:
                        output_bl_list.append(var)
	   print ">>>>>>> Generate output with baseline ------------>OK"
	   output_withbaseline = open(conf.output_file, "w")
           output_withbaseline.writelines(output_bl_list)
           output_withbaseline.close()
	   print ">>>>>>> END"
	   sys.exit()

	# New parameters added, and maybe exist parameters also changed 
	print ">>>>>>> New parameters added, and maybe exist parameters also changed"
	out_dict={};
	for var in output_list:
		list_row = var.split("\t")
		key = '\t'.join(list_row[0:col_outbl])
		value = '\t'.join(list_row[col_outbl:col_out])
		out_dict[key] = value

	output_list_new = []
	i = 0
	for var in output_bl_list:
		var = var.strip('\n')
		list_row = var.split("\t")
		key = '\t'.join(list_row)
		value = out_dict.get(key)
		while (i>=len(out_dict)):
			i = i/2;
		if value is None:
			value = out_dict.values()[i] 
		output_list_new.append("\t".join((var,value)))
		i = i + 1;

	print ">>>>>>> Generate output with baseline ------------>OK"
        for var in output_list:
                if var not in output_list_new:
                        output_list_new.append(var)
        output_withbaseline = open(conf.output_file, "w")
        output_withbaseline.writelines(output_list_new)
        output_withbaseline.close()
	print ">>>>>>> END"

def main():
    try:
        do_Clear("./output/output.txt")    
        del_Seed(conf.seed_file)
        do_Clear("./self")
        opts,args=getopt.getopt(sys.argv[1:],"hb:")
        for op,val in opts:
                if op=="-b":
                        baseline=val
			print "use",baseline, "as baseline"
			integrate_baseline(baseline);
                elif op=="-h":
                        usage()
                        sys.exit()
    except Exception,e: 
        print Exception,":",e 

if __name__=="__main__":
    main()
