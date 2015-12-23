#!/bin/bash
##
# This tool is used to seperate and group test files according to their license
# for Code (IP) Scan.
#
# Copyright (c) 2015 Intel Corporation.
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
#    You, Yi <yi.you@intel.com>
#    Zhang, Zhiqiang <zhiqiang.zhang@intel.com>


# How to use:
#     1.This shell need to run under /bin/bash.
#     2.Need 2 parameters: <project/sub-project folder> <dest-folder>
#       For now just allowed to use project folder(tct level) or sub-project folder(tct/webapi level).
#       If using this shell-script on other folder, just Header-scaning and COPYING-scanning work.
#       example:
#       -using sub-project folder: <tools/License/>$ ./license.sh ./webapi ./webapi_splitted
#       -using project folder: <tools/License/>$ ./license.sh ./tct ./tct_splitted

# Execute step:
#     step 1: Header-scaning
#     step 2: Manually-operation:
#             -Move all 'blacklist.*' to Intel_folder
#             -Move all 'Makefile.*' to Intel_folder
#     step 3: COPYING-scanning
#     step 4: Manually-operation:
#             -Move all 'jquery.*' and 'jquery-*'
#             -Move all 'config.xml' and 'icon.png' under wrt-tests
#             -Move files under sub-project/ (not include sub-dir)
#             -Move files under sub-project/doc (not include sub-dir)
#             -Move files under sub-project/packaging (not include sub-dir)
#             -Move files under sub-project/tct-testconfig (not include sub-dir)
#             -Move files under rootdir/.../.../w3c (level >= 3) (not include sub-dir)
#             -Move files under rootdir/.../.../webkit (level >= 3)
#             -Move files under rootdir/.../.../khronos (level >= 3) (not include sub-dir)
#             -Move files under rootdir/webapi-*-usage-tests folder
#             -Move files under rootdir/-*(suite)*-tests folder
#     step 5: Unknown-license moving

##
# Input format, avoid the input such as '../webapi/', delete the character '/'
inputFormat()
{
  test_src_path="${src_path##*\/}"
  test_dest_path="${dest_path##*\/}"

  if [[ -z "${test_src_path}" ]]; then
    echo -n "Input-format: $src_path --> "
    src_path="${src_path%\/}"
    echo "$src_path"
  fi

  if [[ -z "${test_dest_path}" ]]; then
    echo -n "Input-format: $dest_path --> "
    dest_path="${dest_path%\/}"
    echo "$dest_path"
  fi

  src_root_dir="${src_path##*/}"
}

if [[ "$#" -eq "2" ]]; then
  src_path="$1"   #as the root path
  dest_path="$2"
  src_root_dir=""
  inputFormat
  echo " "
  echo "Move files in [$src_path] to [$dest_path]"

  for git_file in $(find "$src_path" -type d -name ".*" | grep -wv "./"); do
    rm -rf "$git_file"
    echo "deleted: $git_file"
  done

else
  echo "[ERROR] Arguments invalid: license.sh [source path] [destination path] | $#"
  exit;
fi

# Verify input path
if [[ ! -d "$src_path" ]] || [[ ! -d "$dest_path" ]]; then
  if [[ ! -d "$src_path" ]]; then
    echo "[ERROR] Path not exist: source path '$src_path'"
    echo "exit"
    exit
  fi

  if [[ ! -d "$dest_path" ]]; then
    echo -n "Destination path '$dest_path' not exist, creating ..."
    mkdir "$dest_path"
    echo " [done]"
  fi
fi

##
# Creat folders function define
defineFolders()
{
  echo " "
  dest_IntelBSD_folder="$dest_path/IDS_BSD3_License/"
  dest_IntelGPLv2_folder="$dest_path/IDS_GPLv2_License/"
  dest_Samsung_folder="$dest_path/TPC_Apache_License/"
  dest_Flora_folder="$dest_path/TPC_Flora_License/"
  dest_W3C_folder="$dest_path/TPC_W3C-BSD_License/"
  dest_Khronos_folder="$dest_path/TPC_MIT_License/"
  dest_Jquery_folder="$dest_path/TPC_MIT_License/"
  dest_WebKit_folder="$dest_path/TPC_BSD2_License/"
  dest_Chrome_folder="$dest_path/TPC_BSD3_License/"
  dest_LGPL_folder="$dest_path/TPC_LGPL_License/"
  dest_CCBY_folder="$dest_path/TPC_CCBY_License/"
  dest_Zlib_folder="$dest_path/TPC_ZLIB_License/"
  dest_Unknown_folder="$dest_path/Unknown_License/"
}

