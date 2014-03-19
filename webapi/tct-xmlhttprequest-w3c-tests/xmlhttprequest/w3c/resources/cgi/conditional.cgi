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

TAG=
DATE=

val=`echo -n "$QUERY_STRING" | cgi-getfield tag`
[ $? -eq 0 ] && TAG="$val"

val=`echo -n "$QUERY_STRING" | cgi-getfield date`
[ $? -eq 0 ] && DATE="$val"

if [ -n "$TAG" -a "$HTTP_IF_NONE_MATCH" = "$TAG" ]; then
        echo "Status: 304 SUPERCOOL"
elif [ -n "$DATE" -a "$HTTP_IF_MODIFIED_SINCE" = "$DATE" ]; then
        echo "Status: 304 SUPERCOOL"
fi

[ -n "$DATE" ] && echo "Last-Modified: $DATE"
[ -n "$TAG" ] && echo "ETag: $TAG"
echo "Content-Type: text/plain"
echo
echo -n "MAYBE NOT"
