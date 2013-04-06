Summary:	A setproctitle() implementation
Summary(pl.UTF-8):	Implementacja funkcji setproctitle()
Name:		setproctitle
Version:	0.3.2
Release:	2
License:	LGPL v2.1+ (implementation), BSD (man page)
Group:		Libraries
# ftp://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus/files/SRPMS
Source0:	%{name}-%{version}.tar
# Source0-md5:	2677fb7e07f1a068fe079ec79bfae558
URL:		http://sisyphus.ru/srpm/Sisyphus/setproctitle/get
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides setproctitle() function for setting the invoking
process's title.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcję setproctitle() do ustawiania nazwy
działającego procesu.

%package devel
Summary:	Header file and development documentation for setproctitle library
Summary(pl.UTF-8):	Plik nagłówkowy i dokumentacja programisty do biblioteki setproctitle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file and development documentation for setproctitle library.

%description devel -l pl.UTF-8
Plik nagłówkowy i dokumentacja programisty do biblioteki setproctitle.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libsetproctitle.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libsetproctitle.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsetproctitle.so
%{_includedir}/setproctitle.h
%{_mandir}/man3/setproctitle.3*
