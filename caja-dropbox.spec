Summary: 		Dropbox extension for caja
Name: 			caja-dropbox
Version: 		1.6.0
Release: 		3%{?dist}
License: 		GPLv3+ and CC-BY-ND
Group: 			User Interface/Desktops
URL: 			https://linux.dropbox.com
Source0: 		https://linux.dropbox.com/packages/nautilus-dropbox-%{version}.tar.bz2

Patch0:         caja-dropbox_fix_autoconf-automake_deprecations.patch
Patch1:         caja-dropbox_nautilus_to_caja.patch

BuildRequires: 	mate-file-manager-devel
BuildRequires:  python-docutils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

# Run a fake X session 
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xauth
BuildRequires:  zlib-devel

Requires: 		mate-file-manager-extensions
Requires: 		pygtk2
Requires: 		hicolor-icon-theme

%description
Dropbox extension for caja file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%setup -q -n nautilus-dropbox-%{version}

%patch0 -p1 -b .deprecations
%patch1 -p1 -b .caja

autoreconf -i -f

%build
# xvfb-run is needed to find pygtk2
xvfb-run -a ./configure CFLAGS="$RPM_OPT_FLAGS"

xvfb-run -a make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/dropbox.desktop


%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc AUTHORS COPYING NEWS README 
%{_bindir}/dropbox
%{_datadir}/caja-dropbox/
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/dropbox.1.gz
%{_datadir}/applications/dropbox.desktop
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.so


%changelog
* Sat Jul 20 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-3
- add exports

* Thu May 16 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-2
- use a fake X session to find pygtk2 BR, fix build server issue
- fix autoconf/automake deprecations

* Sun May 12 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-1
- add require hicolor-icon-theme
- remove useless libmatenotify BR
- clean up BR's
- switch to current upstream source
- fix licence information

* Thu Mar 21 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-2
- initial build for fedora

* Fri Nov 16 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-1
- build against official fedora mate-desktop
- remove epoch
- test remove libmate require
- clean BR
- add rpm scriptlets
- improve spec file

* Mon Aug 27 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-0100
- build for f18

* Thu Jul 05 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-4
- switch to Mate-Desktop source

* Thu Feb 23 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-3
- fixed build error for i686

* Mon Feb 13 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-2
- rebuild for enable builds for .i686

* Thu Jan 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-1
- start building for caja   

