Summary:	A setproctitle() implementation
Name:		setproctitle
Version:	0.3.1
Release:	1
License:	LGPL or BSD
Group:		Applications/System
# ftp://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus/files/SRPMS
Source0:	%{name}-%{version}.tar
# Source0-md5:	7d59294eedb80127c62d01e6a6f2fd8f
URL:		http://sisyphus.ru/srpm/Sisyphus/setproctitle/get
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides setproctitle function for setting the invoking
process's title.

%package devel
Summary:	Header files and development documentation for setproctitle
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for setproctitle.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"
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
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/*.so.[0-9]

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/man3/*.3*
