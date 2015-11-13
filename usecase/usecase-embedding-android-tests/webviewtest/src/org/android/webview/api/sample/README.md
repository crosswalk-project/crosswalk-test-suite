## Usecase Design

### 1. The [WebViewWithLayoutActivity](basic/WebViewWithLayoutActivity.java) sample shows how to load url, include:

* WebView can load url

This usecase covers following interface and methods:

* WebView interface: loadUrl method



### 2. The [WebViewWithAnimatableActivity](basic/WebViewWithAnimatableActivity.java) sample shows how to use basic functionalities of animatable WebView, include:

* Animatable WebView can be scaled down or up

This usecase covers following interface and methods:

* WebView interface: loadUrl, getAlpha, getScaleX, getScaleY method



### 3. The [WebViewWithLoadDataWithBaseURL](basic/WebViewWithLoadDataWithBaseURL.java) sample shows how WebView load local html and image, include:

* WebView can load local data, etc html, image

This usecase covers following interface and methods:

* WebView interface: loadDataWithBaseURL method



### 4. The [WebViewWithMultiInstanceActivity](basic/WebViewWithMultiInstanceActivity.java) sample shows how to create multi instance, include:

* WebView can create multi instance

This usecase covers following interface and methods:

* WebView interface: loadUrl method



### 5. The [WebViewWithPlayVideoActivity](basic/WebViewWithPlayVideoActivity.java) sample shows WebView can play html5 video, include:

* WebView can play html5 video

This usecase covers following interface and methods:

* WebView interface: loadUrl method



### 6. The [WebViewWithPauseTimerActivity](basic/WebViewWithPauseTimerActivity.java) sample shows WebView can pause and resume timer, include:

* WebView can pause and resume timer

This usecase covers following interface and methods:

* WebView interface: loadUrl, pauseTimers, resumeTimers method



### 7. The [WebViewWithScrollViewParent](basic/WebViewWithScrollViewParent.java) sample check WebView inside a scrollview can display, include:

* WebView inside a scrollview can display

This usecase covers following interface and methods:

* WebView interface: loadUrl methods



### 8. The [WebViewWithMultiInstanceOverlay](basic/WebViewWithMultiInstanceOverlay.java) sample check two webviews filling in the same parent view can be displayed dynamically, include:

* Two webviews filling in the same parent view can be displayed dynamically

This usecase covers following interface and methods:

* WebView interface: loadUrl, setVisibility, getVisibility methods



### 9. The [WebViewWithClients](client/WebViewWithClients.java) sample check WebView's WebViewClient & WebChromeClient override methods can be invoked when webview load a url, include:

* WebView's WebViewClient & WebChromeClient

This usecase covers following interface and methods:

* WebView interface: loadUrl method
* WebViewClient interface: doUpdateVisitedHistory, onLoadResource, onPageFinished, onPageStarted, shouldOverrideUrlLoading methods
* WebChromeClient interface: getVisitedHistory, onProgressChanged, onReceivedTitle, onReceivedTouchIconUrl methods



### 10. The [WebViewWithNavigation](misc/WebViewWithNavigation.java) sample sample demonstrates how to forward and backward history, include:

* WebView can backward history client when go backward button is clicked
* WebView can forward history client when go forward button is clicked

This usecase covers following interface and methods:

* WebView interface: loadUrl, canGoBack, canGoForward, goBack, goForward, copyBackForwardList method
* WebHistoryItem interface: getUrl, getOriginalUrl, getTitle methods



### 11. The [WebViewWithOnReceivedIcon](client/WebViewWithOnReceivedIcon.java) sample demonstrates how to load icon when it's available, include:

* WebView can load icon when it's available

This usecase covers following interface and methods:

* WebView interface: loadUrl method
* WebChromeClient interface: onReceivedIcon method



### 12. The [WebViewWithOnCreateWindow](client/WebViewWithOnCreateWindow.java) sample demonstrates how to create new window, include:

* WebView can create new window

This usecase covers following interface and methods:

* WebView interface: loadUrl method
* WebChromeClient interface: onCreateWindow method



### 13. The [WebViewWithFullScreenActivity](basic/WebViewWithFullScreenActivity.java) sample demonstrates how to enter and exit fullscreen, include:

* WebView can enter and exit fullscreen

This usecase covers following interface and methods:

* WebView interface: loadUrl method



### 14. The [WebViewWithShouldOverrideUrlLoading](client/WebViewWithShouldOverrideUrlLoading.java) sample demonstrates how to trigger shouldOverrideUrlLoading method, include:

* WebView can trigger shouldOverrideUrlLoading method

This usecase covers following interface and methods:

* WebView interface: loadUrl method
* WebViewClient interface: shouldOverrideUrlLoading methods



### 15. The [WebViewWithTransparent](basic/WebViewWithTransparent.java) sample check WebView's transparent feature, include:

* WebView's transparent can display

This usecase covers following interface and methods:

* WebView interface: loadUrl, setBackgroundColor methods



### 16. The [WebViewWithClearCache](basic/WebViewWithClearCache.java) sample check whether WebView can clear cache, include:

* WebView can clear cache

This usecase covers following interface and methods:

* WebView interface: loadUrl, clearCache methods
* WebViewClient interface: onPageFinished methods



### 17. The [WebViewWithOnShowFileChooser](client/WebViewWithOnShowFileChooser.java) sample check WebView can open local file, include:

* WebChromeClient.onShowFileChooser can be invoked

This usecase covers following interface and methods:

* WebView interface: WebChromeClient.onShowFileChooser methods