##
# Core function: Make-dir and Move
makeMove()
{
  if [[ "$#" -eq "2" ]]; then
    s_path="$1"
    d_path="$2"
    del_pre_path="${s_path#*$src_root_dir}"
    #echo "\ndel_pre_path: $del_pre_path"
    del_post_path="${del_pre_path%\/*}"
    mv_path="$d_path${del_post_path#*/}"
    #echo "mv_path: $mv_path"
    #echo "s_path: $s_path"
    mkdir -p "$mv_path" && mv "$s_path" "$mv_path" && echo "succees" || echo "failed"
  else
    echo "[ERROR] Arguments invalid: makeMove() [Source Path] [Destination Path] | $#"
  fi
}

##
# Folder level (Relative to <rootdir> folder: level 0)
folderLevel()
{
  if [[ "$#" -eq "1" ]]; then
    if [[ -d "$1" ]]; then
      path="$1"
      level=0
      while [[ -d "$path" ]]; do
        if [[ "$path" -ef "$src_path" ]]; then
          echo "$level"
          return
        fi
        path="${path%\/*}"
        level=$((level + 1))
      done
      echo "-1"
      return
    else
      echo "folderLevel(): not a directory"
    fi
  else
    echo "[ERROR] Arguments invalid: folderLevel() [Folder Path] | $#"
  fi
}

##
# Remove the empty directories in rootdir to make the scanning faster.
clearEmptyDir()
{
  echo "Clearing empty directories ..."
  find "$src_path" -type d ! -name '.' -exec rmdir -p {} \; 2>/dev/null
  echo " "
}


###############################  BY HEADER  ##############################

##
# Define scanning function based on header
scanHeader()
{
  if [[ "$#" -eq "2" ]]; then
    count=1
    for file in $1; do
      if [[ -n "$file" ]]; then
        echo -n "$count Executing: $file - "
        makeMove "$file" "$2"
        count=$((count+1))
      fi
    done
    echo "$((count-1)) files been written: $2" | tee -a ./counter.log
  else
    echo "[ERROR] Arguments invalid: scanHeader() [Source Path] [Destination Path] | $#"
  fi
}

# Creat destination folder
defineFolders
echo " "
echo "------------------------ START BY HEADER ------------------------" | tee ./counter.log
echo " "
echo "Start scanning files for License, please waiting..."
start_sec=$(date -d this-day +%s)

# Samsung: Apache License 2.0
# HEADER:  'Copyright (c) 2013 Samsung Electronics Co., Ltd.' with 'Apache License'
echo " "
echo "Scanning SAMSUNG Apache License 2.0 Header" | tee -a ./counter.log
SAMSUNG_Apache_Header=$(grep -rli "Copyright .* Samsung Electronics" "$src_path" | grep -v "COPYING")
scanHeader "$SAMSUNG_Apache_Header" "$dest_Samsung_folder"

# Samsung: Apache License 2.0
# HEADER:  'http://www.apache.org/licenses/LICENSE-2.0'
echo " "
echo "Scanning Apache License 2.0 Header" | tee -a ./counter.log
Apache_Header=$(grep -rli "http://www.apache.org/licenses/LICENSE-2.0" "$src_path")
scanHeader "$Apache_Header" "$dest_Samsung_folder"

# Flora License
# HEADER:  'Flora License'
echo " "
echo "Scanning Flora License Header" | tee -a ./counter.log
FLORA_Header=$(grep -rli "Flora.*License" "$src_path" | grep -Ev "COPYING|LICENSE.Flora")
scanHeader "$FLORA_Header" "$dest_Flora_folder"

# JQuery: MIT License
# HEADER: 'MIT'
echo " "
echo "Begining scanning jQuery MIT License" | tee -a ./counter.log
JQUERY_MIT_Header=$(grep -rli "jquery.org" "$src_path" | xargs grep -lw "MIT" | grep -v "COPYING")
scanHeader "$JQUERY_MIT_Header" "$dest_Jquery_folder"

# Khronos: MIT License
# COPYING: 'MIT'
echo " "
echo "Scanning Khronos MIT License" | tee -a ./counter.log
KHRONOS_MIT_Header=$(grep -rli "Copyright .* Khronos Group Inc" "$src_path" | grep -v "COPYING")
scanHeader "$KHRONOS_MIT_Header" "$dest_Khronos_folder"

# W3C: Dual License: 3-clause BSD License and W3C Test Suite License
# COPYING: 'dual-licensed'
echo " "
echo "Scanning W3C Dual License" | tee -a ./counter.log
W3C_DUAL_Header=$(grep -rwli "w3c" "$src_path" | xargs grep -E -li "dual.*licensed|Test.*Suite.*License|3.*clause.*BSD.*License" | grep -E -v "COPYING|jquery*")
scanHeader "$W3C_DUAL_Header" "$dest_W3C_folder"

