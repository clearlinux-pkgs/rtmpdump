#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rtmpdump
Version  : 1
Release  : 6
URL      : https://git.ffmpeg.org/gitweb/rtmpdump.git/snapshot/c5f04a58fc2aeea6296ca7c44ee4734c18401aa3.tar.gz
Source0  : https://git.ffmpeg.org/gitweb/rtmpdump.git/snapshot/c5f04a58fc2aeea6296ca7c44ee4734c18401aa3.tar.gz
Summary  : RTMP implementation
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: rtmpdump-bin = %{version}-%{release}
Requires: rtmpdump-lib = %{version}-%{release}
Requires: rtmpdump-license = %{version}-%{release}
BuildRequires : gmp-dev
BuildRequires : gnutls-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
Patch1: 0001-Fix-build.patch

%description
RTMP Dump v2.4
(C) 2009 Andrej Stepanchuk
(C) 2009-2011 Howard Chu
(C) 2010 2a665470ced7adb7156fcef47f8199a6371c117b8a79e399a2771e0b36384090
(C) 2011 33ae1ce77301f4b4494faaa5f609f3c48b9dcf82
License: GPLv2
librtmp license: LGPLv2.1
http://rtmpdump.mplayerhq.hu/

%package bin
Summary: bin components for the rtmpdump package.
Group: Binaries
Requires: rtmpdump-license = %{version}-%{release}

%description bin
bin components for the rtmpdump package.


%package dev
Summary: dev components for the rtmpdump package.
Group: Development
Requires: rtmpdump-lib = %{version}-%{release}
Requires: rtmpdump-bin = %{version}-%{release}
Provides: rtmpdump-devel = %{version}-%{release}
Requires: rtmpdump = %{version}-%{release}

%description dev
dev components for the rtmpdump package.


%package lib
Summary: lib components for the rtmpdump package.
Group: Libraries
Requires: rtmpdump-license = %{version}-%{release}

%description lib
lib components for the rtmpdump package.


%package license
Summary: license components for the rtmpdump package.
Group: Default

%description license
license components for the rtmpdump package.


%prep
%setup -q -n rtmpdump-c5f04a5
cd %{_builddir}/rtmpdump-c5f04a5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624659030
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1624659030
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rtmpdump
cp %{_builddir}/rtmpdump-c5f04a5/COPYING %{buildroot}/usr/share/package-licenses/rtmpdump/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/rtmpdump-c5f04a5/librtmp/COPYING %{buildroot}/usr/share/package-licenses/rtmpdump/6138ce06f16aef800693fb256090749acbabd038
%make_install
## install_append content
mkdir -p ${buildroot}/usr/lib64
mv %{buildroot}/usr/lib/librtmp.so* %{buildroot}/usr/lib64/
sed -i 's|libdir=/usr/lib|libdir=/usr/lib64|' %{buildroot}/usr/lib64/pkgconfig/librtmp.pc
## install_append end

%files
%defattr(-,root,root,-)
/usr/man/man1/rtmpdump.1
/usr/man/man3/librtmp.3
/usr/man/man8/rtmpgw.8

%files bin
%defattr(-,root,root,-)
/usr/bin/rtmpdump
/usr/bin/rtmpgw
/usr/bin/rtmpsrv
/usr/bin/rtmpsuck

%files dev
%defattr(-,root,root,-)
/usr/include/librtmp/amf.h
/usr/include/librtmp/http.h
/usr/include/librtmp/log.h
/usr/include/librtmp/rtmp.h
/usr/lib64/librtmp.so
/usr/lib64/pkgconfig/librtmp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/librtmp.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rtmpdump/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/rtmpdump/6138ce06f16aef800693fb256090749acbabd038
