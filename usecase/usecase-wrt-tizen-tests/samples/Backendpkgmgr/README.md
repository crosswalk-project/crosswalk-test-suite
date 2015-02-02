## Usecase Design

This sample demonstrates XWALK-1731 feature basic functionalities, include:

* pkgcmd with option to perform install/uninstall/list task.

This usecase covers following methods:

* pkgcmd -i -t wgt -p ${package} -q
* pkgcmd -u -n ${id} -q
* pkgcmd -l -t ${type} , type:rpm,xpk,wgt
* pkgcmd -s -n ${id} -t ${type}