# Chrome: BSD 3-Clause License
# http://src.chromium.org/viewvc/chrome/trunk/src/LICENSE
# HEADER: 'BSD-style license', 'Chromium Authors'
echo " "
echo "Scanning Chrome BSD 3-Clause License" | tee -a ./counter.log
CHROME_BSD_Header=$(grep -rli "BSD-style license" "$src_path" | xargs grep -li "Chromium Authors")
scanHeader "$CHROME_BSD_Header" "$dest_Chrome_folder"

# Crosswalk: BSD 3-Clause License
# https://github.com/crosswalk-project/crosswalk/blob/master/LICENSE
# HEADER: 'BSD-style license', 'Intel'
echo " "
echo "Scanning Crosswalk BSD 3-Clause License" | tee -a ./counter.log
CHROME_BSD_Header=$(grep -rli "BSD-style license" "$src_path" | xargs grep -li "Intel")
scanHeader "$CHROME_BSD_Header" "$dest_IntelBSD_folder"

# Intel: GPL 2.0
# HEADER:  'Copyright (c) 2012 Intel Corporation.' with 'General Public License'
# FILE:  <testsuite>/testkit/web/index.html, <testsuite>/testkit/web/testrunner.js
echo " "
echo "Scanning Intel GPLv2 License Header" | tee -a ./counter.log
INTEL_GPLV2_Header=$(grep -E -rli "General Public License|GPL Version 2 license" "$src_path" | grep -Ev "COPYING|jquery*")
scanHeader "$INTEL_GPLV2_Header" "$dest_IntelGPLv2_folder"

# Intel: OBL BSD License
# HEADER:  'Copyright (c) 2012 Intel Corporation.' or 'Copyright (c) 2013 Intel Corporation.'
# COPYING: 'Intel'
echo " "
echo "Scanning Intel OBL BSD License" | tee -a ./counter.log
INTEL_OBL_BSD_Header=$(grep -rli "Copyright .* Intel Corporation" "$src_path" | xargs grep -Li "General Public License" | grep -v "COPYING")
scanHeader "$INTEL_OBL_BSD_Header" "$dest_IntelBSD_folder"

# SIMD: Zlib License
# https://github.com/johnmccutchan/ecmascript_simd/blob/master/LICENSE.txt
# HEADER: 'commercial applications'
echo " "
echo "Scanning SIMD License" | tee -a ./counter.log
SIMD_Header=$(grep -rli "commercial applications" "$src_path")
scanHeader "$SIMD_Header" "$dest_Zlib_folder"

# CCBY: CC BY 3.0
# HEADER:  'http://creativecommons.org/'
echo " "
echo "Scanning CC BY 3.0 Header" | tee -a ./counter.log
CCBY_Header=$(grep -rli "http://creativecommons.org/" "$src_path")
scanHeader "$CCBY_Header" "$dest_CCBY_folder"

echo " "
end_sec=$(date -d this-day +%s)
cost=$((end_sec - start_sec))
echo "----------------- END BY HEADER cost:$cost seconds -----------------" | tee -a ./counter.log
echo " " | tee -a ./counter.log

clearEmptyDir


#############################  BY MANUAL SET  ##############################

##
# Intel GPLv2 License from testkit-lite
# pack.sh
# testcase.xsl
# testresult.xsl
# tests.css
moveTestkite()
{
  count=1
  files_from_testkit=$(find "$src_path" -type f -name "pack.sh" -o -type f -name "testcase.xsl" -o -type f -name "testresult.xsl" -o -type f -name "tests.css")
  for ft in $files_from_testkit; do
    echo -n "$count executing: $ft -"
    makeMove "$ft" "$dest_IntelGPLv2_folder"
    count=$((count+1))
  done
  echo "(MANUAL SET) moveTestkite: $((count-1)) files been written." | tee -a ./counter.log
  echo " "
}

##
# Intel BSD3 License for Intel developed scripts
# autogen
# configure.ac
# config.xml.crx
# config.xml.wgt
# icon.png
# inst.sh.apk
# inst.sh.ivi
# inst.sh.wgt
# inst.sh.xpk
# Makefile.am
# manifest.json
# tests.full.xml
# tests.xml
# *.spec
# subtestresult.xml
moveTestScripts()
{
  count=1
  files_by_intel=$(find "$src_path" -type f -name "autogen" -o -type f -name "configure.ac" -o -type f -name "config.xml*" -o -type f -name "icon.png" -o -type f -name "inst.sh*" -o -type f -name "Makefile.*" -o -type f -name "manifest.json" -o -type f -name "tests*xml*" -o -type f -name "*.spec" -o -type f -name "subtestresult.xml")
  for fm in $files_by_intel; do
    echo -n "$count executing: $fm -"
    makeMove "$fm" "$dest_IntelBSD_folder"
    count=$((count+1))
  done
  echo "(MANUAL SET) moveTestScripts.*: $((count-1)) files been written." | tee -a ./counter.log
  echo " "
}

