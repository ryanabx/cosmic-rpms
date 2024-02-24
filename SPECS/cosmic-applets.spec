# Generated by specgen.py ryanabx

# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate cosmic-applets
%global repo https://github.com/pop-os/cosmic-applets

Name:           cosmic-applets
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        WIP applets for cosmic-panel

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-applets

Source:         %{crate}.tar.gz
Source:         %{crate}-vendor.tar.xz



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
mkdir .cargo
cp .vendor/config.toml .cargo/config.toml


%build

cargo build --bin cosmic-app-list
cargo build --bin cosmic-applet-audio
cargo build --bin cosmic-applet-battery
cargo build --bin cosmic-applet-bluetooth
cargo build --bin cosmic-applet-graphics
cargo build --bin cosmic-applet-network
cargo build --bin cosmic-applet-notifications
cargo build --bin cosmic-applet-power
cargo build --bin cosmic-applet-time
cargo build --bin cosmic-applet-tiling
cargo build --bin cosmic-applet-status-area
cargo build --bin cosmic-applet-workspaces
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}


%install

install -Dm0644 target/release/cosmic-app-list %{_bindir}/cosmic-app-list
install -Dm0644 cosmic-app-list/data/com.system76.CosmicAppList.desktop %{_datadir}/applications/com.system76.CosmicAppList.desktop
install -Dm0644 cosmic-app-list/data/icons/com.system76.CosmicAppList.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppList.svg

install -Dm0644 target/release/cosmic-applet-audio %{_bindir}/cosmic-applet-audio
install -Dm0644 cosmic-applet-audio/data/com.system76.CosmicAppletAudio.desktop %{_datadir}/applications/com.system76.CosmicAppletAudio.desktop
install -Dm0644 cosmic-applet-audio/data/icons/com.system76.CosmicAppletAudio.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletAudio.svg

install -Dm0644 target/release/cosmic-applet-battery %{_bindir}/cosmic-applet-battery
install -Dm0644 cosmic-applet-battery/data/com.system76.CosmicAppletBattery.desktop %{_datadir}/applications/com.system76.CosmicAppletBattery.desktop
install -Dm0644 cosmic-applet-battery/data/icons/com.system76.CosmicAppletBattery.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletBattery.svg

install -Dm0644 target/release/cosmic-applet-bluetooth %{_bindir}/cosmic-applet-bluetooth
install -Dm0644 cosmic-applet-bluetooth/data/com.system76.CosmicAppletBluetooth.desktop %{_datadir}/applications/com.system76.CosmicAppletBluetooth.desktop
install -Dm0644 cosmic-applet-bluetooth/data/icons/com.system76.CosmicAppletBluetooth.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletBluetooth.svg

install -Dm0644 target/release/cosmic-applet-graphics %{_bindir}/cosmic-applet-graphics
install -Dm0644 cosmic-applet-graphics/data/com.system76.CosmicAppletGraphics.desktop %{_datadir}/applications/com.system76.CosmicAppletGraphics.desktop
install -Dm0644 cosmic-applet-graphics/data/icons/com.system76.CosmicAppletGraphics.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletGraphics.svg

install -Dm0644 target/release/cosmic-applet-network %{_bindir}/cosmic-applet-network
install -Dm0644 cosmic-applet-network/data/com.system76.CosmicAppletNetwork.desktop %{_datadir}/applications/com.system76.CosmicAppletNetwork.desktop
install -Dm0644 cosmic-applet-network/data/icons/com.system76.CosmicAppletNetwork.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletNetwork.svg

install -Dm0644 target/release/cosmic-applet-notifications %{_bindir}/cosmic-applet-notifications
install -Dm0644 cosmic-applet-notifications/data/com.system76.CosmicAppletNotifications.desktop %{_datadir}/applications/com.system76.CosmicAppletNotifications.desktop
install -Dm0644 cosmic-applet-notifications/data/icons/com.system76.CosmicAppletNotifications.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletNotifications.svg

