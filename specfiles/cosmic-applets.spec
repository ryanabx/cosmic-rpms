# Cosmic App List
%global idapplist com.system76.CosmicAppList
%global binapplist cosmic-app-list
# Cosmic Applet Audio
%global idaudio com.system76.CosmicAppletAudio
%global binaudio cosmic-applet-audio
# Cosmic Applet Battery
%global idbattery com.system76.CosmicAppletBattery
%global binbattery cosmic-applet-battery
# Cosmic Applet Bluetooth
%global idbluetooth com.system76.CosmicAppletBluetooth
%global binbluetooth cosmic-applet-bluetooth
# Cosmic Applet Graphics
%global idgraphics com.system76.CosmicAppletGraphics
%global bingraphics cosmic-applet-graphics
# Cosmic Applet Network
%global idnetwork com.system76.CosmicAppletNetwork
%global binnetwork cosmic-applet-network
# Cosmic Applet Notifications
%global idnotifications com.system76.CosmicAppletNotifications
%global binnotifications cosmic-applet-notifications
# Cosmic Applet Power
%global idpower com.system76.CosmicAppletPower
%global binpower cosmic-applet-power
# Cosmic Applet Workspaces
%global idworkspaces com.system76.CosmicAppletWorkspaces
%global binworkspaces cosmic-applet-workspaces
# Cosmic Applet Time
%global idtime com.system76.CosmicAppletTime
%global bintime cosmic-applet-time
# Cosmic Applet Tiling
%global idtiling com.system76.CosmicAppletTiling
%global bintiling cosmic-applet-tiling
# Cosmic Applet Status Area
%global idstatusarea com.system76.CosmicAppletStatusArea
%global binstatusarea cosmic-applet-status-area

%global commit 286fab4f19b3c73e0bacc48318df901336860196
Name:           cosmic-applets
Version:        0.1.0~20240221.286fab
Release:        %autorelease
Summary:        Applets for COSMIC Panel

License:        GPL-3.0
URL:            https://github.com/pop-os/%{name}
Source0:        https://github.com/pop-os/%{name}/archive/%{commit}.tar.gz

# For now, we require all deps for all of cosmic-epoch
BuildRequires:  make
BuildRequires:  which
BuildRequires:  just
BuildRequires:  rustc
BuildRequires:  libglvnd-devel
BuildRequires:  libseat-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  lld
BuildRequires:  libinput-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  dbus-devel
BuildRequires:  wayland-devel
BuildRequires:  clang-devel
BuildRequires:  cargo
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pipewire-devel
BuildRequires:  pam-devel
BuildRequires:  flatpak-devel
BuildRequires:  rust-rav1e+nasm-rs-devel

# For now, we require all deps for all of cosmic-epoch
Requires:       libseat
Requires:       pop-icon-theme
Requires:       greetd
Requires:       greetd-selinux
Requires:       cage
Requires:       mozilla-fira-mono-fonts
Requires:       mozilla-fira-sans-fonts

%description
Applets for COSMIC Panel

%prep
%autosetup

%build
just build-release
# just build-release --bin cosmic-app-list
# just build-release --bin cosmic-applet-audio
# just build-release --bin cosmic-applet-battery
# just build-release --bin cosmic-applet-bluetooth
# just build-release --bin cosmic-applet-graphics
# just build-release --bin cosmic-applet-network
# just build-release --bin cosmic-applet-notifications
# just build-release --bin cosmic-applet-power
# just build-release --bin cosmic-applet-status-area
# just build-release --bin cosmic-applet-tiling
# just build-release --bin cosmic-applet-time
# just build-release --bin cosmic-applet-workspaces
# just build-release --bin cosmic-panel-button

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
# applist
%{_bindir}/%{binapplist}
%{_datadir}/applications/%{idapplist}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idapplist}.svg
%{_datadir}/metainfo/%{idapplist}.metainfo.xml
# audio
%{_bindir}/%{binaudio}
%{_datadir}/applications/%{idaudio}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idaudio}.svg
%{_datadir}/metainfo/%{idaudio}.metainfo.xml
# battery
%{_bindir}/%{binbattery}
%{_datadir}/applications/%{idbattery}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idbattery}.svg
%{_datadir}/metainfo/%{idbattery}.metainfo.xml
# bluetooth
%{_bindir}/%{binbluetooth}
%{_datadir}/applications/%{idbluetooth}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idbluetooth}.svg
%{_datadir}/metainfo/%{idbluetooth}.metainfo.xml
# graphics
%{_bindir}/%{bingraphics}
%{_datadir}/applications/%{idgraphics}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idgraphics}.svg
%{_datadir}/metainfo/%{idgraphics}.metainfo.xml
# network
%{_bindir}/%{binnetwork}
%{_datadir}/applications/%{idnetwork}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idnetwork}.svg
%{_datadir}/metainfo/%{idnetwork}.metainfo.xml
# notifications
%{_bindir}/%{binnotifications}
%{_datadir}/applications/%{idnotifications}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idnotifications}.svg
%{_datadir}/metainfo/%{idnotifications}.metainfo.xml
# power
%{_bindir}/%{binpower}
%{_datadir}/applications/%{idpower}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idpower}.svg
%{_datadir}/metainfo/%{idpower}.metainfo.xml
# workspaces
%{_bindir}/%{binworkspaces}
%{_datadir}/applications/%{idworkspaces}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idworkspaces}.svg
%{_datadir}/metainfo/%{idworkspaces}.metainfo.xml
# time
%{_bindir}/%{bintime}
%{_datadir}/applications/%{idtime}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idtime}.svg
%{_datadir}/metainfo/%{idtime}.metainfo.xml
# tiling
%{_bindir}/%{bintiling}
%{_datadir}/applications/%{idtiling}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idtiling}.svg
%{_datadir}/metainfo/%{idtiling}.metainfo.xml
# statusarea
%{_bindir}/%{binstatusarea}
%{_datadir}/applications/%{idstatusarea}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{idstatusarea}.svg
%{_datadir}/metainfo/%{idstatusarea}.metainfo.xml

%changelog
* Tue Feb 20 2024 Ryan Brue <ryanbrue@hotmail.com>
- Created package
