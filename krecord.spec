Summary:	Sound recorder for KDE
Summary(pl):	Rejestrator d¼wiêku dla KDE
Name:		krecord
Version:	1.11
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://bytesex.org/misc/%{name}_%{version}.tar.gz
URL:		http://bytesex.org/krecord.html
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
A simple KDE interface to record sounds.

%description -l pl
Prosty interfejs KDE do rejestrowania d¼wiêku.

%prep
%setup -q

%build
KDEDIR="%{_prefix}"; export KDEDIR
kde_htmldir="%{_htmldir}"; export kde_htmldir
CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG} -I%{_includedir}/qt"
%configure2_13 \
	--disable-path-check

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/krecord
%{_applnkdir}/Multimedia/krecord.kdelnk
%{_datadir}/apps/krecord
