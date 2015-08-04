package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.ClientCertRequest;

public class OnReceivedClientCertRequestHelper extends CallbackHelper{

	private ClientCertRequest mHandler;
	
	public void notifyCalled(ClientCertRequest handler) {
		mHandler = handler;
		notifyCalled();
	}
	
	public ClientCertRequest getHandler() {
		assert getCallCount() > 0;
		return mHandler;
	}   
}