##
# W3C Dual License from testharness.js
# idlharness.js
# testharness.css
# testharness.js
# testharnessreport.js
# webidl2.js
# WebIDLParser.js
moveTestharness()
{
  count=1
  files_from_testharness=$(find "$src_path" -type f -name "idlharness.js" -o -type f -name "testharness.css" -o -type f -name "testharness.js" -o -type f -name "testharnessreport.js" -o -type f -name "webidl2.js" -o -type f -name "WebIDLParser.js")
  for ft in $files_from_testharness; do
    echo -n "$count executing: $ft -"
    makeMove "$ft" "$dest_W3C_folder"
    count=$((count+1))
  done
  echo "(MANUAL SET) moveTestharness: $((count-1)) files been written." | tee -a ./counter.log
  echo " "
}

echo "------------------------ START MANUAL SET ------------------------" | tee -a ./counter.log
start_sec=$(date -d this-day +%s)

moveTestkite
moveTestScripts
moveTestharness

end_sec=$(date -d this-day +%s)
cost=$((end_sec - start_sec))
echo "--------------- END MANUAL SET cost:$cost seconds ---------------" | tee -a ./counter.log
echo " " | tee -a ./counter.log

clearEmptyDir



##############################  BY COPYING  ##############################

# Define KEY in 'COPYING'
INTEL_BSD_KEY="THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION"
SAMSUNG_Apache_KEY="Copyright .* Samsung Electronics"
FLORA_KEY="Flora.*License"
INTEL_GPLV2_KEY="GNU General Public License|GPL Version 2 license"
W3C_DUAL_KEY="dual.*license|W3C Test Suite License"
KHRONOS_MIT_KEY="Khronos Group.*MIT|Khronos.*license"
WEBKIT_BSD_KEY="webkit.*license"
LGPL_KEY="Lesser General Public License"

##
# KEY-Destination matching
keydestMatch()
{
  key="$1"
  if [[ "$key" = "$INTEL_BSD_KEY" ]]; then
    echo "$dest_IntelBSD_folder"
  elif [[ "$key" = "$SAMSUNG_Apache_KEY" ]]; then
    echo "$dest_Samsung_folder"
  elif [[ "$key" = "$FLORA_KEY" ]]; then
    echo "$dest_Flora_folder"
  elif [[ "$key" = "$INTEL_GPLV2_KEY" ]]; then
    echo "$dest_IntelGPLv2_folder"
  elif [[ "$key" = "$W3C_DUAL_KEY" ]]; then
    echo "$dest_W3C_folder"
  elif [[ "$key" = "$KHRONOS_MIT_KEY" ]]; then
    echo "$dest_Khronos_folder"
  elif [[ "$key" = "$WEBKIT_BSD_KEY" ]]; then
    echo "$dest_WebKit_folder"
  elif [[ "$key" = "$LGPL_KEY" ]]; then
    echo "$dest_LGPL_folder"
  else
    echo "[ERROR] Wrong KEY: $key"
    exit 1
  fi
  return
}

