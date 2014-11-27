## Usecase Design

This sample demonstrates Advertising feature basic functionalities, include:

* Create, show and destroy an advertising

This usecase covers following interfaces and methods:

* xwalk interface: experimental
* experimental interface: ad
* Advertising interface: create(RequestOptions requestOptions)
* Advertise interface: destroy(), show(boolean show), onopen, onclose
* RequestOptions interface: service, publisherId, type, size, bannerAtTop, overlap

Precondition:

* Google Play developer account: The pubID can be changed to yourself admob public ID
* This Advertising test need extension resources
** Clone source code from https://github.com/crosswalk-project/crosswalk-android-extensions
** Build ad.zip extension refer to https://github.com/crosswalk-project/crosswalk-android-extensions/blob/master/README.md
** unzip ad.zip then copy the ad floder to /samples/Advertising/res
