%global appid_app_list com.system76.CosmicAppList
%global appid_audio com.system76.CosmicAppletAudio
%global appid_battery com.system76.CosmicAppletBattery
%global appid_bluetooth com.system76.CosmicAppletBluetooth
%global appid_graphics com.system76.CosmicAppletGraphics
%global appid_network com.system76.CosmicAppletNetwork
%global appid_notifications com.system76.CosmicAppletNotifications
%global appid_power com.system76.CosmicAppletPower
%global appid_time com.system76.CosmicAppletTime
%global appid_tiling com.system76.CosmicAppletTiling
%global appid_status_area com.system76.CosmicAppletStatusArea
%global appid_workspaces com.system76.CosmicAppletWorkspaces

%global commit e214e9867876c96b24568d8a45aaca2936269d9b

%global appid com.system76.CosmicApplets

# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate cosmic-applets
%global repo cosmic-applets

Name:           cosmic-applets
Version:        0.1.0

Release:        %autorelease
Summary:        WIP applets for cosmic-panel

SourceLicense:  None
# FIXME: paste output of %%cargo_license_summary here
License:        GPL-3.0
# LICENSE.dependencies contains a full license breakdown
# FIXME: No license information in crate metadata.

URL:            https://github.com/pop-os/%{repo}
Source:         %{crate}.tar.gz
Source:         %{crate}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 26.1

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

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{crate} -p1 -a1
# %cargo_prep -N
cat .vendor/config.toml >> .cargo/config

%build
# %cargo_build
cargo build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
# %cargo_install
install -Dm0644 target/release/cosmic-app-list %{_bindir}/cosmic-app-list
install -Dm0644 target/release/cosmic-applet-audio %{_bindir}/cosmic-applet-audio
install -Dm0644 target/release/cosmic-applet-battery %{_bindir}/cosmic-applet-battery
install -Dm0644 target/release/cosmic-applet-bluetooth %{_bindir}/cosmic-applet-bluetooth
install -Dm0644 target/release/cosmic-applet-graphics %{_bindir}/cosmic-applet-graphics
install -Dm0644 target/release/cosmic-applet-network %{_bindir}/cosmic-applet-network
install -Dm0644 target/release/cosmic-applet-notifications %{_bindir}/cosmic-applet-notifications
install -Dm0644 target/release/cosmic-applet-power %{_bindir}/cosmic-applet-power
install -Dm0644 target/release/cosmic-applet-time %{_bindir}/cosmic-applet-time
install -Dm0644 target/release/cosmic-applet-tiling %{_bindir}/cosmic-applet-tiling
install -Dm0644 target/release/cosmic-applet-status-area %{_bindir}/cosmic-applet-status-area
install -Dm0644 target/release/cosmic-applet-workspaces %{_bindir}/cosmic-applet-workspaces

