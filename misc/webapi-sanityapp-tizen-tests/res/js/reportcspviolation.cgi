#!/usr/bin/env python
import time
import os
print 'Content-Type: text/html\n\n'
while True:
    i = raw_input()
    if i is None:
        break
    if str(i).strip()=='':
        break
    n = 1
    if os.path.isfile('/tmp/csp-report.log'):
        file_object_num = open('/tmp/csp-report.log','r')
        for line in file_object_num:
            if str(line).find("Time:") >= 0:
                n = n+1
        file_object_num.close( )
    file_object = open('/tmp/csp-report.log', 'a')
    file_object.write('\n %d   Time:' %n)
    file_object.write( time.strftime(' %Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    file_object.write('\n')
    file_object.write('     Data:')
    file_object.write(i)
    file_object.write('\n')
    file_object.close( )
    print i
