##License

Copyright (c) 2014 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Xia, Junchen <junchen.xia@intel.com>

##Introduction

Grunt is an automatic task runner, you can find more information about Grunt at [here](http://gruntjs.com/).
This tool aims to format all the html, css and javascript files in the webtest project, all related filenames should be named correctly: .html/.xml .css .js/.json

##Prepare

Check node version by:
```
node -v //Make sure your node version >= 0.8.0
```
To ubuntu 12.04 users, since there is no latest node and npm in official repo. So install npm and nodejs by:
```
sudo add-apt-repository ppa:richarvey/nodejs
sudo apt-get update
sudo apt-get install nodejs npm
```

If this is the first time you run Grunt, make sure you have installed npm and run this command:
```
sudo npm install -g grunt-cli
```
If there is any network connection problem, try to set up the proxy for npm by:
```
npm config set proxy http://xxx.com
npm config set https-proxy http://xxx.com
```
where `xxx.com` should be your proxy address.

Finally, execute:
```
./install.sh
```

##Usage

There are two tasks configured in Gruntfile.js, you can run them by:

-  `grunt all`
       Format all files located in webtest according to rules in Gruntfile.js.

-  `grunt dir --target=foldername`
       Format one or more folders, which located relatively to the webtest top directory.
       Specific:
1. for one folder:` grunt dir --target='a'`
2. for multiple folders:`grunt dir --target='{a,b,c}'`

More options can be configured in Gruntfile.js

##More

This plugin is based on [grunt-prettify](https://github.com/jonschlinkert/grunt-prettify), [grunt-cssbeautifier](https://github.com/sexnothing/grunt-cssbeautifier), [js-beautify](https://github.com/einars/js-beautify).
