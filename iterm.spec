Summary:	Internationalized Terminal Emulator Framework
Summary(pl):	Szkielet dla umiêdzynarodowionego emulatora terminala
Name:		iterm
Version:	0.5
Release:	0.1
License:	Common Public License v0.5
Group:		Libraries
Source0:	http://www.doc.ic.ac.uk/~mbt99/Y/src/%{name}-%{version}-mbt.tar.gz
# Source0-md5:	e13a6273319e041fcf3b4800581ef62c
Patch0:		%{name}-make.patch
URL:		http://www-124.ibm.com/linux/projects/iterm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fribidi-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
#	INCLUDES="-I../../../lib/include -I."

# Xiterm
cd ../src
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
#	INCLUDES="-I../../../lib/include -I../lib"

# fbiterm
cd ../../fbiterm
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
#	INCLUDES="-I../../../lib/include"

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libiterm -p /sbin/ldconfig
%postun	-n libiterm -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

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
