#!/bin/bash
## Check apache2
which apache2 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Not find apache2, please install apache2 firstly."
    exit 1
fi

## Copy cgi libs into /usr/bin
current_dir=$(cd $(dirname $0);pwd)
bit_type=`uname -m`
if [ "$bit_type" == "x86_64" ]; then
    cp ${current_dir}/tools/64bits/cgi-* /usr/bin
elif [ "$bit_type" == "i686" ]; then
    cp ${current_dir}/tools/32bits/cgi-* /usr/bin
fi

## Config apache2 configurations
rm -rf /etc/apache2/sites-enabled/*
#### Create soft link 001-webtestingservice in /etc/apache2/sites-enabled
cp ${current_dir}/webtestingservice /etc/apache2/sites-available
ln -s /etc/apache2/sites-available/webtestingservice /etc/apache2/sites-enabled/000-webtestingservice

## Forbid default handling php files including cgi
result=`grep -rn "application\/x-httpd-php\([[:space:]]\)" /etc/mime.types`
if [ -n "$result" ]; then
    head_char=`echo ${result} | cut -d ':' -f2 | cut -c 1`
    if [ ${head_char} != '#' ]; then
        sed -i 's/application\/x-httpd-php\([[:space:]]\)/#application\/x-httpd-php\1/g' /etc/mime.types
    fi
fi

## Handle server resouces
server_dir=/opt/webtestingservice
if [ -d ${server_dir} ]; then
    bk_suffix=`date +%Y%m%d%H%M%S`
    mv ${server_dir} ${server_dir}_${bk_suffix}
fi

mkdir ${server_dir}

current_dir=`dirname $0`
unzip ${current_dir}/wts_tests.zip -d ${server_dir}

#### Replace ipaddr in files
ipaddr=`ifconfig eth0 | awk '/inet/ {split($2,x,":");print x[2]}'`
replace_records=/tmp/replace_ipaddr.txt

grep -rn "MACRO_IPADDR" ${server_dir} | cut -d ':' -f1 | sort | uniq > ${replace_records}

for replace_file in `cat ${replace_records}`
do
    sed -i "s/MACRO_IPADDR/${ipaddr}/g" ${replace_file}
done

rm ${replace_records}

## Restart apache2 service
/etc/init.d/apache2 restart

## Modify /etc/hosts
sed -i '/web-platform\.test/d' /etc/hosts
sed -i "s#127.0.0.1\([[:space:]]\)localhost#127\.0\.0\.1\1localhost\\n"$ipaddr"\\tweb-platform\.test\\n"$ipaddr"\\twww.web-platform.test\\n"$ipaddr"\\twww1.web-platform.test\\n"$ipaddr"\\twww2.web-platform.test\\n"$ipaddr"\\txn--n8j6ds53lwwkrqhv28a.web-platform.test\\n"$ipaddr"\\txn--lve-6lad.web-platform.test#g" /etc/hosts

## Start python server
process_result=`ps ax |grep python |grep "python\ serve\.py" | cut -d ' ' -f2`
if [ -n "$process_result" ]; then
    for process_id in `echo ${process_result}`
    do
        kill ${process_id}
    done
fi

cd ${server_dir}/suites/w3c/web-platform-tests
python serve.py&
