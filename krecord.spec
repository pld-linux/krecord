Summary:	Sound recorder for KDE
Summary(pl):	Rejestrator d¼wiêku dla KDE
Name:		krecord
Version:	1.15.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.bytesex.org/releases/krecord/%{name}_%{version}.tar.gz
# Source0-md5:	6673074a813cda1298366adf48618cd5
Source1:	%{name}.desktop
patch0:		%{name}-doc-path.patch
URL:		http://bytesex.org/krecord.html
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
A simple KDE interface to record sounds.

%description -l pl
Prosty interfejs KDE do rejestrowania d¼wiêku.

%prep
%setup -q
%patch0 -p1

%build
KDEDIR="%{_prefix}"; export KDEDIR
QTDIR="%{_prefix}"; export QTDIR
kde_htmldir="%{_htmldir}"; export kde_htmldir
#CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG} -I%{_includedir}/qt"
CFLAGS="%{rpmcflags}"; export CFLAGS

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/krecord
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/krecord
