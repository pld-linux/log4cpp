Summary:	Library for flexible logging
Summary(pl):	Biblioteka do elastycznego logowania
Name:		log4cpp
Version:	0.3.4b
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/log4cpp/%{name}-%{version}.tar.gz
# Source0-md5:	8051f012fcc58173e8015710d449457a
Patch0:		%{name}-am18.patch
Patch1:		%{name}-nolibs.patch
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

%description -l pl
Log4cpp to biblioteka klas C++ do elastycznego logowania do plików,
sysloga, IDSA i innych miejsc. Jest tworzona na podstawie biblioteki
Javy Log4j i pozostaje jak najbli¿ej jej API w granicach rozs±dku.

%package devel
Summary:	Header files for log4cpp
Summary(pl):	Pliki nag³ówkowe log4cpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the development and header files for log4cpp.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki log4cpp.

%package static
Summary:	Static log4cpp library
Summary(pl):	Statyczna biblioteka log4cpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static log4cpp library.

%description static -l pl
Ten pakiet zawiera statyczn± bibliotekê log4cpp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# extract BB_CHECK_OMNITHREADS and BB_CHECK_PTHREADS missing from m4
tail -n +4487 aclocal.m4 | head -n 96 > m4/BB_CHECK_THREADS.m4

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.css doc/html/*.png doc/html/*.html doc/html/api
%attr(755,root,root) %{_bindir}/log4cpp-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
