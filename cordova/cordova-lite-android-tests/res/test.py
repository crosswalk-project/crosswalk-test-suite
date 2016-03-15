import os
import commands
import sys
import json
import util
from optparse import OptionParser
PKG_ARCHS = ["x86", "arm", "x86_64", "arm64"]

util.setUp()
try:
    usage = "Usage: ./test.py -m shared -a x86"
    opts_parser = OptionParser(usage=usage)
    opts_parser.add_option(
        "-a",
        "--arch",
        dest="pkgarch",
        help="specify the apk arch, e.g. x86, arm, x86_64, arm64")
    global BUILD_PARAMETERS
    (BUILD_PARAMETERS, args) = opts_parser.parse_args()
except Exception as e:
    print "Got wrong options: %s, exit ..." % e
    sys.exit(1)


if not BUILD_PARAMETERS.pkgarch:
    print "Please add the -a parameter for the pkgarch"
    sys.exit(1)
elif BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
    print "Wrong pkg-arch, only support: %s, exit ..." % PKG_ARCHS
    sys.exit(1)

app_name = "CrosswalkVersion"
pkg_name = "com.example.crosswalkVersion1"
current_path_tmp = os.getcwd()
project_path = os.path.join(current_path_tmp, app_name)
util.create(app_name, pkg_name, current_path_tmp)

main_version = util.CROSSWALK_VERSION.split('.')[0]

latestVersion = util.getLatestCrosswalkVersion(util.CROSSWALK_BRANCH, main_version)

pkg_mode_tmp = "core"
apk_name_arch = "armv7"
pack_arch_tmp = "arm"

if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch != "arm":
    apk_name_arch = BUILD_PARAMETERS.pkgarch
    if BUILD_PARAMETERS.pkgarch == "x86":
        pack_arch_tmp = "x86"
    elif BUILD_PARAMETERS.pkgarch == "x86_64":
        pack_arch_tmp = "x86 --xwalk64bit"
    elif BUILD_PARAMETERS.pkgarch == "arm64":
        pack_arch_tmp = "arm --xwalk64bit"


VERSION_TYPES_EXPECTED = {'org.xwalk:xwalk_core_library_canary:%s+' % main_version: latestVersion,
                          'xwalk_core_library_canary:%s+' % main_version: latestVersion,
                          '%s+' % main_version: latestVersion,
                          '%s' % main_version: latestVersion,
                          'org.xwalk:xwalk_core_library_canary:%s' % util.CROSSWALK_VERSION: util.CROSSWALK_VERSION,
                          'xwalk_core_library_canary:%s' % util.CROSSWALK_VERSION: util.CROSSWALK_VERSION,
                          '%s' % util.CROSSWALK_VERSION: util.CROSSWALK_VERSION}


count = 1
for version_tmp in VERSION_TYPES_EXPECTED:
    os.system('cp ../index.html www/index.html')
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % VERSION_TYPES_EXPECTED[version_tmp])
    util.replaceUserString(
            project_path,
            'www/index.html',
            '{expectedVersion}',
            VERSION_TYPES_EXPECTED[version_tmp])
    print version_tmp
    print VERSION_TYPES_EXPECTED[version_tmp]
    util.installWebviewPlugin("lite", version_tmp)
    util.build(app_name, pack_arch_tmp)

    apk_source = os.path.join(project_path, "platforms", "android", 
            "build", "outputs", "apk", "android-%s-debug.apk" % apk_name_arch)
    apk_dest = os.path.join(current_path_tmp, "CrosswalkVersion_%s_%d.apk" % (util.CROSSWALK_BRANCH, count))
    util.doCopy(apk_source, apk_dest)

    count = count + 1
    util.removeWebviewPlugin()
    os.system('rm -r platforms/android/build/outputs/apk/*.apk')

    util.installWebviewPlugin("lite")
    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\"' \
            ' value=\\"%s\\" \/>/g" config.xml' % version_tmp)
    util.build(app_name, pack_arch_tmp)
    os.system('cp platforms/android/build/outputs/apk/android-%s-debug.apk ../CrosswalkVersion_%s_%d.apk' 
        % (apk_name_arch, util.CROSSWALK_BRANCH, count))
    count = count + 1
    util.removeWebviewPlugin()
    os.system('rm -r platforms/android/build/outputs/apk/*.apk')

for i in range(count - 1):
    util.checkApkExist("../CrosswalkVersion_%s_%d.apk" % (util.CROSSWALK_BRANCH, (i + 1)))


