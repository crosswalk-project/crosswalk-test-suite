## Usecase Design

### 1. The [XWalkViewWithPreferences](misc/XWalkViewWithPreferences.java) sample demonstrates XWALK-2376 feature basic functionalities, include:

* XWalkView can set style value
* XWalkView can get style value

This usecase covers following interface and methods:

* XWalkPreferences interface: setValue, getStringValue, getBooleanValue, getIntegerValue methods



### 2. The [XWalkViewWithEchoExtension](misc/XWalkViewWithEchoExtension.java) sample demonstrates XWALK-3917 feature basic functionalities, include:

* extension can be supported

These two usecases cover following interface and methods:

* XWalkExtension interface: onMessage, onSyncMessage methods
* XWalkView interface: load method



### 3. The [XWalkViewWithMultiSurfaceViews](basic/XWalkViewWithMultiSurfaceViews.java) and [XWalkViewWithMultiTextureViews](basic/XWalkViewWithMultiTextureViews.java) sample demonstrate XWALK-2012 feature basic functionalities, include:

* Multiple surfaceViews can be shown in order at first
* Multiple surfaceViews can be shown in order when rotating the device screen 90 degrees
* Multiple surfaceViews can be shown in order when restoring the device screen
* Multiple textureViews can be shown in order at first
* Multiple textureViews can be shown in order when rotating the device screen 90 degrees
* Multiple textureViews can be shown in order when restoring the device screen

This usecase covers following interface and methods:

* XWalkPreference interface: setValue method
* XWalkView interface: load method



### 4. The [XWalkViewWithAnimatable](basic/XWalkViewWithAnimatable.java) sample demonstrates how to use the basic functionalities of animatible XWalkView, include:

* Animatable XWalkView can be scaled down or scaled up

This usecase covers following interface and methods:

* XWalkPreference interface: setValue method
* XWalkView interface: load, getAlpha, getScaleX, getScaleY methods



### 5. The [XWalkViewWithLoadAppFromManifest](basic/XWalkViewWithLoadAppFromManifest.java) sample demonstrates how to load app from manifest, include:

* XWalkView can load app from manifest

This usecase covers following interface and methods:

* XWalkView interface: loadAppFromManifest methods



### 6. The [XWalkViewWithMultiInstanceActivity](basic/XWalkViewWithMultiInstanceActivity.java) sample demonstrates how to create multi instance, include:

* XWalkView can create multi instance

This usecase covers following interface and methods:

* XWalkView interface: load method



### 7. The [XWalkViewWithOnHideOnShow](basic/XWalkViewWithOnHideOnShow.java) sample demonstrates XWalkView can hide and show, include:

* XWalkView can hide when clicking home key
* There is no short white screen displayed when clicking home key
* XWalkView can show when Click the 'EmbeddedAPISamples' app again

This usecase covers following interface and methods:

* XWalkView interface: load method



### 8. The [XWalkViewWithPauseTimer](basic/XWalkViewWithPauseTimer.java) sample demonstrates XWalkView can pause timers, include:

* XWalkView can pause timers when it's pauseTimers() method is called
* XWalkView can resume timers when it's resumeTimers() method is called

This usecase covers following interface and methods:

* XWalkView interface: load, pauseTimers, resumeTimers methods



### 9. The [XWalkViewWithResourceAndUIClient](client/XWalkViewWithResourceAndUIClient.java) sample demonstrates how to set resource client and UI client, include:

* XWalkView can set resource client
* XWalkView can set UI client
* The log record the the implementation methods of resource client and UI client

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient, setUIClient methods
* ResourceClient interface: onLoadStarted, onLoadFinished, onProgressChanged, shouldInterceptLoadRequest, onReceivedLoadError methods
* UIClient interface: onJavascriptCloseWindow, onJavascriptModalDialog, onFullscreenToggled, openFileChooser, onScaleChanged methods



