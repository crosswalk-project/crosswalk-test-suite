#!/usr/bin/env python

# Copyright (c) 2014 Intel Corporation. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Copy common resource to test suites with testharness.
"""

import os
import shutil
import sys
import stat
from optparse import OptionParser

PARAMETERS = None

def overwriteCopy(src, dest, symlinks=False, ignore=None):
    if not os.path.exists(dest):
        os.makedirs(dest)
        shutil.copystat(src, dest)
    sub_list = os.listdir(src)
    if ignore:
        excl = ignore(src, sub_list)
        sub_list = [x for x in sub_list if x not in excl]
    for i_sub in sub_list:
        s_path = os.path.join(src, i_sub)
        d_path = os.path.join(dest, i_sub)
        if symlinks and os.path.islink(s_path):
            if os.path.lexists(d_path):
                os.remove(d_path)
            os.symlink(os.readlink(s_path), d_path)
            try:
                s_path_s = os.lstat(s_path)
                s_path_mode = stat.S_IMODE(s_path_s.st_mode)
                os.lchmod(d_path, s_path_mode)
            except Exception:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)

def doCopy(src_item=None, dest_item=None):
    print("Copying %s to %s" % (src_item, dest_item))
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                print("Create non-existent dir: %s" %
                         os.path.dirname(dest_item))
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception as e:
        print("Fail to copy file %s: %s" % (src_item, e))
        return False

    return True

def searchDest(src_item,dest_dir):
    try:
        subdir_list = os.listdir(dest_dir)
        if dest_dir[-1] != '/':
           dest_dir += '/'
        for sub_dir in subdir_list:
           sub_dir = dest_dir + sub_dir + '/resources/testharness.js'
           if os.path.exists(sub_dir):
              dest,filename = os.path.split(sub_dir)
              doCopy(src_item,dest)
    except Exception as e:
        print("Fail to search dest dir %s: %s" % (dest_dir, e))
        return False

def main():
    try:
        usage = "Usage: ./copy.py -s /path/to/resources -p /path/to/crosswalk/webapi"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-s",
            "--src",
            dest="srcdir",
            help="specify the path of resource files")
        opts_parser.add_option(
            "-d",
            "--dest",
            dest="destdir",
            help="specify the path of destination where the resources copy to")
        if len(sys.argv) == 1:
            sys.argv.append("-h")

        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
         
        searchDest(PARAMETERS.srcdir,PARAMETERS.destdir)
        

    except Exception as e:
        print("Got wrong options: %s, exit ..." % e)
        sys.exit(1)

    if not PARAMETERS.srcdir:
        PARAMETERS.srcdir = os.getcwd()
    PARAMETERS.srcdir = os.path.expanduser(PARAMETERS.srcdir)

    

if __name__ == '__main__':
    main()
