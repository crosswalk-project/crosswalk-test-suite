%define _unpackaged_files_terminate_build 0

Summary: Webapi w3c manual test suite
Name: tct-manual-w3c-tests
Version: 2.2.1
Release: 1
License: BSD
Group: System/Libraries
Source: %name-%version.tar.gz

%description
This is webapi w3c manual test suite package

%prep
%setup -q


%build
./autogen
./configure --prefix=/usr
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

############## generate crx, wgt packge ####################
crx_installer="chromium-browser"
wgt_installer="wrt-installer"

cp -a $RPM_BUILD_ROOT  $RPM_BUILD_DIR/%name
cp -a manifest.json    $RPM_BUILD_DIR/%name
cp -a icon.png       $RPM_BUILD_DIR/%name

pre_dir=`pwd`
cd $RPM_BUILD_DIR/%name

cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=opt/%name/webrunner/index.html?testsuite=/usr/share/%name/tests.xml">
tests.full.xml
</head>
EOF

#create crx
if [[ %TYPE == "all" || %TYPE == "crx" ]]; then
    echo %TYPE
    type $crx_installer > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        export DISPLAY=:0
        cp -f $pre_dir/config.xml.crx ./config.xml
        $crx_installer --user-data-dir=/tmp  --pack-extension=../%name
        mv ../%name.crx  $RPM_BUILD_ROOT/opt/%name/
    fi
fi

#create zip
cp -f $pre_dir/config.xml.crx ./config.xml
cd $RPM_BUILD_DIR
zip -Drq %name-%version-%release.zip %name
cd $RPM_BUILD_DIR/%name

#create wgt
cp -f $pre_dir/config.xml.wgt ./config.xml
zip -rq $RPM_BUILD_ROOT/opt/%name/%name.wgt *

cd $pre_dir
rm -rf $RPM_BUILD_DIR/%name


mkdir -p $RPM_BUILD_ROOT/opt/unpacked_crx/%name
########################## end ##############################


%clean
rm -rf $RPM_BUILD_ROOT


%files
/opt/%name
/usr/share/%name
/opt/unpacked_crx/%name


%changelog


%post
############## install/uninstall crx, wgt packge ####################
crx_installer="chromium-browser"
wgt_installer="wrt-installer"

type $crx_installer > /dev/null 2>&1
if [ $? -eq 0 ]; then
    crx_install_dir="/opt/unpacked_crx/%name"
    cd $crx_install_dir
    [ -e /opt/%name/%name.crx ] && unzip /opt/%name/%name.crx
    cd -
fi

type $wgt_installer > /dev/null 2>&1
if [ $? -eq 0 ]; then
    [ -e /opt/%name/%name.wgt ] && $wgt_installer -i /opt/%name/%name.wgt
    if [ $? -eq 0 ]; then
        echo "Install /opt/%name/%name.wgt to /opt/usr/apps/`wrt-launcher -l 2> /dev/null | grep %name | tail -n 1 | awk '{ print $NF }'` done"
        echo "$(wrt-launcher -l | awk '/%name/ { print $(NF-1); exit }') sdbd rw" | smackload
    else
        echo "Install /opt/%name/%name.wgt fail ..."
    fi
    sync
fi


%postun
crx_installer="chromium-browser"
wgt_installer="wrt-installer"
type $wgt_installer > /dev/null 2>&1
if [ $? -eq 0 ]; then
    package_id=`wrt-launcher -l 2> /dev/null | grep %name | tail -n 1 | awk '{ print $NF }'`
    if [ -n "$(ps -ef | grep $package_id | grep -v grep | awk '{print $2}')" ]; then
        for i in $(ps -ef | grep $package_id | grep -v grep | awk '{print $2}')
        do
            kill -9 $i
            if [ "$?" -ne 0 ]; then
                echo "Kill the processes of %name fail ..."
            else
               echo "Kill the processes of %name done"
           fi
        done
    fi

    if [ -n "$package_id" ]; then
        $wgt_installer -un $package_id
       if [ "$?" -ne 0 ]; then
                echo "Uninstall %name fail ..."
        else
                echo "Uninstall %name done"
        fi
        sync
    fi

fi

rm -rf /opt/unpacked_crx/%name
########################## end ##############################
