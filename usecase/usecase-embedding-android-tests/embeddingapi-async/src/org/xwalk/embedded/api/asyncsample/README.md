## Usecase Design

### 1. The [XWalkViewWithPreferencesAsync](misc/XWalkViewWithPreferencesAsync.java) sample demonstrates XWALK-2376 feature basic functionalities, include:

* XWalkView can set style value
* XWalkView can get style value

This usecase covers following interface and methods:

* XWalkPreferences interface: setValue, getStringValue, getBooleanValue, getIntegerValue methods



### 2. The [XWalkViewWithEchoExtensionAsync](misc/XWalkViewWithEchoExtensionAsync.java) sample demonstrates XWALK-3917 feature basic functionalities, include:

* extension can be supported

These two usecases cover following interface and methods:

* XWalkExtension interface: onMessage, onSyncMessage methods
* XWalkView interface: load method



### 3. The [XWalkViewWithMultiSurfaceViewsAsync](basic/XWalkViewWithMultiSurfaceViewsAsync.java) and [XWalkViewWithMultiTextureViewsAsync](baisc/XWalkViewWithMultiTextureViewsAsync.java) sample demonstrate XWALK-2012 feature basic functionalities, include:

* Multiple surfaceViews can be shown in order at first
* Multiple surfaceViews can be shown in order when rotating the device screen 90 degrees
* Multiple surfaceViews can be shown in order when restoring the device screen
* Multiple textureViews can be shown in order at first
* Multiple textureViews can be shown in order when rotating the device screen 90 degrees
* Multiple textureViews can be shown in order when restoring the device screen

This usecase covers following interface and methods:

* XWalkPreference interface: setValue method
* XWalkView interface: load method



### 4. The [XWalkViewWithAnimatableAsync](basic/XWalkViewWithAnimatableAsync.java) sample demonstrates how to use the basic functionalities of animatible XWalkView, include:

* Animatable XWalkView can be scaled down or scaled up

This usecase covers following interface and methods:

* XWalkPreference interface: setValue method
* XWalkView interface: load, getAlpha, getScaleX, getScaleY methods



### 5. The [XWalkViewWithLoadAppFromManifestAsync](basic/XWalkViewWithLoadAppFromManifestAsync.java) sample demonstrates how to load app from manifest, include:

* XWalkView can load app from manifest

This usecase covers following interface and methods:

* XWalkView interface: loadAppFromManifest methods



### 6. The [XWalkViewWithMultiInstanceActivityAsync](basic/XWalkViewWithMultiInstanceActivityAsync.java) sample demonstrates how to create multi instance, include:

* XWalkView can create multi instance

This usecase covers following interface and methods:

* XWalkView interface: load method



### 7. The [XWalkViewWithOnHideOnShowAsync](basic/XWalkViewWithOnHideOnShowAsync.java) sample demonstrates XWalkView can hide and show, include:

* XWalkView can hide when clicking home key
* There is no short white screen displayed when clicking home key
* XWalkView can show when Click the 'EmbeddedAPISamples' app again

This usecase covers following interface and methods:

* XWalkView interface: load method



### 8. The [XWalkViewWithPauseTimerAsync](basic/XWalkViewWithPauseTimerAsync.java) sample demonstrates XWalkView can pause timers, include:

* XWalkView can pause timers when it's pauseTimers() method is called
* XWalkView can resume timers when it's resumeTimers() method is called

This usecase covers following interface and methods:

* XWalkView interface: load, pauseTimers, resumeTimers methods



### 9. The [XWalkViewWithResourceAndUIClientAsync](client/XWalkViewWithResourceAndUIClientAsync.java) sample demonstrates how to set resource client and UI client, include:

* XWalkView can set resource client
* XWalkView can set UI client
* The log record the the implementation methods of resource client and UI client

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient, setUIClient methods
* ResourceClient interface: onLoadStarted, onLoadFinished, onProgressChanged, shouldInterceptLoadRequest, onReceivedLoadError methods
* UIClient interface: onJavascriptCloseWindow, onJavascriptModalDialog, onFullscreenToggled, openFileChooser, onScaleChanged methods



