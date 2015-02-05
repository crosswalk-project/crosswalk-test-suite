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
#         Fan, Yugang <yugang.fan@intel.com>

import os
import re
import subprocess
import string

#XW_ENV = "export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket"


def do_cmd(cmd):
    output = []
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        cmd_return_code = cmd_proc.poll()
        if cmd_return_code is not None:
            break

    if not cmd.endswith("&"):
        while True:
            line = cmd_proc.stdout.readline().strip("\r\n")
            print line
            if not line or line.find("daemon started") >= 0:
                break
            output.append(line)

    return (cmd_return_code, output)

def get_user_id(mode,device,tizen_user=None):
    cmd = ''
    try:
       if not tizen_user:
          tizen_user = 'app'
       if mode == "SDB" :
          cmd = "sdb -s %s shell id -u %s" % (device, tizen_user)
       else:
          cmd = "ssh %s \"id -u %s\"" % (device, tizen_user)
       user_info =  do_cmd(cmd)
       user_id = user_info[1][0]
    except Exception as e:
       print "Failed to get user_id: %s" % e 
       return None
    return  user_id
    
def update_cmd(xw_env,cmd=None):
    if "app_launcher -l" in cmd:
        cmd = "su - app -c '%s;%s'" % (xw_env, cmd)
    return cmd

def get_appid_by_name(app_name=None, platform=None, tizen_user=None):
    mode = "SDB"
    if "comm-mode" in platform and platform["comm-mode"] != "" and platform[
            "comm-mode"].upper().find('SSH') >= 0:
        mode = "SSH"

    device = ""
    if "device" not in platform or platform["device"] == "":
        (return_code, output) = do_cmd("sdb devices")
        for line in output:
            if str.find(line, "\tdevice") != -1:
                device = line.split("\t")[0]
                break
    else:
        device = platform["device"]

    user_id = get_user_id(mode,device,tizen_user)
    user_is_valid = re.match(r'^[0-9]*$',user_id)
    if not user_is_valid:
       print "User %s does not exist, exit" % tizen_user

    xw_env = "export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + str(user_id) + "/dbus/user_bus_socket"

    if mode == "SSH":
        cmd = "ssh %s \"%s\"" % (
            device, update_cmd(xw_env,'app_launcher -l'))
    else:
        cmd = "sdb -s %s shell %s" % (
            device, update_cmd(xw_env,'app_launcher -l'))

    (return_code, output) = do_cmd(cmd)
    if return_code != 0:
        return ""

    test_app_id = ""
    for line in output:
        line_sections = line.strip("\r\n").split()
        print line_sections
        if len(line_sections) == 1:
            continue
        i_name = line_sections[0].strip("\'")
        if app_name == i_name:
            test_app_id = line_sections[1].strip("\'")
            break
    print "Got app-id of %s: %s" % (app_name, test_app_id)
    return test_app_id
