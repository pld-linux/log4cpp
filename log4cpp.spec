Summary:	Library for flexible logging
Summary(pl):	Biblioteka do elastycznego logowania
Name:		log4cpp
Version:	0.2.8
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3162d64a8ed6e4c2d5887410a34a27a3
URL:		http://log4cpp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Requires:	%{name} = %{version}

%description devel
This package contains the development and header files for log4cpp.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki log4cpp.

%package static
Summary:	Static log4cpp library
Summary(pl):	Statyczna biblioteka log4cpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static log4cpp library.

%description static -l pl
Ten pakiet zawiera statyczn± bibliotekê log4cpp.

%prep
%setup -q

%build
rm -f missing
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
	docdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/html*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/log4cpp-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