### 10. The [XWalkViewWithNavigationAsync](misc/XWalkViewWithNavigationAsync.java) sample demonstrates how to forward and backward history, include:

* XWalkView can backward history client when go backward button is clicked
* XWalkView can forward history client when go forward button is clicked

This usecase covers following interface and methods:

* XWalkView interface: load, getNavigationHistory methods
* XWalkNavigationHistory interface: canGoForward, navigate, getCurrentItem methods
* XWalkNavigationItem interface: getOriginalUrl, getTitle methods



### 11. The [XWalkViewWithVersionAndAPIVersionAsync](basic/XWalkViewWithVersionAndAPIVersionAsync.java) sample demonstrates how to get API version and xwalk version, include:

* XWalkView can get and show API version
* XWalkView can get and show xwalk version

This usecase covers following interface and methods:

* XWalkView interface: load, getAPIVersion, getXWalkVersion methods



### 12. The [XWalkViewWithLayoutActivityAsync](basic/XWalkViewWithLayoutActivityAsync.java) sample demonstrates how to load view UI, include:

* XWalkView can load view UI

This usecase covers following interface and methods:

* XWalkView interface: load method



### 13. The [XWalkViewWithOnIconAvailableOnReceivedIconAsync](client/XWalkViewWithOnIconAvailableOnReceivedIconAsync.java) sample demonstrates how to load icon when it's available, include:

* XWalkView can load icon when it's available

This usecase covers following interface and methods:

* XWalkView interface: load method
* UIClient interface: onIconAvailable, onReceivedIcon methods



### 14. The [XWalkViewWithOnCreateWindowRequestedAsync](client/XWalkViewWithOnCreateWindowRequestedAsync.java) sample demonstrates how to create new window, include:

* XWalkView can create new window

This usecase covers following interface and methods:

* XWalkView interface: load method
* UIClient interface: onCreateWindowRequested methods



### 15. The [XWalkViewWithFullScreenActivityAsync](baisc/XWalkViewWithFullScreenActivityAsync.java) sample demonstrates how to enter and exit fullscreen, include:

* XWalkView can enter and exit fullscreen

This usecase covers following interface and methods:

* XWalkView interface: load, leaveFullscreen method



### 16. The [XWalkViewWithShouldOverrideUrlLoadingAsync](client/XWalkViewWithShouldOverrideUrlLoadingAsync.java) sample demonstrates how to trigger shouldOverrideUrlLoading method, include:

* XWalkView can trigger shouldOverrideUrlLoading method

This usecase covers following interface and methods:

* XWalkView interface: load method
* ResourceClient interface: shouldOverrideUrlLoading methods



### 17. The [XWalkViewWithSetZOrderOnTopAsync](basic/XWalkViewWithSetZOrderOnTopAsync.java) sample check XWalkView's transparent feature whether display the view under the webview, include:

* XWalkView's transparent can display the view under the webview

This usecase covers following interface and methods:

* XWalkView interface: setZOrderOnTop, setBackgroundColor methods



### 18. The [XWalkViewWithRedirectionAsync](client/XWalkViewWithRedirectionAsync.java) sample verifies how many times onPageLoadStopped called when visit a web page with redirection, include:

* XWalkUIClient's onPageLoadStopped() method just be called once when visit a web page with redirection

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient, setUIClient methods
* ResourceClient interface: onProgressChanged method
* UIClient interface: onPageLoadStarted, onPageLoadStopped methods



### 19. The [XWalkViewWithLoadImageAsync](basic/XWalkViewWithLoadImageAsync.java) sample load image from XWalkView, include:

* XWalkView can load image

This usecase covers following interface and methods:

* XWalkView interface: load, onActivityResult methods



### 20. The [XWalkViewWithClearCacheAsync](basic/XWalkViewWithClearCacheAsync.java) sample check whether xwalkview can clear cache, include:

* XWalkView can clear cache

This usecase covers following interface and methods:

* XWalkView interface: load, clearCache methods
* UIClient interface: onPageLoadStopped methods



### 21. The [XWalkViewWithContactExtensionAsync](misc/XWalkViewWithContactExtensionAsync.java) sample demonstrates XWALK-3917 feature basic functionalities, include:

* extension can be supported with additional permissions

These two usecases cover following interface and methods:

* XWalkExtension interface: onMessage methods
* XWalkView interface: load method



### 22. The [XWalkViewWithZoomInAndOutAsync](basic/XWalkViewWithZoomInAndOutAsync.java) sample check whether xwalkview can zoom, include:

* XWalkView can zoom in, zoom out, zoom by

This usecase covers following interface and methods:

* XWalkView interface: load, zoomIn, zoomOut, zoomBy, canZoomOut, canZoomIn methods



### 23. The [XWalkViewWithDownloadListenerAsync](msic/XWalkViewWithDownloadListenerActivityAsync.java) sample check whether xwalkview can setUserAgentString & getUserAgentString & setDownloadListener & override onDownloadStart, include:

* XWalkView can setUserAgentString & getUserAgentString & setDownloadListener & override onDownloadStart

This usecase covers following interface and methods:

* XWalkView interface: load, setUserAgentString, getUserAgentString, setDownloadListener, onDownloadStart methods



### 24. The [XWalkViewWithBlockAndErrorRedirectionAsync](client/XWalkViewWithBlockAndErrorRedirectionAsync.java) sample check whether xwalkview can block response and redirect when url or internet is not avaliable, include:

* XWalkView can block response & make error redirection

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: shouldInterceptLoadRequest, onReceivedLoadError methods



### 25. The [XWalkViewWithSaveStateAsync](basic/XWalkViewWithSaveStateAsync.java) sample check whether xwalkview can saveState & restoreState bundle, include:

* XWalkView can saveState & restoreState bundle

This usecase covers following interface and methods:

* XWalkView interface: load, saveState, restoreState methods



### 26. The [XWalkViewWithInputConnectionAsync](extended/XWalkViewWithInputConnectionAsync.java) sample check whether xwalkview can use onCreateInputConnection method, include:

* XWalkView can use onCreateInputConnection method

This usecase covers following interface and methods:

* XWalkView interface: load, onCreateInputConnection methods



### 27. The [XWalkViewWithDispatchKeyEventAsync](extended/XWalkViewWithDispatchKeyEventAsync.java) sample check whether xwalkview can use dispatchKeyEvent method, include:

* XWalkView can use dispatchKeyEvent method

This usecase covers following interface and methods:

* XWalkView interface: load, dispatchKeyEvent methods



### 28. The [XWalkViewWithSetLanguageAsync](basic/XWalkViewWithSetLanguageAsync.java) sample check whether xwalkview can set accept language, include:

* XWalkView can use setAcceptLanguages method

This usecase covers following interface and methods:

* XWalkView interface: load, setAcceptLanguages methods



### 29. The [XWalkViewWithDispatchDrawAsync](extended/XWalkViewWithDispatchDrawAsync.java) sample check whether dispatchDraw method work as same as WebView, include:

* dispatchDraw can be override

This usecase covers following interface and methods:

* XWalkView interface: dispatchDraw methods


### 30. The [XWalkViewWithCookieManagerTestAsync](misc/XWalkViewWithCookieManagerTestAsync.java) sample check whether XWalkCookieManager apis can work, include:

* XWalkCookieManager apis can work

This usecase covers following interface and methods:

* XWalkView interface: load method
* XWalkCookieManager interface: setAcceptCookie, acceptCookie, setCookie, getCookie, removeSessionCookie, removeAllCookie, hasCookies, removeExpiredCookie, flushCookieStore



### 31. The [XWalkViewWithOnDrawAsync](extended/XWalkViewWithOnDrawAsync.java) sample check whether onDraw method work as same as WebView, include:

* onDraw can be override

This usecase covers following interface and methods:

* XWalkView interface: onDraw method



### 32. The [XWalkViewWithOverScrollAsync](extended/XWalkViewWithOverScrollAsync.java) sample check whether onOverScrolled method work as same as WebView, include:

* onOverScrolled can be override

This usecase covers following interface and methods:

* XWalkView interface: onOverScrolled method



