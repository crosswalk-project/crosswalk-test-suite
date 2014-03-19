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
#        Liu, xin <xinx.liu@intel.com>

TYPE=
RESPONSE_CODE=200
BODY=
CONTENT_TYPE="text/plain"

if [ -n "$HTTP_IF_NONE_MATCH" ]; then
        echo "Status: 304 Not Modified"
fi

val=`echo -n "$QUERY_STRING" | cgi-getfield types`
[ $? -eq 0 ] && TYPE="$val"

case "$TYPE" in
     "audio") BODY=`cat silence.wav`
              CONTENT_TYPE="audio/wav";;
     "css") BODY=`cat gray_bg.css`
            CONTENT_TYPE="text/css";;
     "font") BODY=`cat Ahem.ttf`
             CONTENT_TYPE="application/octet-stream";;
     "iframe") BODY=`cat blank_page_green.htm`
             CONTENT_TYPE="text/html";;
     "image") BODY=`cat 1x1-blue.png`
             CONTENT_TYPE="image/png";;
     "script") BODY=`cat empty_script.js`
             CONTENT_TYPE="text/javascript";;
      *) RESPONSE_CODE="404";;
esac

echo "Status: $RESPONSE_CODE"
echo "Content-type: $CONTENT_TYPE"
echo

val=`echo -n "$QUERY_STRING" | cgi-getfield cacheable`
if [ $? -eq 0 ]; then
        echo "Etag: 7"
else
        echo "Cache-control: no-cache"
fi

echo "$BODY"
