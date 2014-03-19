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

echo "Server: Mongoose/1.3 (Linux)"

echo -n "X-Request-Method: "
if [ -n "$REQUEST_METHOD" ]; then
    echo "$REQUEST_METHOD"
else
    echo "NO"
fi

echo -n "X-Request-Query: "
if [ -n "$QUERY_STRING" ]; then
    echo "$QUERY_STRING"
else
    echo "NO"
fi

echo -n "X-Request-Content-Length: "
if [ -n "$CONTENT_LENGTH" ]; then
    echo "$CONTENT_LENGTH"
else
    echo "NO"
fi

echo -n "X-Request-Content-Type: "
if [ -n "$CONTENT_TYPE" ]; then
    echo "$CONTENT_TYPE"
else
    echo "NO"
fi
echo "Content-Type: text/plain"
echo
if [ "$REQUEST_METHOD" = "POST" ]; then
    dd count=$CONTENT_LENGTH bs=1 2> /dev/null
fi