### 10. The [XWalkViewWithNavigation](misc/XWalkViewWithNavigation.java) sample demonstrates how to forward and backward history, include:

* XWalkView can backward history client when go backward button is clicked
* XWalkView can forward history client when go forward button is clicked

This usecase covers following interface and methods:

* XWalkView interface: load, getNavigationHistory methods
* XWalkNavigationHistory interface: canGoForward, navigate, getCurrentItem methods
* XWalkNavigationItem interface: getOriginalUrl, getTitle methods



### 11. The [XWalkViewWithVersionAndAPIVersion](basic/XWalkViewWithVersionAndAPIVersion.java) sample demonstrates how to get API version and xwalk version, include:

* XWalkView can get and show API version
* XWalkView can get and show xwalk version

This usecase covers following interface and methods:

* XWalkView interface: load, getAPIVersion, getXWalkVersion methods



### 12. The [XWalkViewWithLayoutActivity](basic/XWalkViewWithLayoutActivity.java) sample demonstrates how to load view UI, include:

* XWalkView can load view UI

This usecase covers following interface and methods:

* XWalkView interface: load method



### 13. The [XWalkViewWithOnIconAvailableOnReceivedIcon](client/XWalkViewWithOnIconAvailableOnReceivedIcon.java) sample demonstrates how to load icon when it's available, include:

* XWalkView can load icon when it's available

This usecase covers following interface and methods:

* XWalkView interface: load method
* UIClient interface: onIconAvailable, onReceivedIcon methods



### 14. The [XWalkViewWithOnCreateWindowRequested](client/XWalkViewWithOnCreateWindowRequested.java) sample demonstrates how to create new window, include:

* XWalkView can create new window

This usecase covers following interface and methods:

* XWalkView interface: load method
* UIClient interface: onCreateWindowRequested methods



### 15. The [XWalkViewWithFullScreenActivity](basic/XWalkViewWithFullScreenActivity.java) sample demonstrates how to enter and exit fullscreen, include:

* XWalkView can enter and exit fullscreen

This usecase covers following interface and methods:

* XWalkView interface: load, leaveFullscreen method



### 16. The [XWalkViewWithShouldOverrideUrlLoading](client/XWalkViewWithShouldOverrideUrlLoading.java) sample demonstrates how to trigger shouldOverrideUrlLoading method, include:

* XWalkView can trigger shouldOverrideUrlLoading method

This usecase covers following interface and methods:

* XWalkView interface: load method
* ResourceClient interface: shouldOverrideUrlLoading methods



### 17. The [XWalkViewWithSetZOrderOnTop](basic/XWalkViewWithSetZOrderOnTop.java) sample check XWalkView's transparent feature whether display the view under the webview, include:

* XWalkView's transparent can display the view under the webview

This usecase covers following interface and methods:

* XWalkView interface: setZOrderOnTop, setBackgroundColor methods



### 18. The [XWalkViewWithRedirection](client/XWalkViewWithRedirection.java) sample verifies how many times onPageLoadStopped called when visit a web page with redirection, include:

* XWalkUIClient's onPageLoadStopped() method just be called once when visit a web page with redirection

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient, setUIClient methods
* ResourceClient interface: onProgressChanged method
* UIClient interface: onPageLoadStarted, onPageLoadStopped methods



### 19. The [XWalkViewWithLoadImage](basic/XWalkViewWithLoadImage.java) sample load image from XWalkView, include:

* XWalkView can load image

This usecase covers following interface and methods:

* XWalkView interface: load, onActivityResult methods



### 20. The [XWalkViewWithClearCache](basic/XWalkViewWithClearCache.java) sample check whether xwalkview can clear cache, include:

* XWalkView can clear cache

This usecase covers following interface and methods:

* XWalkView interface: load, clearCache methods
* UIClient interface: onPageLoadStopped methods



### 21. The [XWalkViewWithContactExtension](misc/XWalkViewWithContactExtension.java) sample demonstrates XWALK-3917 feature basic functionalities, include:

