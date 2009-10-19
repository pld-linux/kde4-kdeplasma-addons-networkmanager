# Conditional build:
%bcond_with	verbose		# verbose build

%define		snap	970120
%define		qtver	4.5.0

Summary:	Plasma applet that controls network via NetworkManager backend
Name:		kde4-kdeplasma-addons-networkmanager
Version:	4.2.3
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Applications
# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/base/plasma/applets/networkmanager/
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	597aa8a8b1002d18cfe5504c4c3fe5d1
BuildRequires:	NetworkManager-devel >= 0.7.0
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma applet that controls network via NetworkManager backend.

%prep
%setup -q -n %{name}-%{snap}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	%{?with_verbose:-DCMAKE_VERBOSE_MAKEFILE=true} \
	-DDBUS_SYSTEM_POLICY_DIR=/etc/dbus-1/system.d \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DESIGN TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*.conf
%{_datadir}/apps/desktoptheme/default/networkmanagement
%{_datadir}/apps/networkmanagement
%{_iconsdir}/oxygen/32x32/actions/accesspoint.png
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/kded/*.desktop
%{_datadir}/kde4/servicetypes/*.desktop
%attr(755,root,root) %{_libdir}/libknmdbus.so
%attr(755,root,root) %{_libdir}/libknmdbus.so.4
%attr(755,root,root) %{_libdir}/libknmdbus.so.4.2.0
%attr(755,root,root) %{_libdir}/libknmstorage.so
%attr(755,root,root) %{_libdir}/libknmstorage.so.4
%attr(755,root,root) %{_libdir}/libknmstorage.so.4.2.0
%attr(755,root,root) %{_libdir}/libknmui.so
%attr(755,root,root) %{_libdir}/libknmui.so.4
%attr(755,root,root) %{_libdir}/libknmui.so.4.2.0
%attr(755,root,root) %{_libdir}/kde4/kcm_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/kded_knetworkmanager.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_openvpnui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_vpncui.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/libexec/networkmanagement_configshell
