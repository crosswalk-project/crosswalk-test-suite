// Copyright (c) 2016 Intel Corporation. All rights reserved.

using System;

namespace xwalk
{
    public class XWalkExtensionInstance
    {
        public XWalkExtensionInstance(dynamic native)
        {
            native_ = native;
        }

        public void HandleMessage(String message)
        {
            native_.PostMessageToJS("From dll async:" + message);
        }
        public void HandleSyncMessage(String message)
        {
            native_.SendSyncReply("From dll sync:" + message);
        }
        private dynamic native_;
    }
}