* extension can be supported with additional permissions

These two usecases cover following interface and methods:

* XWalkExtension interface: onMessage methods
* XWalkView interface: load method



### 22. The [XWalkViewWithZoomInAndOut](basic/XWalkViewWithZoomInAndOut.java) sample check whether xwalkview can zoom, include:

* XWalkView can zoom in, zoom out, zoom by

This usecase covers following interface and methods:

* XWalkView interface: load, zoomIn, zoomOut, zoomBy, canZoomOut, canZoomIn methods



### 23. The [XWalkViewWithDownloadListener](misc/XWalkViewWithDownloadListenerActivity.java) sample check whether xwalkview can setUserAgentString & getUserAgentString & setDownloadListener & override onDownloadStart, include:

* XWalkView can setUserAgentString & getUserAgentString & setDownloadListener & override onDownloadStart

This usecase covers following interface and methods:

* XWalkView interface: load, setUserAgentString, getUserAgentString, setDownloadListener, onDownloadStart methods



### 24. The [XWalkViewWithBlockAndErrorRedirection](client/XWalkViewWithBlockAndErrorRedirection.java) sample check whether xwalkview can block response and redirect when url or internet is not avaliable, include:

* XWalkView can block response & make error redirection

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: shouldInterceptLoadRequest, onReceivedLoadError methods



### 25. The [XWalkViewWithSaveState](basic/XWalkViewWithSaveState.java) sample check whether xwalkview can saveState & restoreState bundle, include:

* XWalkView can saveState & restoreState bundle

This usecase covers following interface and methods:

* XWalkView interface: load, saveState, restoreState methods



### 26. The [XWalkViewWithInputConnection](extended/XWalkViewWithInputConnection.java) sample check whether xwalkview can use onCreateInputConnection method, include:

* XWalkView can use onCreateInputConnection method

This usecase covers following interface and methods:

* XWalkView interface: load, onCreateInputConnection methods



### 27. The [XWalkViewWithDispatchKeyEvent](extended/XWalkViewWithDispatchKeyEvent.java) sample check whether xwalkview can use dispatchKeyEvent method, include:

* XWalkView can use dispatchKeyEvent method

This usecase covers following interface and methods:

* XWalkView interface: load, dispatchKeyEvent methods



### 28. The [XWalkViewWithSetLanguage](basic/XWalkViewWithSetLanguage.java) sample check whether xwalkview can set accept language, include:

* XWalkView can use setAcceptLanguages method

This usecase covers following interface and methods:

* XWalkView interface: load, setAcceptLanguages methods



### 29. The [XWalkViewWithDispatchDraw](extended/XWalkViewWithDispatchDraw.java) sample check whether dispatchDraw method work as same as WebView, include:

* dispatchDraw can be override

This usecase covers following interface and methods:

* XWalkView interface: dispatchDraw methods


### 30. The [XWalkViewWithCookieManagerTest](misc/XWalkViewWithCookieManagerTest.java) sample check whether XWalkCookieManager apis can work, include:

* XWalkCookieManager apis can work

This usecase covers following interface and methods:

* XWalkView interface: load method
* XWalkCookieManager interface: setAcceptCookie, acceptCookie, setCookie, getCookie, removeSessionCookie, removeAllCookie, hasCookies, removeExpiredCookie, flushCookieStore



### 31. The [XWalkViewWithOnDraw](extended/XWalkViewWithOnDraw.java) sample check whether onDraw method work as same as WebView, include:

* onDraw can be override

This usecase covers following interface and methods:

* XWalkView interface: onDraw method



### 32. The [XWalkViewWithOverScroll](extended/XWalkViewWithOverScroll.java) sample check whether onOverScrolled method work as same as WebView, include:

* onOverScrolled can be override

This usecase covers following interface and methods:

* XWalkView interface: onOverScrolled method



