#!/bin/bash
## Stop apache2 service
/etc/init.d/apache2 stop

## Stop python server for w3c web tests
process_result=`ps ax |grep python |grep "python\ serve\.py" | cut -d ' ' -f2`

if [ -n "$process_result" ]; then
    for process_id in `echo ${process_result}`
    do
        kill ${process_id}
    done
fi

## Remove cgi libs into /usr/bin
rm -rf /usr/bin/cgi-getcookie  /usr/bin/cgi-getfield

## Remove apache2 configurations webtestingservice in /etc/apache2/sites-available
rm -rf /etc/apache2/sites-available/webtestingservice

#### Remove soft link 000-webtestingservice in /etc/apache2/sites-enabled
rm -rf /etc/apache2/sites-enabled/000-webtestingservice

## Restore /etc/hosts
sed -i '/web-platform\.test/d' /etc/hosts

## Remove server resouces
rm -rf /opt/webtestingservice