install -Dm0644 target/release/cosmic-applet-power %{_bindir}/cosmic-applet-power
install -Dm0644 cosmic-applet-power/data/com.system76.CosmicAppletPower.desktop %{_datadir}/applications/com.system76.CosmicAppletPower.desktop
install -Dm0644 cosmic-applet-power/data/icons/com.system76.CosmicAppletPower.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletPower.svg

install -Dm0644 target/release/cosmic-applet-time %{_bindir}/cosmic-applet-time
install -Dm0644 cosmic-applet-time/data/com.system76.CosmicAppletTime.desktop %{_datadir}/applications/com.system76.CosmicAppletTime.desktop
install -Dm0644 cosmic-applet-time/data/icons/com.system76.CosmicAppletTime.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletTime.svg

install -Dm0644 target/release/cosmic-applet-tiling %{_bindir}/cosmic-applet-tiling
install -Dm0644 cosmic-applet-tiling/data/com.system76.CosmicAppletTiling.desktop %{_datadir}/applications/com.system76.CosmicAppletTiling.desktop
install -Dm0644 cosmic-applet-tiling/data/icons/com.system76.CosmicAppletTiling.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletTiling.svg

install -Dm0644 target/release/cosmic-applet-status-area %{_bindir}/cosmic-applet-status-area
install -Dm0644 cosmic-applet-status-area/data/com.system76.CosmicAppletStatusArea.desktop %{_datadir}/applications/com.system76.CosmicAppletStatusArea.desktop
install -Dm0644 cosmic-applet-status-area/data/icons/com.system76.CosmicAppletStatusArea.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletStatusArea.svg

install -Dm0644 target/release/cosmic-applet-workspaces %{_bindir}/cosmic-applet-workspaces
install -Dm0644 cosmic-applet-workspaces/data/com.system76.CosmicAppletWorkspaces.desktop %{_datadir}/applications/com.system76.CosmicAppletWorkspaces.desktop
install -Dm0644 cosmic-applet-workspaces/data/icons/com.system76.CosmicAppletWorkspaces.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletWorkspaces.svg



%files




%{_bindir}/cosmic-app-list
%{_datadir}/applications/com.system76.CosmicAppList.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppList.svg

%{_bindir}/cosmic-applet-audio
%{_datadir}/applications/com.system76.CosmicAppletAudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletAudio.svg

%{_bindir}/cosmic-applet-battery
%{_datadir}/applications/com.system76.CosmicAppletBattery.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletBattery.svg

%{_bindir}/cosmic-applet-bluetooth
%{_datadir}/applications/com.system76.CosmicAppletBluetooth.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletBluetooth.svg

%{_bindir}/cosmic-applet-graphics
%{_datadir}/applications/com.system76.CosmicAppletGraphics.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletGraphics.svg

%{_bindir}/cosmic-applet-network
%{_datadir}/applications/com.system76.CosmicAppletNetwork.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletNetwork.svg

%{_bindir}/cosmic-applet-notifications
%{_datadir}/applications/com.system76.CosmicAppletNotifications.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletNotifications.svg

%{_bindir}/cosmic-applet-power
%{_datadir}/applications/com.system76.CosmicAppletPower.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletPower.svg

%{_bindir}/cosmic-applet-time
%{_datadir}/applications/com.system76.CosmicAppletTime.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletTime.svg

%{_bindir}/cosmic-applet-tiling
%{_datadir}/applications/com.system76.CosmicAppletTiling.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletTiling.svg

%{_bindir}/cosmic-applet-status-area
%{_datadir}/applications/com.system76.CosmicAppletStatusArea.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletStatusArea.svg

%{_bindir}/cosmic-applet-workspaces
%{_datadir}/applications/com.system76.CosmicAppletWorkspaces.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletWorkspaces.svg



%changelog
%autochangelog
    