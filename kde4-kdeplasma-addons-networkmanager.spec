%define		snap	891984

Summary:	Plasma applet that controls network via NetworkManager backend
Name:		kde4-kdeplasma-addons-networkmanager
Version:	0
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Applications
# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/base/plasma/applets/networkmanager/
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	e9c66a8d882eb2b67b24f9bb004cdff9
BuildRequires:	NetworkManager-devel
BuildRequires:	cmake
BuildRequires:	kde4-kdebase-workspace-devel
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
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
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
%{_datadir}/apps/desktoptheme/default/networkmanager
%{_datadir}/apps/knetworkmanager
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
%attr(755,root,root) %{_libdir}/kde4/kcm_knetworkmanager.so
%attr(755,root,root) %{_libdir}/kde4/kded_knetworkmanager.so
%attr(755,root,root) %{_libdir}/kde4/knetworkmanager4_openvpnui.so
%attr(755,root,root) %{_libdir}/kde4/knetworkmanager4_vpncui.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_networkmanager.so
%attr(755,root,root) %{_libdir}/kde4/libexec/knetworkmanager_configshell