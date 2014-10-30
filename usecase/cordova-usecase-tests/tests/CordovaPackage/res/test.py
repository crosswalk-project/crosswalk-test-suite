import os,commands

os.system("./bin/create hello com.example.hello hello");
os.chdir("./hello");
os.system("./cordova/build");
os.system("./cordova/run");
lsstatus = commands.getstatusoutput("ls ./bin/hello*apk &>/dev/null")
if lsstatus[0] == 0:
  print "Build Package Successfully"
else:
  print "Build Package Error"
pmstatus = commands.getstatusoutput("adb shell pm list packages |grep hello")
if pmstatus[0] == 0:
  print "Package Name Consistent"
else:
  print "Package Name Inconsistent"