### 33. The [XWalkViewWithAcceptFileSchemeCookiesAsync](misc/XWalkViewWithAcceptFileSchemeCookiesAsync.java) sample check whether XWalkCookieManager can set AcceptFileSchemeCookies, include:

* XWalkCookieManager apis can work

This usecase covers following interface and methods:

* XWalkCookieManager interface: setAcceptFileSchemeCookies, allowFileSchemeCookies methods



### 34. The [XWalkViewWithOnTouchEventAsync](extended/XWalkViewWithOnTouchEventAsync.java) sample check whether onTouchEvent method work as same as WebView, include:

* onTouchEvent can be override

This usecase covers following interface and methods:

* XWalkView interface: onTouchEvent method



### 35. The [XWalkViewWithOverScrollByAsync](extended/XWalkViewWithOverScrollByAsync.java) sample check whether overScrollBy method work as same as WebView, include:

* overScrollBy can be override

This usecase covers following interface and methods:

* XWalkView interface: overScrollBy method



### 36. The [XWalkViewWithFocusChangedAsync](extended/XWalkViewWithFocusChangedAsync.java) sample check whether onFocusChanged method work as same as WebView, include:

* onFocusChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onFocusChanged method



### 37. The [XWalkViewWithScrollChangedAsync](extended/XWalkViewWithScrollChangedAsync.java) sample check whether onScrollChanged method work as same as WebView, include:

* onScrollChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onScrollChanged method


### 38. The [XWalkViewWithSizeChangedAsync](extended/XWalkViewWithSizeChangedAsync.java) sample check whether onSizeChanged method work as same as WebView, include:

* onSizeChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onSizeChanged method



### 39. The [XWalkViewWithVisibilityChangedAsync](extended/XWalkViewWithVisibilityChangedAsync.java) sample check whether onVisibilityChanged method work as same as WebView, include:

* onVisibilityChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onVisibilityChanged method


### 40. The [XWalkViewWithWindowFocusChangedAsync](extended/XWalkViewWithWindowFocusChangedAsync.java) sample check whether onWindowFocusChanged method work as same as WebView, include:

* onWindowFocusChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onWindowFocusChanged method


### 41. The [XWalkViewWithWindowsVisibilityChangedAsync](extended/XWalkViewWithWindowsVisibilityChangedAsync.java) sample check whether onWindowVisibilityChanged method work as same as WebView, include:

* onWindowVisibilityChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onWindowVisibilityChanged method


### 42. The [XWalkViewWithClearFormDataAsync](extended/XWalkViewWithClearFormDataAsync.java) sample check whether clearFormData method work as same as WebView, include:

* clearFormData can work

This usecase covers following interface and methods:

* XWalkView interface: load, clearFormData methods




### 43. The [XWalkViewWithDisableLongClickAsync](extended/XWalkViewWithDisableLongClickAsync.java) sample check whether setOnLongClickListener method work as same as WebView, include:

* setOnLongClickListener can work

This usecase covers following interface and methods:

* XWalkView interface: load, setOnLongClickListener, setLongClickable methods



### 44. The [XWalkViewWithOnReceivedLoadErrorAsync](client/XWalkViewWithOnReceivedLoadErrorAsync.java) sample check whether XWalkView change dialog of onReceivedLoadError to toast, include:

* onReceivedLoadError can work

This usecase covers following interface and methods:

* XWalkView interface: load, onReceivedLoadError methods


### 45. The [XWalkViewWithLongClickAsync](extended/XWalkViewWithLongClickAsync.java) sample check whether performLongClick and setOnLongClickListener method work as same as WebView, include:

* performLongClick and setOnLongClickListener can be override and invoked

This usecase covers following interface and methods:

* XWalkView interface: performLongClick, setOnLongClickListener methods


### 46. The [XWalkViewWithRequestFocusAsync](extended/XWalkViewWithRequestFocusAsync.java) sample check whether requestFocus method work as same as WebView, include:

* requestFocus can be override and invoked

This usecase covers following interface and methods:

* XWalkView interface: requestFocus methods


### 47. The [XWalkViewWithSetLayerTypeAsync](extended/XWalkViewWithSetLayerTypeAsync.java) sample check whether setLayerType method work as same as WebView, include:

* setLayerType can be invoked

This usecase covers following interface and methods:

* XWalkView interface: setLayerType methods


### 48. The [XWalkViewWithNetworkAvailableAsync](extended/XWalkViewWithNetworkAvailableAsync.java) sample check whether setNetworkAvailable method work as same as WebView, include:

* setNetworkAvailable can be invoked

This usecase covers following interface and methods:

* XWalkView interface: setNetworkAvailable methods


### 49. The [XWalkViewWithConsoleLogAsync](client/XWalkViewWithConsoleLogAsync.java) sample check whether onConsoleMessage method work as same as WebView, include:

* onConsoleMessage can be invoked

This usecase covers following interface and methods:

* XWalkView XWalkUIClient interface: onConsoleMessage methods


### 50. The [XWalkViewWithReceivedTitleAsync](client/XWalkViewWithReceivedTitleAsync.java) sample check whether onReceivedTitle method work as same as WebView, include:

* onReceivedTitle can be invoked

This usecase covers following interface and methods:

* XWalkView XWalkUIClient interface: onReceivedTitle methods



### 51. The [XWalkViewWithClientOnRequestFocusAsync](client/XWalkViewWithClientOnRequestFocusAsync.java) sample check whether XWalkUIClient.onRequestFocus method work as same as WebView, include:

* XWalkUIClient.onRequestFocus can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.onRequestFocus methods


### 52. The [XWalkViewWithClientKeyEventAsync](client/XWalkViewWithClientKeyEventAsync.java) sample check whether XWalkUIClient.shouldOverrideKeyEvent method work as same as WebView, include:

* XWalkUIClient.shouldOverrideKeyEvent can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.shouldOverrideKeyEvent methods

### 53. The [XWalkViewWithClientReceivedSSLErrorAsync](client/XWalkViewWithClientReceivedSSLErrorAsync.java) sample check whether XWalkResourceClient.onReceivedSslError method work as same as WebView, include:

* XWalkResourceClient.onReceivedSslError can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkResourceClient.onReceivedSslError methods



### 54. The [XWalkViewWithTransparentAsync](basic/XWalkViewWithTransparentAsync.java) sample check XWalkView's transparent feature, include:

* XWalkView's transparent can display

This usecase covers following interface and methods:

* XWalkView interface: setBackgroundColor methods



### 55. The [XWalkViewWithSetInitialScaleAsync](basic/XWalkViewWithSetInitialScaleAsync.java) sample check XWalkView's setInitialScale feature, include:

* XWalkView can setInitialScale

This usecase covers following interface and methods:

* XWalkView interface: load, setInitialScale methods



### 56. The [XWalkViewWithOnUnhandledKeyEventAsync](client/XWalkViewWithOnUnhandledKeyEventAsync.java) sample check XWalkUIClient.onUnhandledKeyEvent method work as same as WebView, include:

* XWalkUIClient.onUnhandledKeyEvent can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.onUnhandledKeyEvent methods



### 57. The [XWalkViewWithClearCacheForSingleFileAsync](basic/XWalkViewWithClearCacheForSingleFileAsync.java) sample check XWalkView can implement clearCacheForSingleFile API, include:

* XWalkView can implement clearCacheForSingleFile API

This usecase covers following interface and methods:

* XWalkView interface: clearCacheForSingleFile, load methods



### 58. The [XWalkViewWithEncodingDisplayAsync](basic/XWalkViewWithEncodingDisplayAsync.java) sample check XWalkView can display utf-8 charset html file, include:

* XWalkView can display utf-8 charset

This usecase covers following interface and methods:

* XWalkView interface: load



### 59. The [XWalkViewWithOpenFileChooserAsync](client/XWalkViewWithOpenFileChooserAsync.java) sample check XWalkView can open local file, include:

* XWalkUIClient.openFileChooser can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.openFileChooser methods



### 60. The [XWalkViewWithScrollViewParentAsync](basic/XWalkViewWithScrollViewParentAsync.java) sample check XWalkView inside a scrollview can display, include:

* XWalkView inside a scrollview can display

This usecase covers following interface and methods:

* XWalkView interface: load methods



