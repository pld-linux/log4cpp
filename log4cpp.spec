# TODO:
# - pl translations
#
Summary:	Library for flexible logging
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
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4cpp is library of C++ classes for flexible logging to files,
syslog, IDSA and other destinations. It is modeled after the Log4j
Java library, staying as close to their API as is reasonable.

%package devel
Summary:	Header files for log4cpp
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Contains development and header files for log4cpp.

%package static
Summary:	Static log4cpp libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Contains static log4cpp libraries.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/html*
%{_mandir}/man3/*
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_bindir}/log4cpp-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