### 33. The [XWalkViewWithAcceptFileSchemeCookies](misc/XWalkViewWithAcceptFileSchemeCookies.java) sample check whether XWalkCookieManager can set AcceptFileSchemeCookies, include:

* XWalkCookieManager apis can work

This usecase covers following interface and methods:

* XWalkCookieManager interface: setAcceptFileSchemeCookies, allowFileSchemeCookies methods



### 34. The [XWalkViewWithOnTouchEvent](extended/XWalkViewWithOnTouchEvent.java) sample check whether onTouchEvent method work as same as WebView, include:

* onTouchEvent can be override

This usecase covers following interface and methods:

* XWalkView interface: onTouchEvent method



### 35. The [XWalkViewWithOverScrollBy](extended/XWalkViewWithOverScrollBy.java) sample check whether overScrollBy method work as same as WebView, include:

* overScrollBy can be override

This usecase covers following interface and methods:

* XWalkView interface: overScrollBy method



### 36. The [XWalkViewWithFocusChanged](extended/XWalkViewWithFocusChanged.java) sample check whether onFocusChanged method work as same as WebView, include:

* onFocusChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onFocusChanged method



### 37. The [XWalkViewWithScrollChanged](extended/XWalkViewWithScrollChanged.java) sample check whether onScrollChanged method work as same as WebView, include:

* onScrollChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onScrollChanged method


### 38. The [XWalkViewWithSizeChanged](extended/XWalkViewWithSizeChanged.java) sample check whether onSizeChanged method work as same as WebView, include:

* onSizeChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onSizeChanged method



### 39. The [XWalkViewWithVisibilityChanged](extended/XWalkViewWithVisibilityChanged.java) sample check whether onVisibilityChanged method work as same as WebView, include:

* onVisibilityChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onVisibilityChanged method


### 40. The [XWalkViewWithWindowFocusChanged](extended/XWalkViewWithWindowFocusChanged.java) sample check whether onWindowFocusChanged method work as same as WebView, include:

* onWindowFocusChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onWindowFocusChanged method


### 41. The [XWalkViewWithWindowsVisibilityChanged](extended/XWalkViewWithWindowsVisibilityChanged.java) sample check whether onWindowVisibilityChanged method work as same as WebView, include:

* onWindowVisibilityChanged can be override

This usecase covers following interface and methods:

* XWalkView interface: onWindowVisibilityChanged method


### 42. The [XWalkViewWithClearFormData](extended/XWalkViewWithClearFormData.java) sample check whether clearFormData method work as same as WebView, include:

* clearFormData can work

This usecase covers following interface and methods:

* XWalkView interface: load, clearFormData methods




### 43. The [XWalkViewWithDisableLongClick](extended/XWalkViewWithDisableLongClick.java) sample check whether setOnLongClickListener method work as same as WebView, include:

* setOnLongClickListener can work

This usecase covers following interface and methods:

* XWalkView interface: load, setOnLongClickListener, setLongClickable methods



### 44. The [XWalkViewWithOnReceivedLoadError](client/XWalkViewWithOnReceivedLoadError.java) sample check whether XWalkView change dialog of onReceivedLoadError to toast, include:

* onReceivedLoadError can work

This usecase covers following interface and methods:

* XWalkView interface: load, onReceivedLoadError methods


### 45. The [XWalkViewWithLongClick](extended/XWalkViewWithLongClick.java) sample check whether performLongClick and setOnLongClickListener method work as same as WebView, include:

* performLongClick and setOnLongClickListener can be override and invoked

This usecase covers following interface and methods:

* XWalkView interface: performLongClick, setOnLongClickListener methods


### 46. The [XWalkViewWithRequestFocus](extended/XWalkViewWithRequestFocus.java) sample check whether requestFocus method work as same as WebView, include:

* requestFocus can be override and invoked

This usecase covers following interface and methods:

* XWalkView interface: requestFocus methods