### 61. The [XWalkViewWithMultiInstanceOverlayAsync](basic/XWalkViewWithMultiInstanceOverlayAsync.java) sample check two xwalkviews filling in the same parent view can be displayed dynamically, include:

* Two xwalkviews filling in the same parent view can be displayed dynamically

This usecase covers following interface and methods:

* XWalkView interface: load methods



### 62. The [XWalkViewWithOnReceivedHttpAuthRequestAsync](client/XWalkViewWithOnReceivedHttpAuthRequestAsync.java) sample check onReceivedHttpAuthRequest will be invoked when website needs auth request, include:

* XWalkView can handle an authentication request

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: onReceivedHttpAuthRequest methods



### 63. The [XWalkViewWithWindowSecureAsync](basic/XWalkViewWithWindowSecureAsync.java) sample check xwalkview window can prevent from the screenshoting by setting window flag SECURE, include:

* xwalkview window can prevent from the screenshoting by setting window flag SECURE

This usecase covers following interface and methods:

* XWalkView interface: load methods




### 64. The [XWalkViewWithSessionStorageAsync](misc/XWalkViewWithSessionStorageAsync.java) sample check xwalkview can restore html5 sessionstorage value when screen rotates, include:

* xwalkview can restore html5 sessionstorage value when screen rotates

This usecase covers following interface and methods:

* XWalkView interface: load, saveState, restoreState methods



### 65. The [XWalkViewWithOnJavascriptModalDialogAsync](client/XWalkViewWithOnJavascriptModalDialogAsync.java) sample check XWalkUIClient API onJavascriptModalDialog method can work, include:

* XWalkUIClient API onJavascriptModalDialog method can work

This usecase covers following interface and methods:

* XWalkView interface: load methods

* UIClient interface: onJavascriptModalDialog methods



### 66. The [XWalkViewWithOnJavascriptCloseWindowAsync](client/XWalkViewWithOnJavascriptCloseWindowAsync.java) sample check XWalkUIClient API onJavascriptCloseWindow method can work, include:

* XWalkUIClient API onJavascriptCloseWindow method can work

This usecase covers following interface and methods:

* XWalkView interface: load methods

* UIClient interface: onJavascriptCloseWindow methods


### 67. The [XWalkViewSettingUserAgentAsync](setting/XWalkViewSettingUserAgentAsync.java) sample check XWalkSetting API setUserAgentString method can work, include:

* XWalkSetting API setUserAgentString method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setUserAgentString
* XWalkView interface: load methods


### 68. The [XWalkViewSettingAcceptLanguageAsync](setting/XWalkViewSettingAcceptLanguageAsync.java) sample check XWalkSetting API setAcceptLanguage method can work, include:

* XWalkSetting API setAcceptLanguage method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setAcceptLanguage
* XWalkView interface: load methods



### 69. The [XWalkViewSettingSetInitialPageScaleAsync](setting/XWalkViewSettingSetInitialPageScaleAsync.java) sample check XWalkSetting API setInitialPageScale method can work, include:

* XWalkSetting API setInitialPageScale method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setInitialPageScale
* XWalkView interface: load me



### 70. The [XWalkViewSettingTextZoomAsync](setting/XWalkViewSettingTextZoomAsync.java) sample check XWalkSetting API getTextZoom & setTextZoom method can work, include:

* XWalkSetting API getTextZoom & setTextZoom method can work

This usecase covers following interface and methods:

* XWalkSetting interface: getTextZoom, setTextZoom
* XWalkView interface: load methods



### 71. The [XWalkViewSettingSupportZoomAsync](setting/XWalkViewSettingSupportZoomAsync.java) sample check XWalkSetting API support zoom method can work, include:

* XWalkSetting API setUseWideViewPort & getUseWideViewPort & setSupportZoom & supportZoom & setBuiltInZoomControls & getBuiltInZoomControls method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setUseWideViewPort, getUseWideViewPort, setSupportZoom, supportZoom, setBuiltInZoomControls, getBuiltInZoomControls methods
* XWalkView interface: load methods



### 72. The [XWalkViewSettingDefaultFontSizeAsync](setting/XWalkViewSettingDefaultFontSizeAsync.java) sample check XWalkSetting API set default font size method can work, include:

* XWalkSetting API setDefaultFontSize, getDefaultFontSize method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setDefaultFontSize, getDefaultFontSize methods
* XWalkView interface: load methods



### 73. The [XWalkViewSettingDefaultFixedFontSizeAsync](setting/XWalkViewSettingDefaultFixedFontSizeAsync.java) sample check XWalkSetting API set default fixed font size method can work, include:

* XWalkSetting API setDefaultFixedFontSize, getDefaultFixedFontSize method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setDefaultFixedFontSize, getDefaultFixedFontSize methods
* XWalkView interface: load methods



### 74. The [XWalkViewWithCaptureBitmapAsyncAsync](basic/XWalkViewWithCaptureBitmapAsyncAsync.java) sample check XWalkView can capture the visible content of web page, include:

* XWalkView API captureBitmapAsync method can work

This usecase covers following interface and methods:

* XWalkView interface: load, scaptureBitmapAsync methods



### 75. The [XWalkViewWithOnTouchListenerAsync](misc/XWalkViewWithOnTouchListenerAsync.java) sample check XWalkView API setOnTouchListener method can work, include:

* XWalkView API setOnTouchListener method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setOnTouchListener
* XWalkView interface: load methods



### 76. The [XWalkViewWithOnJsAlertAsync](client/XWalkViewWithOnJsAlertAsync.java) sample check API XWalkUIClient.onJsAlert, XWalkUICLient.onJsConfirm and XWalkUIClient.onJsPropmt can work, include:

* API XWalkUIClient.onJsAlert, XWalkUICLient.onJsConfirm and XWalkUIClient.onJsPropmt can work

This usecase covers following interface and methods:

* XWalkUIClient interface: onJsAlert, onJsConfirm, onJsPropmt methods
* XWalkView interface: load methods



### 77. The [XWalkViewWithOnReceivedResponseHeadersAsync](client/XWalkViewWithOnReceivedResponseHeadersAsync.java) sample check API XWalkResourceClient.onReceivedResponseHeaders can work, include:

* API XWalkResourceClient.onReceivedResponseHeaders can work

This usecase covers following interface and methods:

* XWalkResourceClient interface: onReceivedResponseHeaders
* XWalkView interface: load methods



### 78. The [XWalkViewWithGetFaviconAsync](basic/XWalkViewWithGetFaviconAsync.java) sample check XWalkView can get favicon from the html, include:

* XWalkView API getFavicon method can work

This usecase covers following interface and methods:

* XWalkView interface: load, getFavicon methods



### 79. The [XWalkViewWithLoadExtensionAsync](misc/XWalkViewWithLoadExtensionAsync.java) sample check XWalkView can load external extensions dynamically, include:

* XWalkView API getExtensionManager().loadExtension method can work

This usecase covers following interface and methods:

* XWalkView interface: load, getExtensionManager().loadExtension methods



### 80. The [XWalkViewWithIframesAsync](basic/XWalkViewWithIframesAsync.java) sample check XWalkView can be reliable with iframes, include:

* XWalkView can be reliable with iframes

This usecase covers following interface and methods:

* XWalkView interface: load method
* ResourceClient interface: shouldInterceptLoadRequest method



### 81. The [XWalkViewWithClearSslPreferencesAsync](misc/XWalkViewWithClearSslPreferencesAsync.java) sample check XWalkView can clear ssl preferences, include:

* XWalkView can clear ssl preferences

This usecase covers following interface and methods:

* XWalkView interface: load, clearSslPreferences method
* ResourceClient interface: onReceivedSslError method



### 82. The [XWalkViewWithThemeColorAsync](misc/XWalkViewWithThemeColorAsync.java) sample demonstrates XWalkView can support theme-color meta tag by setting ENABLE_THEME_COLOR, include:

* XWalkView can set style value
* XWalkView can get style value

This usecase covers following interface and methods:

* XWalkPreferences interface: getBooleanValue, setValue



### 83. The [XWalkViewWithShouldInterceptLoadRequestAsync](client/XWalkViewWithShouldInterceptLoadRequestAsync.java) sample demonstrates XWalkResourceClient API shouldInterceptLoadRequest can work, include:

* XWalkView can set resource client
* shouldInterceptLoadRequest can work

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: shouldInterceptLoadRequest method



### 84. The [XWalkViewWithClearClientCertPreferencesAsync](basic/XWalkViewWithClearClientCertPreferencesAsync.java) sample demonstrates XWalkView can clear client certificate preferences, include:

* XWalkView can clear client certificate preferences

This usecase covers following interface and methods:

* XWalkView interface: load, clearClientCertPreferences methods
* ResourceClient interface: onReceivedClientCertRequest method



### 85. The [XWalkViewWithSetBackgroundColorAsync](basic/XWalkViewWithSetBackgroundColorAsync.java) sample check XWalkView can set background color without delay, include:

* XWalkView can set background color without delay

This usecase covers following interface and methods:

* XWalkView interface: load, setBackgroundColor method



### 86. The [XWalkViewWithNewLoadAsync](basic/XWalkViewWithNewLoadAsync.java) sample check XWalkView's new interface: load URL with specified HTTP headers, include:

* XWalkView can load url with specified HTTP headers

This usecase covers following interface and methods:

* XWalkView interface: load method



### 87. The [XWalkViewWithComputeScrollAsync](extended/XWalkViewWithComputeScrollAsync.java) sample check XWalkView can computeHorizontalScrollOffset, computeHorizontalScrollRange, computeVerticalScrollOffset, computeVerticalScrollRange and computeVerticalScrollExtent, include:

* XWalkView can computeHorizontalScrollOffset, computeHorizontalScrollRange, computeVerticalScrollOffset, computeVerticalScrollRange and computeVerticalScrollExtent

This usecase covers following interface and methods:

* XWalkView interface: load, computeHorizontalScrollOffset, computeHorizontalScrollRange, computeVerticalScrollOffset, computeVerticalScrollRange and computeVerticalScrollExtent methods


### 88. The [XWalkViewSettingDomStorageEnabledAsync](setting/XWalkViewSettingDomStorageEnabledAsync.java) sample check XWalkView can enable/disable DOM storage API, include:

* XWalkView can enable DOM storage API
* XWalkView can disable DOM storage API

This usecase covers following interface and methods:

* XWalkSettings interface: setDomStorageEnabled, getDomStorageEnabled


### 89. The [XWalkViewSettingSaveFormDataAsync](setting/XWalkViewSettingSaveFormDataAsync.java) sample check XWalkView can enable/disable form autocomplete and/or delete saved form data, include:

* XWalkView can enable saveFormData
* XWalkView can disable saveFormData

This usecase covers following interface and methods:

* XWalkSettings interface: setSaveFormData, getSaveFormData


### 90. The [XWalkViewSettingJavaScriptEnabledAsync](setting/XWalkViewSettingJavaScriptEnabledAsync.java) sample check XWalkView can enable/disable JavaScript, include:

* XWalkView can enable JavaScript
* XWalkView can disable JavaScript

This usecase covers following interface and methods:

* XWalkSettings interface: setJavaScript, getJavaScript


### 91. The [XWalkViewSettingJavaScriptCanOpenWindowsAutomaticallyAsync](setting/XWalkViewSettingJavaScriptCanOpenWindowsAutomaticallyAsync.java) sample check XWalkView can enable/disable JavaScriptCanOpenWindowsAutomatically, include:

* XWalkView can enable JavaScriptCanOpenWindowsAutomatically
* XWalkView can disable JavaScriptCanOpenWindowsAutomatically

This usecase covers following interface and methods:

* XWalkSettings interface: setJavaScriptCanOpenWindowsAutomatically, getJavaScriptCanOpenWindowsAutomatically

### 92. The [XWalkViewSettingDatabaseEnabledAsync](setting/XWalkViewSettingDatabaseEnabledAsync.java) sample check XWalkView can enable/disable Database storage, include:

* XWalkView can enable Database storage
* XWalkView can disable Database storage

This usecase covers following interface and methods:

* XWalkSettings interface: setDatabaseEnabled, getDatabaseEnabled
