Summary:	Sound recorder for KDE
Name:		krecord
Version:	1.1
Release:	1
Serial:		1
License:	GPL
Group:		Applications/Sound
Source:		ftp://ftp.kde.org:/pub/kde/stable/1.1.1/apps/multimedia/sound/%{name}-%{version}.tar.gz
BUildPrereq:	qt-devel >= 1.42
BUildPrereq:	kdesupport-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
A simple KDE interface to record sounds.

%prep
%setup -q -n %{name}

%build
export KDEDIR=%{kdeprefix}
export QTDIR=%{kdeprefix}
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
make CXXFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG -I/usr/include/qt" KDEDIR=%{kdeprefix}

%install
rm -rf $RPM_BUILD_ROOT
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
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{kdename}