### 47. The [XWalkViewWithSetLayerType](extended/XWalkViewWithSetLayerType.java) sample check whether setLayerType method work as same as WebView, include:

* setLayerType can be invoked

This usecase covers following interface and methods:

* XWalkView interface: setLayerType methods


### 48. The [XWalkViewWithNetworkAvailable](extended/XWalkViewWithNetworkAvailable.java) sample check whether setNetworkAvailable method work as same as WebView, include:

* setNetworkAvailable can be invoked

This usecase covers following interface and methods:

* XWalkView interface: setNetworkAvailable methods


### 49. The [XWalkViewWithConsoleLog](client/XWalkViewWithConsoleLog.java) sample check whether onConsoleMessage method work as same as WebView, include:

* onConsoleMessage can be invoked

This usecase covers following interface and methods:

* XWalkView XWalkUIClient interface: onConsoleMessage methods


### 50. The [XWalkViewWithReceivedTitle](client/XWalkViewWithReceivedTitle.java) sample check whether onReceivedTitle method work as same as WebView, include:

* onReceivedTitle can be invoked

This usecase covers following interface and methods:

* XWalkView XWalkUIClient interface: onReceivedTitle methods



### 51. The [XWalkViewWithClientOnRequestFocus](client/XWalkViewWithClientOnRequestFocus.java) sample check whether XWalkUIClient.onRequestFocus method work as same as WebView, include:

* XWalkUIClient.onRequestFocus can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.onRequestFocus methods


### 52. The [XWalkViewWithClientKeyEvent](client/XWalkViewWithClientKeyEvent.java) sample check whether XWalkUIClient.shouldOverrideKeyEvent method work as same as WebView, include:

* XWalkUIClient.shouldOverrideKeyEvent can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.shouldOverrideKeyEvent methods

### 53. The [XWalkViewWithClientReceivedSSLError](client/XWalkViewWithClientReceivedSSLError.java) sample check whether XWalkResourceClient.onReceivedSslError method work as same as WebView, include:

* XWalkResourceClient.onReceivedSslError can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkResourceClient.onReceivedSslError methods



### 54. The [XWalkViewWithTransparent](basic/XWalkViewWithTransparent.java) sample check XWalkView's transparent feature, include:

* XWalkView's transparent can display

This usecase covers following interface and methods:

* XWalkView interface: setBackgroundColor methods



### 55. The [XWalkViewWithSetInitialScale](basic/XWalkViewWithSetInitialScale.java) sample check XWalkView's setInitialScale feature, include:

* XWalkView can setInitialScale

This usecase covers following interface and methods:

* XWalkView interface: load, setInitialScale methods



### 56. The [XWalkViewWithOnUnhandledKeyEvent](client/XWalkViewWithOnUnhandledKeyEvent.java) sample check XWalkUIClient.onUnhandledKeyEvent method work as same as WebView, include:

* XWalkUIClient.onUnhandledKeyEvent can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.onUnhandledKeyEvent methods



### 57. The [XWalkViewWithClearCacheForSingleFile](basic/XWalkViewWithClearCacheForSingleFile.java) sample check XWalkView can implement clearCacheForSingleFile API, include:

* XWalkView can implement clearCacheForSingleFile API

This usecase covers following interface and methods:

* XWalkView interface: clearCacheForSingleFile, load methods



### 58. The [XWalkViewWithEncodingDisplay](basic/XWalkViewWithEncodingDisplay.java) sample check XWalkView can display utf-8 charset html file, include:

* XWalkView can display utf-8 charset

This usecase covers following interface and methods:

* XWalkView interface: load



### 59. The [XWalkViewWithOpenFileChooser](client/XWalkViewWithOpenFileChooser.java) sample check XWalkView can open local file, include:

* XWalkUIClient.openFileChooser can be invoked

This usecase covers following interface and methods:

* XWalkView interface: XWalkUIClient.openFileChooser methods



### 60. The [XWalkViewWithScrollViewParent](basic/XWalkViewWithScrollViewParent.java) sample check XWalkView inside a scrollview can display, include:

* XWalkView inside a scrollview can display

This usecase covers following interface and methods:

* XWalkView interface: load methods



### 61. The [XWalkViewWithMultiInstanceOverlay](basic/XWalkViewWithMultiInstanceOverlay.java) sample check two xwalkviews filling in the same parent view can be displayed dynamically, include:

* Two xwalkviews filling in the same parent view can be displayed dynamically

This usecase covers following interface and methods:

* XWalkView interface: load methods



### 62. The [XWalkViewWithOnReceivedHttpAuthRequest](client/XWalkViewWithOnReceivedHttpAuthRequest.java) sample check onReceivedHttpAuthRequest will be invoked when website needs auth request, include:

* XWalkView can handle an authentication request

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: onReceivedHttpAuthRequest methods



### 63. The [XWalkViewWithWindowSecure](basic/XWalkViewWithWindowSecure.java) sample check xwalkview window can prevent from the screenshoting by setting window flag SECURE, include:

* xwalkview window can prevent from the screenshoting by setting window flag SECURE

This usecase covers following interface and methods:

* XWalkView interface: load methods



### 64. The [XWalkViewWithSessionStorage](misc/XWalkViewWithSessionStorage.java) sample check xwalkview can restore html5 sessionstorage value when screen rotates, include:

* xwalkview can restore html5 sessionstorage value when screen rotates

This usecase covers following interface and methods:

* XWalkView interface: load, saveState, restoreState methods



### 65. The [XWalkViewWithOnJavascriptModalDialog](client/XWalkViewWithOnJavascriptModalDialog.java) sample check XWalkUIClient API onJavascriptModalDialog method can work, include:

* XWalkUIClient API onJavascriptModalDialog method can work

This usecase covers following interface and methods:

* XWalkView interface: load methods

* UIClient interface: onJavascriptModalDialog methods



### 66. The [XWalkViewWithOnJavascriptCloseWindow](client/XWalkViewWithOnJavascriptCloseWindow.java) sample check XWalkUIClient API onJavascriptCloseWindow method can work, include:

* XWalkUIClient API onJavascriptCloseWindow method can work

This usecase covers following interface and methods:

* XWalkView interface: load methods

* UIClient interface: onJavascriptCloseWindow methods


### 67. The [XWalkViewSettingUserAgent](setting/XWalkViewSettingUserAgent.java) sample check XWalkSetting API setUserAgentString method can work, include:

* XWalkSetting API setUserAgentString method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setUserAgentString
* XWalkView interface: load methods


### 68. The [XWalkViewSettingAcceptLanguage](setting/XWalkViewSettingAcceptLanguage.java) sample check XWalkSetting API setAcceptLanguage method can work, include:

* XWalkSetting API setAcceptLanguage method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setAcceptLanguage
* XWalkView interface: load methods



### 69. The [XWalkViewSettingSetInitialPageScale](setting/XWalkViewSettingSetInitialPageScale.java) sample check XWalkSetting API setInitialPageScale method can work, include:

* XWalkSetting API setInitialPageScale method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setInitialPageScale
* XWalkView interface: load methods



### 70. The [XWalkViewSettingTextZoom](setting/XWalkViewSettingTextZoom.java) sample check XWalkSetting API getTextZoom & setTextZoom method can work, include:

* XWalkSetting API getTextZoom & setTextZoom method can work

This usecase covers following interface and methods:

* XWalkSetting interface: getTextZoom, setTextZoom
* XWalkView interface: load methods



### 71. The [XWalkViewSettingSupportZoom](setting/XWalkViewSettingSupportZoom.java) sample check XWalkSetting API support zoom method can work, include:

* XWalkSetting API setUseWideViewPort & getUseWideViewPort & setSupportZoom & supportZoom & setBuiltInZoomControls & getBuiltInZoomControls method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setUseWideViewPort, getUseWideViewPort, setSupportZoom, supportZoom, setBuiltInZoomControls, getBuiltInZoomControls methods
* XWalkView interface: load methods



