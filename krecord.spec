%define kdeprefix /usr
%define version 1.1
%define release 1
%define sourcedir stable/1.1.1/apps/multimedia/sound

%define qtver  qt >= 1.42

%define kdename  krecord
Name: %{kdename}
Summary: Sound recorder for KDE
Version: %{version}
Release: %{release}
Serial: 1
#Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.gz
Source: %{kdename}-%{version}.tar.gz
License: GPL
Group: Applications/Sound
Buildroot: /var/tmp/%{kdename}-buildroot
Requires: %{qtver} kdesupport
Prefix: %{kdeprefix}

%description
A simple KDE interface to record sounds.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}

%build
export KDEDIR=%{kdeprefix}
export QTDIR=%{kdeprefix}
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
make CXXFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG -I/usr/include/qt" KDEDIR=%{kdeprefix}

%install
export KDEDIR=$RPM_BUILD_ROOT%{kdeprefix}
export QTDIR=$RPM_BUILD_ROOT%{kdeprefix}
install -d $RPM_BUILD_ROOT%{kdeprefix}/bin
install -d $RPM_BUILD_ROOT%{kdeprefix}/share/applnk/Multimedia

make install prefix=$RPM_BUILD_ROOT%{kdeprefix}

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
        $RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' \
        -e '/\/applnk\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}

%changelog
* Thu May 27 1999 Gerald Teschl <gerald@esi.ac.at>
- Created
