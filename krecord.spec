Summary:	Sound recorder for KDE
Name:		krecord
Version:	1.4
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	ftp://ftp.kde.org/pub/kde/Attic/old/1.1.2/apps/multimedia/sound/%{name}-%{version}.tar.gz
BuildRequires:	qt-devel >= 1.42
BuildRequires:	kdesupport-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple KDE interface to record sounds.

%prep
%setup -q -n %{name}

%build
KDEDIR=%{kdeprefix} ; export KDEDIR
QTDIR=%{kdeprefix} ; export QTDIR
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
%{__make} CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG} -I/usr/include/qt" KDEDIR=%{kdeprefix}

%install
rm -rf $RPM_BUILD_ROOT
KDEDIR=$RPM_BUILD_ROOT%{kdeprefix} ; export KDEDIR
QTDIR=$RPM_BUILD_ROOT%{kdeprefix} ; export QTDIR
install -d $RPM_BUILD_ROOT%{kdeprefix}/bin
install -d $RPM_BUILD_ROOT%{kdeprefix}/share/applnk/Multimedia

%{__make} install prefix=$RPM_BUILD_ROOT%{kdeprefix}

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
%defattr(644,root,root,755)