### 72. The [XWalkViewSettingDefaultFontSize](setting/XWalkViewSettingDefaultFontSize.java) sample check XWalkSetting API set default font size method can work, include:

* XWalkSetting API setDefaultFontSize, getDefaultFontSize method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setDefaultFontSize, getDefaultFontSize methods
* XWalkView interface: load methods



### 73. The [XWalkViewSettingDefaultFixedFontSize](setting/XWalkViewSettingDefaultFixedFontSize.java) sample check XWalkSetting API set default fixed font size method can work, include:

* XWalkSetting API setDefaultFixedFontSize, getDefaultFixedFontSize method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setDefaultFixedFontSize, getDefaultFixedFontSize methods
* XWalkView interface: load methods



### 74. The [XWalkViewWithCaptureBitmapAsync](basic/XWalkViewWithCaptureBitmapAsync.java) sample check XWalkView can capture the visible content of web page, include:

* XWalkView API captureBitmapAsync method can work

This usecase covers following interface and methods:

* XWalkView interface: load, scaptureBitmapAsync methods



### 75. The [XWalkViewWithOnTouchListener](misc/XWalkViewWithOnTouchListener.java) sample check XWalkView API setOnTouchListener method can work, include:

* XWalkView API setOnTouchListener method can work

This usecase covers following interface and methods:

* XWalkSetting interface: setOnTouchListener
* XWalkView interface: load methods



### 76. The [XWalkViewWithOnJsAlert](client/XWalkViewWithOnJsAlert.java) sample check API XWalkUIClient.onJsAlert, XWalkUICLient.onJsConfirm and XWalkUIClient.onJsPropmt can work, include:

* API XWalkUIClient.onJsAlert, XWalkUICLient.onJsConfirm and XWalkUIClient.onJsPropmt can work

This usecase covers following interface and methods:

* XWalkUIClient interface: onJsAlert, onJsConfirm, onJsPropmt methods
* XWalkView interface: load methods



### 77. The [XWalkViewWithOnReceivedResponseHeaders](client/XWalkViewWithOnReceivedResponseHeaders.java) sample check API XWalkResourceClient.onReceivedResponseHeaders can work, include:

* API XWalkResourceClient.onReceivedResponseHeaders can work

This usecase covers following interface and methods:

* XWalkResourceClient interface: onReceivedResponseHeaders
* XWalkView interface: load methods



### 78. The [XWalkViewWithGetFavicon](basic/XWalkViewWithGetFavicon.java) sample check XWalkView can get favicon from the html, include:

* XWalkView API getFavicon method can work

This usecase covers following interface and methods:

* XWalkView interface: load, getFavicon methods



### 79. The [XWalkViewWithLoadExtension](misc/XWalkViewWithLoadExtension.java) sample check XWalkView can load external extensions dynamically, include:

* XWalkView API getExtensionManager().loadExtension method can work

This usecase covers following interface and methods:

* XWalkView interface: load, getExtensionManager().loadExtension methods



### 80. The [XWalkViewWithIframes](basic/XWalkViewWithIframes.java) sample check XWalkView can be reliable with iframes, include:

* XWalkView can be reliable with iframes

This usecase covers following interface and methods:

* XWalkView interface: load method
* ResourceClient interface: shouldInterceptLoadRequest method



### 81. The [XWalkViewWithClearSslPreferences](misc/XWalkViewWithClearSslPreferences.java) sample check XWalkView can clear ssl preferences, include:

* XWalkView can clear ssl preferences

This usecase covers following interface and methods:

* XWalkView interface: load, clearSslPreferences method
* ResourceClient interface: onReceivedSslError method



### 82. The [XWalkViewWithThemeColor](misc/XWalkViewWithThemeColor.java) sample demonstrates XWalkView can support theme-color meta tag by setting ENABLE_THEME_COLOR, include:

* XWalkView can set style value
* XWalkView can get style value

This usecase covers following interface and methods:

* XWalkPreferences interface: getBooleanValue, setValue



### 83. The [XWalkViewWithShouldInterceptLoadRequest](client/XWalkViewWithShouldInterceptLoadRequest.java) sample demonstrates XWalkResourceClient API shouldInterceptLoadRequest can work, include:

* XWalkView can set resource client
* shouldInterceptLoadRequest can work

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: shouldInterceptLoadRequest method



### 84. The [XWalkViewWithClearClientCertPreferences](basic/XWalkViewWithClearClientCertPreferences.java) sample demonstrates XWalkView can clear client certificate preferences, include:

* XWalkView can clear client certificate preferences

This usecase covers following interface and methods:

* XWalkView interface: load, clearClientCertPreferences methods
* ResourceClient interface: onReceivedClientCertRequest method



### 85. The [XWalkViewWithSetBackgroundColor](basic/XWalkViewWithSetBackgroundColor.java) sample check XWalkView can set background color without delay, include:

* XWalkView can set background color without delay

This usecase covers following interface and methods:

* XWalkView interface: load, setBackgroundColor method



### 86. The [XWalkViewWithNewLoad](basic/XWalkViewWithNewLoad.java) sample check XWalkView's new interface: load URL with specified HTTP headers, include:

* XWalkView can load url with specified HTTP headers

This usecase covers following interface and methods:

* XWalkView interface: load method



### 87. The [XWalkViewWithComputeScroll](extended/XWalkViewWithComputeScroll.java) sample check XWalkView can computeHorizontalScrollOffset, computeHorizontalScrollRange, computeVerticalScrollOffset, computeVerticalScrollRange and computeVerticalScrollExtent, include:

* XWalkView can computeHorizontalScrollOffset, computeHorizontalScrollRange, computeVerticalScrollOffset, computeVerticalScrollRange and computeVerticalScrollExtent

This usecase covers following interface and methods:

* XWalkView interface: load, computeHorizontalScrollOffset, computeHorizontalScrollRange, computeVerticalScrollOffset, computeVerticalScrollRange and computeVerticalScrollExtent methods


### 88. The [XWalkViewSettingDomStorageEnabled](setting/XWalkViewSettingDomStorageEnabled.java) sample check XWalkView can enable/disable DOM storage API, include:

* XWalkView can enable DOM storage API
* XWalkView can disable DOM storage API

This usecase covers following interface and methods:

* XWalkSettings interface: setDomStorageEnabled, getDomStorageEnabled


### 89. The [XWalkViewSettingSaveFormData](setting/XWalkViewSettingSaveFormData.java) sample check XWalkView can enable/disable form autocomplete and/or delete saved form data, include:

* XWalkView can enable saveFormData
* XWalkView can disable saveFormData

This usecase covers following interface and methods:

* XWalkSettings interface: setSaveFormData, getSaveFormData


### 90. The [XWalkViewSettingJavaScriptEnabled](setting/XWalkViewSettingJavaScriptEnabled.java) sample check XWalkView can enable/disable JavaScript, include:

* XWalkView can enable JavaScript
* XWalkView can disable JavaScript

This usecase covers following interface and methods:

* XWalkSettings interface: setJavaScript, getJavaScript


### 91. The [XWalkViewSettingJavaScriptCanOpenWindowsAutomatically](setting/XWalkViewSettingJavaScriptCanOpenWindowsAutomatically.java) sample check XWalkView can enable/disable JavaScriptCanOpenWindowsAutomatically, include:

* XWalkView can enable JavaScriptCanOpenWindowsAutomatically
* XWalkView can disable JavaScriptCanOpenWindowsAutomatically

This usecase covers following interface and methods:

* XWalkSettings interface: setJavaScriptCanOpenWindowsAutomatically, getJavaScriptCanOpenWindowsAutomatically

