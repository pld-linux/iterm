#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Internationalized Terminal Emulator Framework
Summary(pl.UTF-8):	Szkielet dla umiędzynarodowionego emulatora terminala
Name:		iterm
Version:	0.5
Release:	6
License:	Common Public License v0.5
Group:		Applications
Source0:	http://www.doc.ic.ac.uk/~mbt99/Y/src/%{name}-%{version}-mbt.tar.gz
# Source0-md5:	e13a6273319e041fcf3b4800581ef62c
Source1:	gtkiterm.desktop
Source2:	xiterm.desktop
Patch0:		%{name}-make.patch
Patch1:		%{name}-256-colors.patch
Patch2:		%{name}-fb-scroll.patch
Patch3:		%{name}-terminfo.patch
Patch4:		%{name}-fb-direct.patch
Patch5:		%{name}-gcc4.patch
Patch6:		%{name}-fb-bold_font.patch
Patch7:		%{name}-fb-direct16.patch
URL:		http://www-124.ibm.com/linux/projects/iterm/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	fribidi-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	pkgconfig
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-proto-fontsproto-devel
# currently %{_datadir}/terminfo/i dir belongs to terminfo
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Iterm is a platform-independent framework for making Internationalized
Virtual Terminal Emulator. Implementing platform-dependent part of
this framework, you can easily build internationalized virtual
terminal/Widget.

%description -l pl.UTF-8
Iterm to niezależny od platformy szkielet do tworzenia
umiędzynarodowionych emulatorów wirtualnych terminali. Poprzez
zaimplementowanie zależnych od platformy części szkieletu można łatwo
zbudować umiędzynarodowiony program lub widget emulatora terminala.

%package -n libiterm
Summary:	Internationalized Terminal Emulator Library
Summary(pl.UTF-8):	Biblioteka umiędzynarodowionego emulatora terminala
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libiterm
This is a portable library for internationalized terminal emulator.
All you need to make terminal emulator is to implements callback
functions, like a drawing string on specific column and row, or set
fore/background color and so on.

%description -n libiterm -l pl.UTF-8
libiterm to przenośna biblioteka dla umiędzynarodowionego emulatora
terminala. Wszystko co trzeba zrobić aby otrzymać emulator, to
zaimplementować funkcje callback takie jak rysowanie napisów w
określonej kolumnie i wierszu, ustawianie koloru napisów/tła itp.

%package -n libiterm-devel
Summary:	Header files for libiterm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libiterm
Group:		Development/Libraries
Requires:	libiterm = %{version}-%{release}
Requires:	fribidi-devel
Requires:	utempter-devel

%description -n libiterm-devel
Header files for libiterm library.

%description -n libiterm-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libiterm.

%package -n libiterm-static
Summary:	Static libiterm library
Summary(pl.UTF-8):	Statyczna biblioteka libiterm
Group:		Development/Libraries
Requires:	libiterm-devel = %{version}-%{release}

%description -n libiterm-static
Static libiterm library.

%description -n libiterm-static -l pl.UTF-8
Statyczna biblioteka libiterm.

%package -n libXiterm
Summary:	X Internationalized Terminal Widget
Summary(pl.UTF-8):	Widget umiędzynarodowionego terminala dla X
Group:		Libraries
Requires:	libiterm = %{version}-%{release}

%description -n libXiterm
libXiterm is an X Internationalized Terminal Widget which uses
libiterm.

%description -n libXiterm -l pl.UTF-8
libXiterm to widget umiędzynarodowionego terminala korzystający z
libiterm.

%package -n libXiterm-devel
Summary:	Header files for libXiterm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXiterm
Group:		Development/Libraries
Requires:	libXiterm = %{version}-%{release}
Requires:	libiterm-devel = %{version}-%{release}

%description -n libXiterm-devel
Header files for libXiterm library.

%description -n libXiterm-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libXiterm.

%package -n libXiterm-static
Summary:	Static libXiterm library
Summary(pl.UTF-8):	Statyczna biblioteka libXiterm
Group:		Development/Libraries
Requires:	libXiterm-devel = %{version}-%{release}

%description -n libXiterm-static
Static libXiterm library.

%description -n libXiterm-static -l pl.UTF-8
Statyczna biblioteka libXiterm.

%package Xaw
Summary:	X Internationalized Terminal Emulator
Summary(pl.UTF-8):	Umiędzynarodowiony emulator terminala dla X
Group:		X11/Applications
Requires:	libXiterm = %{version}-%{release}

%description Xaw
xiterm is an X Internationalized Terminal Emulator which uses
libXiterm widget.

%description Xaw -l pl.UTF-8
xiterm to umiędzynarodowiony emulator terminala dla X korzystający
z widgetu libXiterm.

%package fb
Summary:	fbiterm - FrameBuffer Internationalized TERMinal emulator
Summary(pl.UTF-8):	fbiterm - umiędzynarodowiony emulator terminala dla framebuffera
Group:		Applications
Requires:	libiterm = %{version}-%{release}

%description fb
FrameBuffer Internationalized TERMinal emulator (fbiterm) is a
terminal program capable of displaying world languages on the Linux
console. It uses libiterm (Internationalized Terminal Framework),
Linux framebuffer, fonts loaded from X Window System font library,
as well as BiDi text layout engine. As such, it readily supports
BiDi/CTL and CJK languages.

