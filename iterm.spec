Summary:	Internationalized Terminal Emulator Framework
Summary(pl):	Szkielet dla umiêdzynarodowionego emulatora terminala
Name:		iterm
Version:	0.5
Release:	1
License:	Common Public License v0.5
Group:		Applications
Source0:	http://www.doc.ic.ac.uk/~mbt99/Y/src/%{name}-%{version}-mbt.tar.gz
# Source0-md5:	e13a6273319e041fcf3b4800581ef62c
Patch0:		%{name}-make.patch
URL:		http://www-124.ibm.com/linux/projects/iterm/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	fribidi-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	utempter-devel
# currently %{_datadir}/terminfo/i dir belongs to terminfo
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Iterm is a platform-independent framework for making Internationalized
Virtual Terminal Emulator. Implementing platform-dependent part of
this framework, you can easily build internationalized virtual
terminal/Widget.

%description -l pl
Iterm to niezale¿ny od platformy szkielet do tworzenia
umiêdzynarodowionych emulatorów wirtualnych terminali. Poprzez
zaimplementowanie zale¿nych od platformy czê¶ci szkieletu mo¿na ³atwo
zbudowaæ umiêdzynarodowiony program lub widget emulatora terminala.

%package -n libiterm
Summary:	Internationalized Terminal Emulator Library
Summary(pl):	Biblioteka umiêdzynarodowionego emulatora terminala
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libiterm
This is a portable library for internationalized terminal emulator.
All you need to make terminal emulator is to implements callback
functions, like a drawing string on specific column and row, or set
fore/background color and so on.

%description -n libiterm -l pl
libiterm to przeno¶na biblioteka dla umiêdzynarodowionego emulatora
terminala. Wszystko co trzeba zrobiæ aby otrzymaæ emulator, to
zaimplementowaæ funkcje callback takie jak rysowanie napisów w
okre¶lonej kolumnie i wierszu, ustawianie koloru napisów/t³a itp.

%package -n libiterm-devel
Summary:	Header files for libiterm library
Summary(pl):	Pliki nag³ówkowe biblioteki libiterm
Group:		Development/Libraries
Requires:	libiterm = %{version}-%{release}
Requires:	fribidi-devel
Requires:	utempter-devel

%description -n libiterm-devel
Header files for libiterm library.

%description -n libiterm-devel -l pl
Pliki nag³ówkowe biblioteki libiterm.

%package -n libiterm-static
Summary:	Static libiterm library
Summary(pl):	Statyczna biblioteka libiterm
Group:		Development/Libraries
Requires:	libiterm-devel = %{version}-%{release}

%description -n libiterm-static
Static libiterm library.

%description -n libiterm-static -l pl
Statyczna biblioteka libiterm.

%package -n libXiterm
Summary:	X Internationalized Terminal Widget
Summary(pl):	Widget umiêdzynarodowionego terminala dla X
Group:		Libraries
Requires:	libiterm = %{version}-%{release}

%description -n libXiterm
libXiterm is an X Internationalized Terminal Widget which uses
libiterm.

%description -n libXiterm -l pl
libXiterm to widget umiêdzynarodowionego terminala korzystaj±cy z
libiterm.

%package -n libXiterm-devel
Summary:	Header files for libXiterm library
Summary(pl):	Pliki nag³ówkowe biblioteki libXiterm
Group:		Development/Libraries
Requires:	libXiterm = %{version}-%{release}
Requires:	libiterm-devel = %{version}-%{release}

%description -n libXiterm-devel
Header files for libXiterm library.

%description -n libXiterm-devel -l pl
Pliki nag³ówkowe biblioteki libXiterm.

%package -n libXiterm-static
Summary:	Static libXiterm library
Summary(pl):	Statyczna biblioteka libXiterm
Group:		Development/Libraries
Requires:	libXiterm-devel = %{version}-%{release}

%description -n libXiterm-static
Static libXiterm library.

%description -n libXiterm-static -l pl
Statyczna biblioteka libXiterm.

%package Xaw
Summary:	X Internationalized Terminal Emulator
Summary(pl):	Umiêdzynarodowiony emulator terminala dla X
Group:		X11/Applications
Requires:	libXiterm = %{version}-%{release}

%description Xaw
xiterm is an X Internationalized Terminal Emulator which uses
libXiterm widget.

%description Xaw -l pl
xiterm to umiêdzynarodowiony emulator terminala dla X korzystaj±cy
z widgetu libXiterm.

%package fb
Summary:	fbiterm - FrameBuffer Internationalized TERMinal emulator
Summary(pl):	fbiterm - umiêdzynarodowiony emulator terminala dla framebuffera
Group:		Applications
Requires:	libiterm = %{version}-%{release}

%description fb
FrameBuffer Internationalized TERMinal emulator (fbiterm) is a
terminal program capable of displaying world languages on the Linux
console. It uses libiterm (Internationalized Terminal Framework),
Linux framebuffer, fonts loaded from X Window System font library,
as well as BiDi text layout engine. As such, it readily supports
BiDi/CTL and CJK languages.

%description fb -l pl
fbiterm (FrameBuffer Internationalized TERMinal emulator) to program
terminalowy potrafi±cy wy¶wietlaæ wiele jêzyków na linuksowej konsoli.
Korzysta z libiterm (szkieletu umiêdzynarodowionego terminala),
linuksowego framebuffera, fontów wczytywanych poprzez bibliotekê z X
Window System, a tak¿e silnika rysuj±cego tekst dwukierunkowy (BiDi).
Jako taki jest gotowy do obs³ugi jêzyków BiDi/CTL i CJK.

%package gtk
Summary:	gtkiterm - GTK+ version of iterm implementation
Summary(pl):	gtkiterm - wersja GTK+ implementacji iterm
Group:		X11/Applications
Requires:	libiterm = %{version}-%{release}

%description gtk
This is a very early version of gtkiterm: GTK+ version of iterm
implementation. I doesn't yet implement all the features of iterm, but
it works as a minimum terminal emulator. 

%description gtk
To jest bardzo wczesna wersja gtkiterm - portu GTK+ implementacji
iterm. Jeszcze nie ma zaimplementowanych wszystkich mo¿liwo¶ci iterma,
ale dzia³a jako minimalny emulator terminala.

%prep
%setup -q
%patch0 -p1

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
	--with-utempter
%{__make}

# libXiterm
cd ../unix/Xaw/lib
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%configure
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

%{__make} -C lib install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C unix/Xaw/lib install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C unix/Xaw/src install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C unix/fbiterm install \
	DESTDIR=$RPM_BUILD_ROOT

install unix/gtk/src/gtkiterm $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_appdefsdir}/ja
install unix/Xaw/src/XIterm $RPM_BUILD_ROOT%{_appdefsdir}
install unix/Xaw/src/XIterm.ja $RPM_BUILD_ROOT%{_appdefsdir}/ja/XIterm

install -d $RPM_BUILD_ROOT%{_datadir}/terminfo
tic -o $RPM_BUILD_ROOT%{_datadir}/terminfo unix/terminfo/iterm.terminfo

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

%files -n libiterm-static
%defattr(644,root,root,755)
%{_libdir}/libiterm.a

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

%files -n libXiterm-static
%defattr(644,root,root,755)
%{_libdir}/libXiterm.a

%files Xaw
%defattr(644,root,root,755)
%doc unix/Xaw/src/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_bindir}/xiterm
%{_appdefsdir}/XIterm
%lang(ja) %{_appdefsdir}/ja/XIterm

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
