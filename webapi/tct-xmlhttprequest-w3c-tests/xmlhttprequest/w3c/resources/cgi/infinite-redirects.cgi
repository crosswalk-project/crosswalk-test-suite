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
#        Lin, Wanming <wanmingx.lin@intel.com>

echo "Server: Mongoose/1.3 (Linux)"
# The infinite redirect script.

location="http://$HTTP_HOST$SCRIPT_NAME"
page="alternate"
type=302
mix=0

val=`echo -n "$QUERY_STRING" | cgi-getfield page`
if [ $? -eq 0 ] && [ $val=="alternate" ]; then
        page="default"
fi

val=`echo -n "$QUERY_STRING" | cgi-getfield type`
if [ $? -eq 0 ] && [ $val -eq 301 ]; then
        type=301
fi

val=`echo -n "$QUERY_STRING" | cgi-getfield mix`
if [ $? -eq 0 ] && [ $val -eq 1 ]; then
        mix=1
        if [ $type -eq 301 ]; then
            type=302
        else
            type=301
        fi
fi

newLocation="$location?page=$page&type=$type&mix=$mix"
echo "Cache-Control: no-cache"
echo "Pragma: no-cache"
echo "Status: 301"
echo "Location: $newLocation"
echo "Content-Type: text/html"
echo

echo "Hello guest. You have been redirected to $newLocation"