##
# Define scanning function based on 'COPYING'
# For each directory, try to find the file 'COPYING'; and find out what license in 'COPYING'
findCopying()
{
  for copying_file in $(find "$src_path" -type f -name "COPYING"); do
    copying_dir="${copying_file%\/COPYING}"

    # Count the times to make sure which license is in COPYING
    INTEL_BSD_Inside=$(grep -E -ci "$INTEL_BSD_KEY" "$copying_file")
    SAMSUNG_Apache_Inside=$(grep -E -ci "$SAMSUNG_Apache_KEY" "$copying_file")
    Flora_Inside=$(grep -E -ci "$FLORA_KEY" "$copying_file")
    INTEL_GPLV2_Inside=$(grep -E -ci "$INTEL_GPLV2_KEY" "$copying_file")
    W3C_DUAL_Inside=$(grep -E -ci "$W3C_DUAL_KEY" "$copying_file")
    KHRONOS_MIT_Inside=$(grep -E -ci "$KHRONOS_MIT_KEY" "$copying_file")
    WEBKIT_BSD_Inside=$(grep -E -ci "$WEBKIT_BSD_KEY" "$copying_file")
    LGPL_Inside=$(grep -E -ci "$LGPL_KEY" "$copying_file")
    isMulti=-1   #-1 means error

    declare -a arguments_list

    # Check Single/Multi/Unknown License
    if [[ "$INTEL_BSD_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$INTEL_BSD_KEY"
    fi

    if [[ "$SAMSUNG_Apache_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$SAMSUNG_Apache_KEY"
    fi

    if [[ "$Flora_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$FLORA_KEY"
    fi

    if [[ "$INTEL_GPLV2_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$INTEL_GPLV2_KEY"
    fi

    if [[ "$W3C_DUAL_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$W3C_DUAL_KEY"
    fi

    if [[ "$KHRONOS_MIT_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$KHRONOS_MIT_KEY"
    fi

    if [[ "$WEBKIT_BSD_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$WEBKIT_BSD_KEY"
    fi

    if [[ "$LGPL_Inside" -gt "0" ]]; then
      isMulti=$((isMulti + 1))
      arguments_list[$isMulti]="$LGPL_KEY"
    fi

    # Different operations for Single/Multi License
    if [[ "$isMulti" -eq "-1" ]]; then
      echo "[Warning] Unknown License: $copying_file"
    elif [[ "$isMulti" -eq "0" ]]; then
      echo "Single-License: $copying_file"
      locateByCopying "$copying_dir" "${arguments_list[*]}"
      unset arguments_list
    elif [[ "$isMulti" -gt "0" ]]; then
      echo "Multi-License: $copying_file"
      #echo -n "| Intel_BSD:$INTEL_BSD_Inside | "
      #echo -n "SAMSUNG:$SAMSUNG_Apache_Inside | "
      #echo -n "intel_GPLv2:$INTEL_GPLV2_Inside | "
      #echo -n "W3C_DUAL:$W3C_DUAL_Inside | "
      #echo -n "Khronos:$KHRONOS_MIT_Inside | "
      #echo -n "WEBKIT：$WEBKIT_BSD_Inside | "
      #echo "LGPL：$LGPL_Inside |"
      #echo "args num: ${#arguments_list[*]}"
      #locateByMultiCopying "$copying_dir" "${arguments_list[@]}"  #must use [@]
      unset arguments_list
    fi

    # Move COPYING away
    if [[ "$(find "$copying_dir" -maxdepth 1 -type f | wc -l)" -eq "1" ]]; then
      echo -n "[moving file: 'COPYING' to $dest_IntelBSD_folder] - "
      makeMove "$copying_file" "$dest_IntelBSD_folder"
    else
      echo "'COPYING' is not the last file. Waiting for moving to Unknown_License with other files."
    fi
    echo " "
  done
}

count_by_copying=0;

##
# For Single-license division
locateByCopying()
{
  if [[ "$#" -eq "2" ]]; then
    cpfile_dir="$1"
    single_key="$2"
    declare -a wait_to_move   #wait to move list
    declare -a deny_to_move   #handle 'except'
    declare -a filelist     #store all file in an folder
    index_w=0
    index_d=0
    index_all=0

    #Finding the destination folder
    de_folder=$(keydestMatch "$single_key")
    echo "< destination: $de_folder >"

    #Testing the files, and fill the move list.
    for file_with_copying in $(find "$cpfile_dir" -maxdepth 1 -type f ! -name "COPYING" -exec basename {} \;); do
      echo "executing:" "$file_with_copying"
      filelist[$index_all]="$file_with_copying"
      index_all=$((index_all + 1))

      #Scanning whether the file is in the 'COPYING'
      if [[ $(grep -c "$file_with_copying" "$cpfile_dir/COPYING") -gt "0" ]]; then
        #Without keyword 'except', can be moved
        if [[ $(grep -Eci "except.*$file_with_copying|$file_with_copying.*except" "$cpfile_dir/COPYING") -eq "0" ]]; then
          #Ignore this file if there is 'These tests are copyright'. Prevent the modify description mixed with the license declare on files
          if [[ $(grep -Eci "These tests are copyright.*|These tests are.*License|images are.*License" "$cpfile_dir/COPYING") -eq "0" ]]; then
            wait_to_move[$index_w]="$file_with_copying"
            index_w=$((index_w + 1))
            echo "$file_with_copying: inserted into the wait_to_move list"
          fi
        else
          deny_to_move[$index_d]="$file_with_copying"
          index_d=$((index_d + 1))
          echo "$file_with_copying: inserted into the deny_to_move list"
        fi
      fi
    done

    # Move operation
    if [[ "$index_all" -gt "0" ]]; then
      # If wait_to_move list empty, fill it
      if [[ "$index_w" -eq "0" ]]; then
        if [[ "$index_d" -eq "0" ]]; then
          echo "puting all file into wait_to_move list"
          length_all="${#filelist[@]}"
          for ((i=0;i<=length_all-1;i++)); do
            wait_to_move[$i]="${filelist[$i]}"
          done
          index_w="$length_all"
        else  #deny_to_move list existed
          echo "puting partical files into wait_to_move list"

          for p_file in "${filelist[@]}"; do
            d_flag=0
            for d_file in "${deny_to_move[@]}"; do
              if [[ "$p_file" = "$d_file" ]]; then
                d_flag=1
                break
              fi
            done

            if [[ "$d_flag" = 0 ]]; then
              wait_to_move[$index_w]="$p_file"
              index_w=$((index_w + 1))
            fi
          done
        fi
      fi

      #If wait_to_move list existed, take moving
      if [[ "$index_w" -gt "0" ]]; then
        for m_file in "${wait_to_move[@]}"; do
          echo -n "[moving list file: $m_file] - "
          makeMove "$cpfile_dir/$m_file" "$de_folder"
          count_by_copying=$((count_by_copying + 1))
        done
      fi
    fi

  unset wait_to_move
  unset deny_to_move
  unset filelist

  else
    echo "[ERROR] Arguments invalid: locateByCopying() [file_name] [single_key] | $#"
  fi
}

##
# For Multi-license division
# waiting for writing based on uniform COPYING formating
locateByMultiCopying()
{
  #if [ "$#" -gt "2" ];
  #then
    cpfile_dir="$1"
    arg_count="$#"
    for ((i=2;i<=arg_count;i++)); do
      echo "${${i}}" #arguments travel
    done
    #for file_with_copying in $(find "$copying_dir" -maxdepth 1 -type f ! -name "COPYING" -exec basename {} \;)
    #do
    #   echo "$file_with_copying"
      #locateByCopying "$file_with_copying" "$copying_dir"
    #done
  #else
    #echo "[ERROR] Arguments invalid: locateByMultiCopying() [file_name] [file_path] [[]]| $#"
  #fi
}

echo "------------------------ START BY COPYING ------------------------" | tee -a ./counter.log
start_sec=$(date -d this-day +%s)

#Scanning based on 'COPYING'
findCopying
echo "$count_by_copying files been written: BY COPYING" | tee -a ./counter.log

end_sec=$(date -d this-day +%s)
cost=$((end_sec - start_sec))
echo "--------------- END BY COPYING cost:$cost seconds ---------------" | tee -a ./counter.log
echo " " | tee -a ./counter.log

#Remove the empty directories in rootdir to make the scanning faster.
echo "Clearing empty directories after division by 'COPYING'"
find "$src_path" -type d ! -name "./" -exec rmdir -p {} \; 2>/dev/null
echo " "

##############################  BY COPYING  ##############################


#############################  BY MANUAL SET  ##############################

##
# Move folder to path, and split COPYING file.
moveCustomedFolder()
{
  if [[ "$#" -eq "2" ]]; then
    cus_folder=$1   # Relatvie path to rootdir
    cus_dest=$2
    max_depth="-1"
  elif [[ "$#" -eq "3" ]]; then
    cus_folder=$1   # Relatvie path to rootdir
    cus_dest=$2
    max_depth=$3
  else
    echo "[ERROR] Arguments invalid: moveCustomedFolder <relatvie-path> <dest-path> [move-maxdepth]"
  fi

  count=1
  count_cp=1

  if [[ "$max_depth" -eq "-1" ]]; then
    echo "Manually move files in $cus_folder folder"
    for cus_file in $(find "$cus_folder" -type f); do
      echo -n "$count executing: $cus_file -"
      if [[ "${cus_file%\/*}" != "COPYING" ]]; then
        makeMove "$cus_file" "$cus_dest"
        count=$((count+1))
      else
        echo -n " (COPYING file) -"
        makeMove "$cus_file" "$dest_IntelBSD_folder"
        count_cp=$((count_cp+1))
      fi
    done
  else
    echo "Manually move files in $cus_folder folder (maxdepth:$max_depth)"
    for cus_file in $(find "$cus_folder" -maxdepth "$max_depth" -type f); do
      echo -n "$count executing: $cus_file -"
      if [[ "${cus_file%\/*}" != "COPYING" ]]; then
        makeMove "$cus_file" "$cus_dest"
        count=$((count+1))
      else
        echo -n " (COPYING file) -"
        makeMove "$cus_file" "$dest_IntelBSD_folder"
        count_cp=$((count_cp+1))
      fi
    done
  fi

  echo "(MANUAL SET) Files under $cus_folder: [$((count-1)) files, $((count_cp-1)) COPYING] has been written." | tee -a ./counter.log
  echo " "
}

##
# Rest files subject to W3C Dual License:
# <testsuite>/<spec>/w3c/
# <testsuite>/<spec>/csswg/
moveW3C()
{
  leftDir=$(find "$src_path" -type d -name "w3c" -o -type d -name "csswg")
  for w3c_dir in $leftDir; do
    folder_level=$(folderLevel "$w3c_dir")
    echo " "
    echo "Scanning: $w3c_dir --------------- level $folder_level"
    moveCustomedFolder "$w3c_dir" "$dest_W3C_folder"
  done
}

##
# Rest files subject to Flora License:
# */LICENSE.Flora
moveFlora()
{
  leftFile=$(find "$src_path" -type f -name "LICENSE.Flora")
  for flora_file in $leftFile; do
    flora_dir="${flora_file%\/LICENSE.Flora}"
    moveCustomedFolder "$flora_dir" "$dest_Flora_folder"
  done
}

##
# Rest files subject to 2-Clause BSD License:
# <testsuite>/<spec>/webkit/
moveWebkit()
{
  leftDir=$(find "$src_path" -type d -name "webkit")
  for webkit_dir in $leftDir; do
    folder_level=$(folderLevel "$webkit_dir")
    echo " "
    echo "Scanning: $webkit_dir --------------- level $folder_level"
    moveCustomedFolder "$webkit_dir" "$dest_WebKit_folder"
  done
}

##
# Rest files subject to 3-Clause BSD License:
# <testsuite>/<spec>/blink/
moveBlink()
{
  leftDir=$(find "$src_path" -type d -name "blink")
  for blink_dir in $leftDir; do
    folder_level=$(folderLevel "$blink_dir")
    echo " "
    echo "Scanning: $blink_dir --------------- level $folder_level"
    moveCustomedFolder "$blink_dir" "$dest_Chrome_folder"
  done
}

##
# Rest files subject to MIT License:
# <testsuite>/<spec>/khronos/
moveKhronos()
{
  leftDir=$(find "$src_path" -type d -name "khronos")
  for kh_dir in in $leftDir; do
    folder_level=$(folderLevel "$kh_dir")
    echo " "
    echo "Scanning: $kh_dir --------------- level $folder_level"
    moveCustomedFolder "$kh_dir" "$dest_Khronos_folder"
  done
}

##
# Rest files subject to Intel 3-Clause BSD License:
# <testsuite>/
moveSuite()
{
  leftDir=$(find "$src_path" -type d -name "*-tests")
  for suite_dir in $leftDir; do
    moveCustomedFolder "$suite_dir" "$dest_IntelBSD_folder" "1"
  done
}

##
# Rest files subject to Flora License:
# */jquery*
moveJQuery()
{
  leftFile1=$(find "$src_path" -type d -name "jquery*" | xargs -I {} find {} -type f)
  count=1
  for per_file in $leftFile1; do
    echo -n "$count executing: $per_file -"
    makeMove "$per_file" "$dest_Jquery_folder"
    count=$((count+1))
  done

  leftFile2=$(find "$src_path" -type f -name "jquery.*" -o -type f -name "jquery-*")
  for jquery_file in $leftFile2; do
    echo -n "$count executing: $jquery_file -"
    makeMove "$jquery_file" "$dest_Jquery_folder"
    count=$((count+1))
  done
  echo "(MANUAL SET) jquery.*: $((count-1)) files been written." | tee -a ./counter.log
  echo " "
}

##
# Rest files subject to Zlib License:
# */ecmascript_simd*
moveSIMD()
{
  leftDir=$(find "$src_path" -type d -name "ecmascript_simd")
  for zlib_dir in in $leftDir; do
    folder_level=$(folderLevel "$zlib_dir")
    echo " "
    echo "Scanning: $zlib_dir --------------- level $folder_level"
    moveCustomedFolder "$zlib_dir" "$dest_Zlib_folder"
  done
}

##
# Rest files subject to Samsung Apache 2.0 License:
# tools/signing/
movesigning()
{
  leftDir=$(find "$src_path" -type d -name "signing")
  for lf_dir in in $leftDir; do
    folder_level=$(folderLevel "$lf_dir")
    echo " "
    echo "Scanning: $lf_dir --------------- level $folder_level"
    moveCustomedFolder "$lf_dir" "$dest_Samsung_folder"
  done
}

echo "------------------------ Start MANUAL SET ------------------------" | tee -a ./counter.log
start_sec=$(date -d this-day +%s)

moveJQuery
moveW3C
moveFlora
moveWebkit
moveBlink
moveKhronos
moveSuite
moveSIMD
movesigning

end_sec=$(date -d this-day +%s)
cost=$((end_sec - start_sec))
echo "--------------- End MANUAL SET cost:$cost seconds ---------------" | tee -a ./counter.log
echo " " | tee -a ./counter.log

clearEmptyDir



############################  Manual Indentification  ##############################

##
moveManualIndentification()
{
  count=1

  # Intel: BSD 3-Clause License
  files=$(find "$src_path" -type f -name "*100x100.png" -o -type f -name "pass.png" -o -type f -name "fail.png" -o -type f -name "config.xml*" -o -type f -name "*.changes" -o -type f -name "*.pdf" -o -type f -name "preconfigure.json" -o -type f -name "tct-testconfig.ini" -o -type f -name "testlist.json" -o -type f -name "flowser.png" -o -type f -name "LICENSE.BSD-3" -o -type f -name "LICENSE" -o -type f -name "COPYING" -o -type f -name "icon-128.png")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_IntelBSD_folder"
    count=$((count+1))
  done

  # Intel: GPLv2 License
  files=$(find "$src_path" -type f -name "back_top.png" -o -type f -name "application.js")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_IntelGPLv2_folder"
    count=$((count+1))
  done

  # JQuery: MIT License
  files=$(find "$src_path" -type f -name "ajax-loader.gif" -o -type f -name "icons*black.png" -o -type f -name "icons*white.png" -o -type f -name "slider.tooltip.js" -o -type f -name "jqueryprogressbar.js")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_Jquery_folder"
    count=$((count+1))
  done

  # Samsung: Apache License 2.0
  files=$(find "$src_path" -type f -name "LICENSE.Apache-2.0")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_Samsung_folder"
    count=$((count+1))
  done

  # W3C: Dual License
  files=$(find "$src_path" -type f -name "1x1-white.png" -o -type f -name "a-green.css" -o -type f -name "canvas-index.css" -o -type f -name "CanvasTest.ttf" -o -type f -name "csstest-basic-bold.ttf" -o -type f -name "11*wgt" -o -type f -name "blue.png")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_W3C_folder"
    count=$((count+1))
  done

  # WebKit: BSD 2-Clause License
  files=$(find "$src_path" -type f -name "ring.png" -o -type f -name "LICENSE.BSD-2")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_WebKit_folder"
    count=$((count+1))
  done

  # Khronos: MIT License
  files=$(find "$src_path" -type f -name "red-green*" -o -type f -name "LICENSE.MIT")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_Khronos_folder"
    count=$((count+1))
  done

  # Meego: LGPLv2.1
  files=$(find "$src_path" -type f -name "PNG_512x512_318Kb_BBB.png" -o -type f -name "LICENSE.LGPL")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_LGPL_folder"
    count=$((count+1))
  done

  # CC BY
  files=$(find "$src_path" -type f -name "LICENSE.CC-BY-3.0" -o -type f -name "Test*" -o -type f -name "*_wgt" -o -type f -name "audio.*" -o -type f -name "image.*" -o -type f -name "video.*" -o -type f -name "icon[AV].png" -o -type f -name "noti*png" -o -type f -name "noti*wav" -o -type f -name "*tizen*png" -o -type f -name "*tizen*jp*g" -o -type f -name "*tizen*mp*" -o -type f -name "*xpk_generator*")
  for f in $files; do
    echo -n "$count executing: $f -"
    makeMove "$f" "$dest_CCBY_folder"
    count=$((count+1))
  done

  echo "(MANUAL SET) moveTestScripts.*: $((count-1)) files been written." | tee -a ./counter.log
  echo " "
}

moveManualIndentification

clearEmptyDir


############################  UNKNOWN LICENSE  ##############################

##
# Rest files subject to Default License
moveDefault()
{
  echo "Moving Unknown-License Files to : $dest_IntelBSD_folder" | tee -a ./counter.log
  count=1
  leftFile=$(find "$src_path" -type f)
  for un_file in $leftFile; do
    echo -n "$count Moving Unknown:" "$un_file -"
    makeMove "$un_file" "$dest_IntelBSD_folder"
    count=$((count+1))
  done
  echo "Unknown License: $((count-1)) files been written." | tee -a ./counter.log
  echo " "
}

moveDefault

clearEmptyDir


echo "############################### RESULT ###############################"
echo " "
cat ./counter.log
echo " "
echo "############################### RESULT ###############################"
echo " "
