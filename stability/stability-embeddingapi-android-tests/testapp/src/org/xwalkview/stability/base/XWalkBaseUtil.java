// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.stability.base;

import java.io.IOException;

public class XWalkBaseUtil {
    
    private static final String TOUCHONEFILE = "touch /mnt/sdcard/onPageLoadStoppedFlag";
    private static final String DELETEONEFILE = "rm -r /mnt/sdcard/onPageLoadStoppedFlag";
    
    public static void createStorageFile(boolean flag) {
        try {
            if (flag) {
                Runtime.getRuntime().exec(TOUCHONEFILE);
            }else {
                Runtime.getRuntime().exec(DELETEONEFILE);
            }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    
}