install -Dm0644 cosmic-app-list/data/%{appid_app_list}.desktop %{_datadir}/applications/%{appid_app_list}.desktop
install -Dm0644 cosmic-app-list/data/icons/%{appid_app_list}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_app_list}.svg
# install -Dm0644 cosmic-app-list/data/ %{_datadir}/metainfo/%{appid_app_list}.metainfo.xml
install -Dm0644 cosmic-applet-audio/data/%{appid_audio}.desktop %{_datadir}/applications/%{appid_audio}.desktop
install -Dm0644 cosmic-applet-audio/data/icons/%{appid_audio}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_audio}.svg
# install -Dm0644 cosmic-applet-audio/data/ %{_datadir}/metainfo/%{appid_audio}.metainfo.xml
install -Dm0644 cosmic-applet-battery/data/%{appid_battery}.desktop %{_datadir}/applications/%{appid_battery}.desktop
install -Dm0644 cosmic-applet-battery/data/icons/%{appid_battery}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_battery}.svg
# install -Dm0644 cosmic-applet-battery/data/ %{_datadir}/metainfo/%{appid_battery}.metainfo.xml
install -Dm0644 cosmic-applet-bluetooth/data/%{appid_bluetooth}.desktop %{_datadir}/applications/%{appid_bluetooth}.desktop
install -Dm0644 cosmic-applet-bluetooth/data/icons/%{appid_bluetooth}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_bluetooth}.svg
# install -Dm0644 cosmic-applet-bluetooth/data/ %{_datadir}/metainfo/%{appid_bluetooth}.metainfo.xml
install -Dm0644 cosmic-applet-graphics/data/%{appid_graphics}.desktop %{_datadir}/applications/%{appid_graphics}.desktop
install -Dm0644 cosmic-applet-graphics/data/icons/%{appid_graphics}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_graphics}.svg
# install -Dm0644 cosmic-applet-graphics/data/ %{_datadir}/metainfo/%{appid_graphics}.metainfo.xml
install -Dm0644 cosmic-applet-network/data/%{appid_network}.desktop %{_datadir}/applications/%{appid_network}.desktop
install -Dm0644 cosmic-applet-network/data/icons/%{appid_network}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_network}.svg
# install -Dm0644 cosmic-applet-network/data/ %{_datadir}/metainfo/%{appid_network}.metainfo.xml
install -Dm0644 cosmic-applet-notifications/data/%{appid_notifications}.desktop %{_datadir}/applications/%{appid_notifications}.desktop
install -Dm0644 cosmic-applet-notifications/data/icons/%{appid_notifications}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_notifications}.svg
# install -Dm0644 cosmic-applet-notifications/data/ %{_datadir}/metainfo/%{appid_notifications}.metainfo.xml
install -Dm0644 cosmic-applet-power/data/%{appid_power}.desktop %{_datadir}/applications/%{appid_power}.desktop
install -Dm0644 cosmic-applet-power/data/icons/%{appid_power}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_power}.svg
# install -Dm0644 cosmic-applet-power/data/ %{_datadir}/metainfo/%{appid_power}.metainfo.xml
install -Dm0644 cosmic-applet-time/data/%{appid_time}.desktop %{_datadir}/applications/%{appid_time}.desktop
install -Dm0644 cosmic-applet-time/data/icons/%{appid_time}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_time}.svg
# install -Dm0644 cosmic-applet-time/data/ %{_datadir}/metainfo/%{appid_time}.metainfo.xml
install -Dm0644 cosmic-applet-tiling/data/%{appid_tiling}.desktop %{_datadir}/applications/%{appid_tiling}.desktop
install -Dm0644 cosmic-applet-tiling/data/icons/%{appid_tiling}.On.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_tiling}.On.svg
install -Dm0644 cosmic-applet-tiling/data/icons/%{appid_tiling}.Off.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_tiling}.Off.svg
# install -Dm0644 cosmic-applet-tiling/data/ %{_datadir}/metainfo/%{appid_tiling}.metainfo.xml
install -Dm0644 cosmic-applet-status-area/data/%{appid_status_area}.desktop %{_datadir}/applications/%{appid_status_area}.desktop
install -Dm0644 cosmic-applet-status-area/data/icons/%{appid_status_area}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_status_area}.svg
# install -Dm0644 cosmic-applet-status-area/data/ %{_datadir}/metainfo/%{appid_status_area}.metainfo.xml
install -Dm0644 cosmic-applet-workspaces/data/%{appid_workspaces}.desktop %{_datadir}/applications/%{appid_workspaces}.desktop
install -Dm0644 cosmic-applet-workspaces/data/icons/%{appid_workspaces}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid_workspaces}.svg
# install -Dm0644 cosmic-applet-workspaces/data/ %{_datadir}/metainfo/%{appid_workspaces}.metainfo.xml

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
# Binaries
%{_bindir}/cosmic-app-list
%{_bindir}/cosmic-applet-audio
%{_bindir}/cosmic-applet-battery
%{_bindir}/cosmic-applet-bluetooth
%{_bindir}/cosmic-applet-graphics
%{_bindir}/cosmic-applet-network
%{_bindir}/cosmic-applet-notifications
%{_bindir}/cosmic-applet-power
%{_bindir}/cosmic-applet-time
%{_bindir}/cosmic-applet-tiling
%{_bindir}/cosmic-applet-status-area
%{_bindir}/cosmic-applet-workspaces
# Icons
%{_datadir}/applications/%{appid_app_list}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_app_list}.svg
# %{_datadir}/metainfo/%{appid_app_list}.metainfo.xml
%{_datadir}/applications/%{appid_audio}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_audio}.svg
# %{_datadir}/metainfo/%{appid_audio}.metainfo.xml
%{_datadir}/applications/%{appid_battery}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_battery}.svg
# %{_datadir}/metainfo/%{appid_battery}.metainfo.xml
%{_datadir}/applications/%{appid_bluetooth}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_bluetooth}.svg
# %{_datadir}/metainfo/%{appid_bluetooth}.metainfo.xml
%{_datadir}/applications/%{appid_graphics}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_graphics}.svg
# %{_datadir}/metainfo/%{appid_graphics}.metainfo.xml
%{_datadir}/applications/%{appid_network}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_network}.svg
# %{_datadir}/metainfo/%{appid_network}.metainfo.xml
%{_datadir}/applications/%{appid_notifications}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_notifications}.svg
# %{_datadir}/metainfo/%{appid_notifications}.metainfo.xml
%{_datadir}/applications/%{appid_power}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_power}.svg
# %{_datadir}/metainfo/%{appid_power}.metainfo.xml
%{_datadir}/applications/%{appid_time}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_time}.svg
# %{_datadir}/metainfo/%{appid_time}.metainfo.xml
%{_datadir}/applications/%{appid_tiling}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_tiling}.On.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid_tiling}.Off.svg
# %{_datadir}/metainfo/%{appid_tiling}.metainfo.xml
%{_datadir}/applications/%{appid_status_area}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_status_area}.svg
# %{_datadir}/metainfo/%{appid_status_area}.metainfo.xml
%{_datadir}/applications/%{appid_workspaces}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid_workspaces}.svg
# %{_datadir}/metainfo/%{appid_workspaces}.metainfo.xml

%changelog
%autochangelog
