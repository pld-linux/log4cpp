Summary:	Library for flexible logging
Summary(pl.UTF-8):	Biblioteka do elastycznego logowania
Name:		log4cpp
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/log4cpp/%{name}-%{version}.tar.gz
# Source0-md5:	1face50ead0790d1297dfb04bacf273c
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-lt.patch
URL:		http://log4cpp.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4cpp is library of C++ classes for flexible logging to files,
syslog, IDSA and other destinations. It is modeled after the Log4j
Java library, staying as close to their API as is reasonable.

%description -l pl.UTF-8
Log4cpp to biblioteka klas C++ do elastycznego logowania do plików,
sysloga, IDSA i innych miejsc. Jest tworzona na podstawie biblioteki
Javy Log4j i pozostaje jak najbliżej jej API w granicach rozsądku.

%package devel
Summary:	Header files for log4cpp
Summary(pl.UTF-8):	Pliki nagłówkowe log4cpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the development and header files for log4cpp.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki log4cpp.

%package static
Summary:	Static log4cpp library
Summary(pl.UTF-8):	Statyczna biblioteka log4cpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static log4cpp library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę log4cpp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-doxygen
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT/removeit \
	mandir=$RPM_BUILD_ROOT%{_mandir}

rm -rf $RPM_BUILD_ROOT/removeit

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/liblog4cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cpp.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/html/default.css doc/html/sflogo.png doc/html/index.html doc/html/api
%attr(755,root,root) %{_bindir}/log4cpp-config
%attr(755,root,root) %{_libdir}/liblog4cpp.so
%{_libdir}/liblog4cpp.la
%{_includedir}/log4cpp
%{_mandir}/man3/log4cpp.3*
%{_mandir}/man3/log4cpp::*.3*
%{_aclocaldir}/log4cpp.m4
%{_pkgconfigdir}/log4cpp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblog4cpp.a
