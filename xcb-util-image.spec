Summary:	XCB util-image module
Summary(pl.UTF-8):	Moduł XCB util-image
Name:		xcb-util-image
Version:	0.4.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# Source0-md5:	a67bfac2eff696170259ef1f5ce1b611
URL:		https://xcb.freedesktop.org/XcbUtil/
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xcb-proto >= 1.6
BuildRequires:	xcb-util-devel >= 0.4.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.8
BuildRequires:	xz
Requires:	libxcb >= 1.4
Requires:	xcb-util >= 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-image module provides the following library:
- image: Port of Xlib's XImage and XShmImage functions.

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util-image udostępnia następującą biliotekę:
- image: port funkcji XImage i XShmImage z Xlib.

%package devel
Summary:	Header files for XCB util-image library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-image
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4
Requires:	xcb-util-devel >= 0.4.0

%description devel
Header files for XCB util-image library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util-image.

%package static
Summary:	Static XCB util-image library
Summary(pl.UTF-8):	Statyczna biblioteka XCB util-image
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-image library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB util-image.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxcb-image.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libxcb-image.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-image.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-image.so
%{_includedir}/xcb/xcb_bitops.h
%{_includedir}/xcb/xcb_image.h
%{_includedir}/xcb/xcb_pixel.h
%{_pkgconfigdir}/xcb-image.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-image.a
