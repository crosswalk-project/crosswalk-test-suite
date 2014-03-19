#!/usr/bin/env bash
#
# Copyright (c) 2014 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Xia, Junchen <junchen.xia@intel.com>

warn() {
    echo "$1" >&2
}

die() {
    warn "$1"
    exit 1
}
echo "Installing node_modules..."
if [ ! -d "node_modules" ];then
    (npm install) || die "npm intall failed, check if valid npm and node installed."
fi
echo "Done."
echo "Installing optimize modules..."
if [ ! -f "js-beautify/beautify-html.js" ] || [ ! -f "grunt-prettify/prettify.js" ] || [ ! -f "js-beautify/beautify.js" ];then
    die "No valid optimize file, tool may behave unpredictably!"
fi
\cp -f js-beautify/beautify-html.js node_modules/grunt-prettify/node_modules/js-beautify/js/lib/beautify-html.js
\cp -f grunt-prettify/prettify.js node_modules/grunt-prettify/tasks/prettify.js
\cp -f js-beautify/beautify.js node_modules/grunt-prettify/node_modules/js-beautify/js/lib/beautify.js
echo "Done. See README before using the tool."
