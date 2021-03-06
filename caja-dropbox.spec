# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.24

Summary: 		Dropbox extension for caja
Name: 			caja-dropbox
Version: 		%{branch}.0
Release: 		4%{?dist}
License: 		GPLv2+
Group: 			User Interface/Desktops
URL: 			https://mate-desktop.org
Source0: 		https://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

ExclusiveArch:  i686 x86_64

BuildRequires:  gcc
BuildRequires:  caja-devel
BuildRequires:  mate-common
BuildRequires:  python3-docutils
BuildRequires:  pygobject3-devel

Requires:       dropbox >= 1:2.10.0
Requires:       caja-core-extensions
Requires:       python3-gpg
Requires:       python3-gobject

%description
Dropbox extension for caja file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%autosetup -p1


%build
%configure --disable-static
%{make_build}

%install
%{make_install}

find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -f

rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_datadir}/caja-dropbox/*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/*
rm -rf %{buildroot}%{_datadir}/man/man1/*
rm -rf %{buildroot}%{_datadir}/applications/*


%files
%doc AUTHORS NEWS README
%license COPYING 
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.so
%{_datadir}/caja/extensions/libcaja-dropbox.caja-extension


%changelog
* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- update runtime dependencies

* Sat Mar 14 2020 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.24.0-1
- update to 1.24.0

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Mon Apr 08 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.22.0-2
- exclude archs again

* Sun Apr 07 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.22.0-1
- update to 1.22.0
- use some upstream patches
- build for all archs

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20.0-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Tue Jul 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.20.0-2
- Fix build for f29 python changes

* Wed May 02 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-1
- update to 1.20.0

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Thu Aug 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Sun Jun 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.14.0-1
- update to 1.14.0 release

* Sun Nov 15 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Sun Aug 09 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-3
- update to 1.10.0 release

* Sat Jan 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-3
- add ExclusiveArch

* Sat Dec 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-2
- use rpmfusion dropbox require
- fix license information
- remove non needed patches

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

