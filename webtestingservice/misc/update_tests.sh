#!/bin/bash
server_dir=/opt/webtestingservice

#### Replace ipaddr in files
ipaddr=`ifconfig eth0 | awk '/inet/ {split($2,x,":");print x[2]}'`
replace_records=/tmp/replace_ipaddr.txt
grep -rn "MACRO_IPADDR" ${server_dir} | cut -d ':' -f1 | sort | uniq > ${replace_records}

for replace_file in `cat ${replace_records}`
do
    sed -i "s/MACRO_IPADDR/${ipaddr}/g" ${replace_file}
done

rm ${replace_records}
