Summary: 		Dropbox extension for caja
Name: 			caja-dropbox
Version: 		1.8.0
Release: 		1%{?dist}
License: 		GPLv3+ and CC-BY-ND
Group: 			User Interface/Desktops
URL: 			https://github.com/mate-desktop/caja-dropbox
Source0: 		http://pub.mate-desktop.org/releases/1.8/caja-dropbox-%{version}.tar.xz
# script binary with serialize images
Source1: 		caja-dropbox

Patch2:         caja-dropbox-1.8.0_disable-creation-of-dropbox-script-binary.patch
Patch3:         caja-dropbox_fix-pygtk-in-configure.patch

BuildRequires: 	caja-devel
BuildRequires:  python-docutils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pygobject2-devel
BuildRequires:  pygtk2-devel

Requires: 		caja-extensions
Requires: 		pygtk2
Requires: 		hicolor-icon-theme

%description
Dropbox extension for caja file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%setup -q

%patch2 -p1 -b .disable-creation

autoreconf -i -f
%patch3 -p1 -b .pygtk

cp %{SOURCE1} caja-dropbox

%build
%configure

make %{?_smp_mflags}

%install
%{make_install}

mkdir -m 755 -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/caja-dropbox

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/caja-dropbox.desktop


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
%{_bindir}/caja-dropbox
%{_datadir}/caja-dropbox/
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/caja-dropbox.1.gz
%{_datadir}/applications/caja-dropbox.desktop
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.so


%changelog
* Fri Oct 10 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-1
- switch to mate upstream
- update to 1.8.0 release

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-6
- bump version to fix build

* Sun Jul 13 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-5
- try use a fake X session to find pygtk2 BR

* Sun Jul 21 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-4
- don't use fake X session for build server
- add script binary with serialize images
- fix pygtk2 configure issue

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

