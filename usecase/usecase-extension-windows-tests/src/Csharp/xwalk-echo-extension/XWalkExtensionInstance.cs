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
            if (string.Equals(message, "BinaryTest", StringComparison.OrdinalIgnoreCase))
            {
                byte[] bytes = new byte[] { 1, 2, 3, 4, 5, 6, 7, 8 };
                native_.PostBinaryMessageToJS(bytes, (ulong)bytes.Length);
            }
            else
            {
                native_.PostMessageToJS("From dll async:" + message);
            }
        }
        public void HandleSyncMessage(String message)
        {
            native_.SendSyncReply("From dll sync:" + message);
        }
        private dynamic native_;
    }
}