%description fb -l pl.UTF-8
fbiterm (FrameBuffer Internationalized TERMinal emulator) to program
terminalowy potrafiący wyświetlać wiele języków na linuksowej konsoli.
Korzysta z libiterm (szkieletu umiędzynarodowionego terminala),
linuksowego framebuffera, fontów wczytywanych poprzez bibliotekę z X
Window System, a także silnika rysującego tekst dwukierunkowy (BiDi).
Jako taki jest gotowy do obsługi języków BiDi/CTL i CJK.

%package gtk
Summary:	gtkiterm - GTK+ version of iterm implementation
Summary(pl.UTF-8):	gtkiterm - wersja GTK+ implementacji iterm
Group:		X11/Applications
Requires:	libiterm = %{version}-%{release}

%description gtk
This is a very early version of gtkiterm: GTK+ version of iterm
implementation. I doesn't yet implement all the features of iterm, but
it works as a minimum terminal emulator. 

%description gtk -l pl.UTF-8
To jest bardzo wczesna wersja gtkiterm - portu GTK+ implementacji
iterm. Jeszcze nie ma zaimplementowanych wszystkich możliwości iterma,
ale działa jako minimalny emulator terminala.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

%build
# libiterm
cd lib
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# no liblayout - disable (default) pls, enable fribidi instead
%configure \
	--disable-pls \
	--enable-fribidi \
	--with-utempter \
	%{!?with_static_libs:--disable-static}
%{__make}

# libXiterm
cd ../unix/Xaw/lib
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

# Xiterm
cd ../src
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

# fbiterm
cd ../../fbiterm
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--x-includes=%{_includedir}
%{__make}

# gtkiterm
cd ../gtk
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	INCLUDES="-I../../../lib/include" \
	LDFLAGS="-L../../../lib/src/.libs"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdefsdir}/ja,%{_datadir}/terminfo,%{_desktopdir}}

%{__make} -C lib install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C unix/Xaw/lib install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C unix/Xaw/src install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C unix/fbiterm install \
	DESTDIR=$RPM_BUILD_ROOT

install unix/gtk/src/gtkiterm $RPM_BUILD_ROOT%{_bindir}
install unix/Xaw/src/XIterm $RPM_BUILD_ROOT%{_appdefsdir}
install unix/Xaw/src/XIterm.ja $RPM_BUILD_ROOT%{_appdefsdir}/ja/XIterm

tic -o $RPM_BUILD_ROOT%{_datadir}/terminfo unix/terminfo/iterm.terminfo

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libiterm -p /sbin/ldconfig
%postun	-n libiterm -p /sbin/ldconfig

%post	-n libXiterm -p /sbin/ldconfig
%postun	-n libXiterm -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README RELNOTES
%lang(ja) %doc README.jp
%lang(zh_CN) %doc README.zh_CN RELNOTES.zh_CN
%{_datadir}/terminfo/i/iterm
%{_datadir}/terminfo/i/iterm-am
%{_datadir}/terminfo/i/iterm-color

%files -n libiterm
%defattr(644,root,root,755)
%doc lib/{AUTHORS,COPYING,ChangeLog,README}
%lang(ja) %doc lib/README.jp
%lang(zh_CN) %doc lib/README.zh_CN
%attr(755,root,root) %{_libdir}/libiterm.so.*.*.*

%files -n libiterm-devel
%defattr(644,root,root,755)
%doc lib/docs/html/*
%attr(755,root,root) %{_libdir}/libiterm.so
%{_libdir}/libiterm.la
%{_includedir}/iterm

%if %{with static_libs}
%files -n libiterm-static
%defattr(644,root,root,755)
%{_libdir}/libiterm.a
%endif

%files -n libXiterm
%defattr(644,root,root,755)
%doc unix/Xaw/README unix/Xaw/lib/{AUTHORS,ChangeLog}
%lang(ja) %doc unix/Xaw/README.jp
%lang(zh_CN) %doc unix/Xaw/README.zh_CN
%attr(755,root,root) %{_libdir}/libXiterm.so.*.*.*

%files -n libXiterm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXiterm.so
%{_libdir}/libXiterm.la
%{_includedir}/Iterm*.h

%if %{with static_libs}
%files -n libXiterm-static
%defattr(644,root,root,755)
%{_libdir}/libXiterm.a
%endif

%files Xaw
%defattr(644,root,root,755)
%doc unix/Xaw/src/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_bindir}/xiterm
%{_appdefsdir}/XIterm
%lang(ja) %{_appdefsdir}/ja/XIterm
%{_desktopdir}/xiterm.desktop

%files fb
%defattr(644,root,root,755)
%doc unix/fbiterm/{AUTHORS,ChangeLog,README}
%lang(ja) %doc unix/fbiterm/README.jp
%lang(zh_CN) %doc unix/fbiterm/README.zh_CN
%attr(755,root,root) %{_bindir}/fbiterm

%files gtk
%defattr(644,root,root,755)
%doc unix/gtk/README
%attr(755,root,root) %{_bindir}/gtkiterm
%{_desktopdir}/gtkiterm.desktop
