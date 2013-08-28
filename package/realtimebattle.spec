Name:           realtimebattle
Version:        1.0.8
Release:        15%{?dist}
Summary:        RealTimeBattle is a programming game for Unix, in which robots controlled by programs are fighting each other.

Group:          X11/Games
License:        GPLv2
URL:            http://realtimebattle.sourceforge.net/
#Source0:        http://hivelocity.dl.sourceforge.net/project/realtimebattle/RealTimeBattle-1.0.x/RealTimeBattle%201.0.8/RealTimeBattle-1.0.8-Ext.tar.gz
Source0:        realtimebattle-%{version}.tar.gz
# all these patches were pulled verbatim from the debian package
Patch0:         realtimebattle-1.0.8-13.debian.patch
Patch1:         realtimebattle-desktop-file.patch

BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  java-1.7.0-openjdk-devel
BuildRequires:  desktop-file-utils
Requires:       gtk2
Requires:       glib2
Requires:       java-1.7.0-openjdk

%description
RealTimeBattle is a programming game for Unix, in which robots controlled by
programs are fighting each other. The goal is to destroy the enemies, using the
radar to examine the environment and the cannon to shoot.

%package devel
Summary: Development package for %{name}
Group: X11/Games
Requires: %{name}-%{version}-%{release}

%description devel
Header files for realtimebattle

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --prefix=/usr --with-rtb-dir=%{_libdir}/realtimebattle

make

%install
make install DESTDIR=%{buildroot}

# removing the generated locale.alias so that it doesn't conflict with the
# system one

rm %{buildroot}/%{_datadir}/locale/locale.alias

