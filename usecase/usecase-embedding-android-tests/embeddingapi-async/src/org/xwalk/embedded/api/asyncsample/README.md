## Usecase Design

### 1. The [XWalkPreferencesActivityAsync](XWalkPreferencesActivityAsync.java) sample demonstrates XWALK-2376 feature basic functionalities, include:

* XWalkView can set style value
* XWalkView can get style value

This usecase covers following interface and methods:

* XWalkPreferences interface: setValue, getStringValue, getBooleanValue, getIntegerValue methods



### 2. The [EchoExtensionActivityAsync](EchoExtensionActivityAsync.java) sample demonstrates XWALK-3917 feature basic functionalities, include:

* extension can be supported

These two usecases cover following interface and methods:

* XWalkExtension interface: onMessage, onSyncMessage methods
* XWalkView interface: load method



### 3. The [MultiSurfaceViewsActivityAsync](MultiSurfaceViewsActivityAsync.java) and [MultiTextureViewsActivityAsync](MultiTextureViewsActivityAsync.java) sample demonstrate XWALK-2012 feature basic functionalities, include:

* Multiple surfaceViews can be shown in order at first
* Multiple surfaceViews can be shown in order when rotating the device screen 90 degrees
* Multiple surfaceViews can be shown in order when restoring the device screen
* Multiple textureViews can be shown in order at first
* Multiple textureViews can be shown in order when rotating the device screen 90 degrees
* Multiple textureViews can be shown in order when restoring the device screen

This usecase covers following interface and methods:

* XWalkPreference interface: setValue method
* XWalkView interface: load method



### 4. The [AnimatableXWalkViewActivityAsync](AnimatableXWalkViewActivityAsync.java) sample demonstrates how to use the basic functionalities of animatible XWalkView, include:

* Animatable XWalkView can be scaled down or scaled up

This usecase covers following interface and methods:

* XWalkPreference interface: setValue method
* XWalkView interface: load, getAlpha, getScaleX, getScaleY methods



### 5. The [LoadAppFromManifestLayoutActivityAsync](LoadAppFromManifestLayoutActivityAsync.java) sample demonstrates how to load app from manifest, include:

* XWalkView can load app from manifest

This usecase covers following interface and methods:

* XWalkView interface: loadAppFromManifest methods



### 6. The [MultiXWalkViewActivityAsync](MultiXWalkViewActivityAsync.java) sample demonstrates how to create multi instance, include:

* XWalkView can create multi instance

This usecase covers following interface and methods:

* XWalkView interface: load method



### 7. The [OnHideOnShowActivityAsync](OnHideOnShowActivityAsync.java) sample demonstrates XWalkView can hide and show, include:

* XWalkView can hide when clicking home key
* There is no short white screen displayed when clicking home key
* XWalkView can show when Click the 'EmbeddedAPISamples' app again

This usecase covers following interface and methods:

* XWalkView interface: load method



### 8. The [PauseTimersActivityAsync](PauseTimersActivityAsync.java) sample demonstrates XWalkView can pause timers, include:

* XWalkView can pause timers when it's pauseTimers() method is called
* XWalkView can resume timers when it's resumeTimers() method is called

This usecase covers following interface and methods:

* XWalkView interface: load, pauseTimers, resumeTimers methods



### 9. The [ResourceAndUIClientsActivityAsync](ResourceAndUIClientsActivityAsync.java) sample demonstrates how to set resource client and UI client, include:

* XWalkView can set resource client
* XWalkView can set UI client
* The log record the the implementation methods of resource client and UI client

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient, setUIClient methods
* ResourceClient interface: onLoadStarted, onLoadFinished, onProgressChanged, shouldInterceptLoadRequest, onReceivedLoadError methods
* UIClient interface: onJavascriptCloseWindow, onJavascriptModalDialog, onFullscreenToggled, openFileChooser, onScaleChanged methods



### 10. The [XWalkNavigationActivityAsync](XWalkNavigationActivityAsync.java) sample demonstrates how to forward and backward history, include:

* XWalkView can backward history client when go backward button is clicked
* XWalkView can forward history client when go forward button is clicked

This usecase covers following interface and methods:

* XWalkView interface: load, getNavigationHistory methods
* XWalkNavigationHistory interface: canGoForward, navigate, getCurrentItem methods
* XWalkNavigationItem interface: getOriginalUrl, getTitle methods



### 11. The [XWalkVersionAndAPIVersionAsync](XWalkVersionAndAPIVersionAsync.java) sample demonstrates how to get API version and xwalk version, include:

* XWalkView can get and show API version
* XWalkView can get and show xwalk version

This usecase covers following interface and methods:

* XWalkView interface: load, getAPIVersion, getXWalkVersion methods



### 12. The [XWalkViewWithLayoutActivityAsync](XWalkViewWithLayoutActivityAsync.java) sample demonstrates how to load view UI, include:

* XWalkView can load view UI

This usecase covers following interface and methods:

* XWalkView interface: load method



### 13. The [OnIconAvailableOnReceivedIconActivityAsync](OnIconAvailableOnReceivedIconActivityAsync.java) sample demonstrates how to load icon when it's available, include:

* XWalkView can load icon when it's available

This usecase covers following interface and methods:

* XWalkView interface: load method
* UIClient interface: onIconAvailable, onReceivedIcon methods



### 14. The [OnCreateWindowRequestedActivityAsync](OnCreateWindowRequestedActivityAsync.java) sample demonstrates how to create new window, include:

* XWalkView can create new window

This usecase covers following interface and methods:

* XWalkView interface: load method
* UIClient interface: onCreateWindowRequested methods



### 15. The [FullScreenActivityAsync](FullScreenActivityAsync.java) sample demonstrates how to enter and exit fullscreen, include:

* XWalkView can enter and exit fullscreen

This usecase covers following interface and methods:

* XWalkView interface: load, leaveFullscreen method



### 16. The [ShouldOverrideUrlLoadingActivityAsync](ShouldOverrideUrlLoadingActivityAsync.java) sample demonstrates how to trigger shouldOverrideUrlLoading method, include:

* XWalkView can trigger shouldOverrideUrlLoading method

This usecase covers following interface and methods:

* XWalkView interface: load method
* ResourceClient interface: shouldOverrideUrlLoading methods



### 17. The [XWalkViewWithTransparentAsync](XWalkViewWithTransparentAsync.java) sample check XWalkView's transparent feature whether display the view under the webview, include:

* XWalkView's transparent can display the view under the webview

This usecase covers following interface and methods:

* XWalkView interface: setZOrderOnTop, setBackgroundColor methods



### 18. The [XWalkViewWithRedirectionAsync](XWalkViewWithRedirectionAsync.java) sample verifies how many times onPageLoadStopped called when visit a web page with redirection, include:

* XWalkUIClient's onPageLoadStopped() method just be called once when visit a web page with redirection

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient, setUIClient methods
* ResourceClient interface: onProgressChanged method
* UIClient interface: onPageLoadStarted, onPageLoadStopped methods



### 19. The [XWalkViewWithLoadImageAsync](XWalkViewWithLoadImageAsync.java) sample load image from XWalkView, include:

* XWalkView can load image

This usecase covers following interface and methods:

* XWalkView interface: load, onActivityResult methods



### 20. The [XWalkViewWithClearCacheAsync](XWalkViewWithClearCacheAsync.java) sample check whether xwalkview can clear cache, include:

* XWalkView can clear cache

This usecase covers following interface and methods:

* XWalkView interface: load, clearCache methods
* UIClient interface: onPageLoadStopped methods



### 21. The [ContactExtensionActivityAsync](ContactExtensionActivityAsync.java) sample demonstrates XWALK-3917 feature basic functionalities, include:

* extension can be supported with additional permissions

These two usecases cover following interface and methods:

* XWalkExtension interface: onMessage methods
* XWalkView interface: load method



### 22. The [ZoomInAndOutXWalkViewActivityAsync](ZoomInAndOutXWalkViewActivityAsync.java) sample check whether xwalkview can zoom, include:

* XWalkView can zoom in, zoom out, zoom by

This usecase covers following interface and methods:

* XWalkView interface: load, zoomIn, zoomOut, zoomBy, canZoomOut, canZoomIn methods



### 23. The [XWalkViewWithDownloadListenerAsync](XWalkViewWithDownloadListenerActivityAsync.java) sample check whether xwalkview can setDownloadListener & override onDownloadStart, include:

* XWalkView can setDownloadListener & override onDownloadStart

This usecase covers following interface and methods:

* XWalkView interface: load, setDownloadListener, onDownloadStart methods



### 24. The [XWalkBlockAndErrorRedirectionAsync](XWalkBlockAndErrorRedirectionAsync.java) sample check whether xwalkview can block response and redirect when url or internet is not avaliable, include:

* XWalkView can block response & make error redirection

This usecase covers following interface and methods:

* XWalkView interface: load, setResourceClient methods
* ResourceClient interface: shouldInterceptLoadRequest, onReceivedLoadError methods



### 25. The [XWalkWithSaveStateAsync](XWalkWithSaveStateAsync.java) sample check whether xwalkview can saveState & restoreState bundle, include:

* XWalkView can saveState & restoreState bundle

This usecase covers following interface and methods:

* XWalkView interface: load, saveState, restoreState methods



### 26. The [XWalkWithInputConnectionAsync](XWalkWithInputConnectionAsync.java) sample check whether xwalkview can use onCreateInputConnection method, include:

* XWalkView can use onCreateInputConnection method

This usecase covers following interface and methods:

* XWalkView interface: load, onCreateInputConnection methods



### 27. The [XWalkViewWithDispatchKeyEventAsync](XWalkViewWithDispatchKeyEventAsync.java) sample check whether xwalkview can use dispatchKeyEvent method, include:

* XWalkView can use dispatchKeyEvent method

This usecase covers following interface and methods:

* XWalkView interface: load, dispatchKeyEvent methods



### 28. The [XWalkViewWithSetLanguageAsync](XWalkViewWithSetLanguageAsync.java) sample check whether xwalkview can set accept language, include:

* XWalkView can use setAcceptLanguages method

This usecase covers following interface and methods:

* XWalkView interface: load, setAcceptLanguages methods



### 29. The [XWalkViewWithDispatchDrawAsync](XWalkViewWithDispatchDrawAsync.java) sample check whether dispatchDraw method work as same as WebView, include:

* dispatchDraw can be override

This usecase covers following interface and methods:

* XWalkView interface: dispatchDraw methods


### 30. The [CookieManagerTestActivityAsync](CookieManagerTestActivityAsync.java) sample check whether XWalkCookieManager apis can work, include:

* XWalkCookieManager apis can work

This usecase covers following interface and methods:

* XWalkView interface: load method
* XWalkCookieManager interface: setAcceptCookie, acceptCookie, setCookie, getCookie, removeSessionCookie, removeAllCookie, hasCookies, removeExpiredCookie, flushCookieStore


### 31. The [XWalkViewWithOnDrawAsync](XWalkViewWithOnDrawAsync.java) sample check whether onDraw method work as same as WebView, include:

* onDraw can be override

This usecase covers following interface and methods:

* XWalkView interface: onDraw methods



### 32. The [XWalkViewWithOverScrollAsync](XWalkViewWithOverScrollAsync.java) sample check whether onOverScrolled method work as same as WebView, include:

* onOverScrolled can be override

This usecase covers following interface and methods:

* XWalkView interface: onOverScrolled methods



### 33. The [AcceptFileSchemeCookiesActivityAsync](AcceptFileSchemeCookiesActivityAsync.java) sample check whether XWalkCookieManager can set AcceptFileSchemeCookies, include:

* XWalkCookieManager apis can work

This usecase covers following interface and methods:

* XWalkView interface: onDraw method
* XWalkCookieManager interface: setAcceptFileSchemeCookies, allowFileSchemeCookies methods
