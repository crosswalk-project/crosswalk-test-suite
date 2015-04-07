#!/bin/sh
#
#Copyright (c) 2013 Intel Corporation.
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#* Redistributions of works must retain the original copyright notice, this list
#  of conditions and the following disclaimer.
#* Redistributions in binary form must reproduce the original copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#* Neither the name of Intel Corporation nor the names of its contributors
#  may be used to endorse or promote products derived from this work without
#  specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
#INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
#OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#Authors:
#        Wang, Jing J <jing.j.wang@intel.com>
FILTER="t1, t2"
RESULT=
val=`echo -n "$QUERY_STRING" | cgi-getfield filter_value`
[ $? -eq 0 ] && FILTER="$val"

WLIST="CONTENT-TYPE"
HEADERS="AUTHORIZATION PRAGMA CONTENT-TYPE OVERWRITE IF STATUS-URI X-TEST X-PINK-UNICORN"

for item in $HEADERS; do
        match=0
        for i in $WLIST; do
                if [ "$i" = "$item" ]; then
                        match=1
                        break
                fi
        done
        key=${item//-/_}
        [ $match -eq 0 ] && key="HTTP_$key"
        val=`printenv $key`
        if [ -n "$FILTER" -a "$val" = "$FILTER" ]; then
                typeset -l v
                v=${item}
                RESULT="$v,"
                break
        fi
done
echo "Content-Type: text/plain"
echo
echo -n "$RESULT"