# installing icon and desktop file
mkdir -p %{buildroot}/%{_datadir}/icons/
install RealTimeBattle.xpm %{buildroot}/%{_datadir}/icons/
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications realtimebattle.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/realtimebattle.desktop

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/realtimebattle
%dir %{_libdir}/realtimebattle
%attr(755,root,root) %{_libdir}/realtimebattle/*

# this grabs stuff from glibc, needs to be more specific
%attr(755,root,root) %{_datadir}/locale/*
%attr(755,root,root) %{_datadir}/info/*

# icon and desktop file
%attr(755,root,root) %{_datadir}/applications/realtimebattle.desktop
%attr(755,root,root) %{_datadir}/icons/RealTimeBattle.xpm

%files devel
%attr(755,root,root) %{_includedir}/RealTimeBattle/*

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons &>/dev/null || :

%changelog
* Thu Aug 22 2013 Tim Flink <tflink@fedoraproject.org> - 1.0.8-15
- Added desktop file and installed icon

* Wed Aug 21 2013 Tim Flink <tflink@fedoraproject.org> - 1.0.8-14
- Converted package from deb to rpm

# the following is the changelog extracted from the realtimebattle debian
# package

* Fri May 18 2012 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-13
- Realy include full patch from Cyril Brulebois <kibi@debian.org>

* Sat Apr 07 2012 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-12
- Bug fix: "LDFLAGS hardening flags missing", thanks to Simon Ruderich
- Closes debian #667956).

* Sat Apr 07 2012 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-11
- Fixes from Cyril Brulebois <kibi@debian.org>:
  * Fix FTBFS with gcc 4.7 by fixing missing <unistd.h> includes
  * Closes: #667351).
- fixes from Niels Thykier:
   * Added build-arch and build-indep to debian/rules.
   * Reduce default-jdk-builddep to default-jdk and use default-java.
   * Use buildflags.mk from dpkg-dev to set default build flags.
     - This enables hardning build by default.
   * Patched team-framework/log/sysloglogdriver.cpp, which was using
     a non-constant as a format string to syslog.
- Fixes from RÃ©mi Vanicat:
   * New standards-version: 3.9.3
   * Include path by Niels Thykier (Closes: debian #648081)
   * Add python to build depend for some robots

* Tue Sep 29 2009 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-10
- Use default-jdk-builddep and default-jre for jBot (Closes: debian #548811)
- Use ${misc:Depends} where needed
- Corrected build depend for dephelper
- Deleting postinst and prerm that are not needed anymore
- New Standards-Version: 3.8.3

* Wed May 20 2009 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-9
- Use ecj to build jBot (Closes: #529506)
- Going to Standards-Version: 3.8.1.0
- Make prerm and postinst fail on error
- Another header to explicitly #include in c++ (Closes: #504847)
- Add an section to the info file (Closes: debian #528885)

* Tue Aug 26 2008 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-8
- Suppression of the logging in the perl robot as it may lead to a
  security risk (Closes: debian #496385).

* Sun Apr 06 2008 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-7
- correction of a typo in build-indep dependency (closes: 473931)

* Sat Mar 22 2008 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-6
- When building binary-indep package, We need a java virtual machine
- (Closes: deb #471551).
- Use Vcs-* and not XS-Vcs-* in control

* Sat Mar 22 2008 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-5
- Don't try to build jBot when not building binary indep package

* Fri Feb 29 2008 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-4
- Going to Standards-Version: 3.7.3
- removing Uploader line
- Adding severall #include for gcc-4.3 (Closes: debian #455614).
- Removing warning about string constant
- Use M_PI in place of M_PIL (closes: #447700)
- Severall cleanup for lintian

* Wed Aug 08 2007 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-3
- I don't use dpatch anymore.
- Make realtimebattle binNMU safe thanks to Lior Kaplan (closes: 432994)
- adding XS-Vcs-Browser and XS-Vcs-git

* Fri Mar 17 2006 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-2
- Adding suggest on python for the python bot.
- Really applying patch for gcc 4.1 (closes: debian #356157, 357403)
- Changing config.guess and config.sub (closes: debian #342428)

* Fri Mar 10 2006 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.8-1
- New upstream release
- Adding manpage from cvs (closes: debian #110739)
- Applying patch for gcc 4.1 (closes: debian #356157)

* Wed Aug 10 2005 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.7+20050807-1
- New upstream release (cvs version)
- Remove circular dependency
- String and List are replaced by stl::string and stl::list
- (Closes: debian #302565).
- Bug fix: "realtimebattle: [INTL:de] German PO file corrections",
- thanks to Jens Seidel (Closes: debian #313822).
- Add Johannes Nicolai to the uploaders field.
- Change the standard version to 3.6.2
- Make doc-base happy with the name of the Info file
- Override menu-icon-missing as icon is in the common package

* Wed Mar 23 2005 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.7-5
- Move image out of /usr/lib
- Make RTB use the icon
- Correction of the menu entry
- use jikes and not gcj to compile the java files

* Thu Jan 20 2005 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.7-4
- The Team Framework now compile with gcc-3.4 thanks to upstream
- (closes: debian #274270)
- Split java bot and common file into realtimebattle-common
- Make jBot use the java alternative
- Correct the .robot scripts so they look at the correct place for
- their needed files
- Move rtb-team out of /usr/share

* Wed Dec 22 2004 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.7-3
- Added buildep on gcj for the java robot

* Wed Dec 22 2004 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.7-2
- solve info installation problem (closes: debian #86755)
- apply upstream patch for partial gcc-3.4 compilation
  (it still fail on Team Framework for now)

* Fri Dec 17 2004 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.7-1
- New upstream release

* Fri Jan 16 2004 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.6-3
- Add AM_MAINTAINER_MODE to configure.in

* Sat Jan 3 2004 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.6-2
- Don't use dh_installinfo, but directly install-info (closes: #225604).
- change name of RealTimeBattle.info.gz to realtimebattle.info.gz.

* Fri Dec 5 2003 RÃ©mi Vanicat <vanicat@debian.org> - 1.0.6-1
- New upstream release
- New debian Maintener (RÃ©mi Vanicat <vanicat@debian.org)
- Compile now with g++ 3.3 (closes: debian #134033, #192461)
- Acknowledge NMU from Matthias Klose <doko@debian.org> :
  (closes: debian #221274)

* Mon Nov 17 2003 Matthias Klose <doko@debian.org> - 1.0.5-5.1
- NMU.
- Build-Depend on gcc-2.95, gcc-2.96, do not build for hppa.
  Closes: debian #134033, #192461.
- Fix doc-base file (closes: debian #149545).
- Fix download location (closes: debian #208567).

* Fri Feb 15 2002 Fredrik Hallenberg <hallon@debian.org> - 1.0.5-5
- Fixed bad code that failed with g++3 (closes: debian #134033)

* Thu Sep 27 2001 Fredrik Hallenberg <hallon@debian.org> - 1.0.5-4
- Applied patch from John R. Daily <jdaily@progeny.com> to fix build failure
  on ia64 (closes: debian #113628)

* Sat Aug 25 2001 Fredrik Hallenberg <hallon@debian.org> - 1.0.5-3
- Rebuild to get rid of seg fault (closes: debian #108387)
- Updated po/Makefile.in.in
- Use section with install-info

* Fri Oct 6 2000 Fredrik Hallenberg <hallon@debian.org> - 1.0.5-2
- Updated doc-base file (closes: debian #58204, #74124)

* Sun Oct 1 2000 Fredrik Hallenberg <hallon@debian.org> - 1.0.5-1
- New upstream release

* Sun Feb 27 2000 Fredrik Hallenberg <hallon@debian.org> - 1.0.3-1
- New upstream release

* Mon Feb 7 2000 Fredrik Hallenberg <hallon@debian.org> - 1.0.2-1
- New upstream release

* Fri Jan 7 2000 Fredrik Hallenberg <hallon@debian.org> - 1.0.0-1
- New upstream release

* Mon Oct 25 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.11-2
- Fixed rotate_and_fire_select.cc so it compiles on glibc2.0 systems.
  (closes: debian #48280)

* Sun Oct 17 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.11-1
- New upstream release

* Sat Aug 21 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.10-1
- New upstream release.
- Use doc-base.

* Mon Aug 16 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.9-1
- New upstream release

* Sun Jul 18 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.8-1
- New upstream release

* Sat Apr 3 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.7-2
- Recompile with glibc 2.1 (deiban bug #35441)

* Mon Mar 8 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.7-1
- Added menuentry from Fredrik Liljegren <eof@hem.utfors.se>
- New upstream release

* Sat Feb 20 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.6-1
- New upstream release

* Mon Feb 8 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.5-2
- Fixed postinst and prerm.

* Sat Feb 6 1999 Fredrik Hallenberg <hallon@debian.org> - 0.9.5-1
- Initial release.

