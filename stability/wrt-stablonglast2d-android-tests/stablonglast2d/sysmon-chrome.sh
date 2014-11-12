#!/bin/bash
sysmonFolder="_sysmon_"`date '+%Y%m%d%H%M'`
mkdir /tmp/$sysmonFolder
echo "Create result folder: /tmp/$sysmonFolder"

#times=`expr 172800 / 10`
times=`expr $1 / 10`
while [ $times -ne "0" ]
do
	echo `date` >> /tmp/$sysmonFolder/cpu.res
	echo `date` >> /tmp/$sysmonFolder/mem.res
	adb shell "dumpsys cpuinfo |grep chrome" >> /tmp/$sysmonFolder/cpu.res
	adb shell "dumpsys meminfo |grep chrome" | head -n 2 >> /tmp/$sysmonFolder/mem.res
	echo >> /tmp/$sysmonFolder/cpu.res
	echo >> /tmp/$sysmonFolder/mem.res
	echo "sysmon times = "$times >> /tmp/$sysmonFolder/times
	times=$(($times - 1))
	sleep 10
done

#kill self
kill -9 $$
