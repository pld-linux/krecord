Summary:	Sound recorder for KDE
Summary(pl):	Rejestrator d¼wiêku dla KDE
Name:		krecord
Version:	1.4
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://ftp.kde.org/pub/kde/Attic/old/1.1.2/apps/multimedia/sound/%{name}-%{version}.tar.gz
BuildRequires:	qt-devel >= 1.42
BuildRequires:	kdesupport-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		kdeprefix	%{_prefix}

%description
A simple KDE interface to record sounds.

%description -l pl
Prosty interfejs KDE do rejestrowania d¼wiêku.

%prep
%setup -q -n %{name}

%build
KDEDIR=%{kdeprefix} ; export KDEDIR
QTDIR=%{kdeprefix} ; export QTDIR
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
%{__make} CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG} -I%{_includedir}/qt" KDEDIR=%{kdeprefix}

%install
rm -rf $RPM_BUILD_ROOT
KDEDIR=$RPM_BUILD_ROOT%{kdeprefix} ; export KDEDIR
QTDIR=$RPM_BUILD_ROOT%{kdeprefix} ; export QTDIR
install -d $RPM_BUILD_ROOT%{kdeprefix}/bin
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

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
