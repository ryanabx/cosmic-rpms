# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-applets
%global repo https://github.com/pop-os/cosmic-applets

Name:           cosmic-applets
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        WIP applets for cosmic-panel

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-applets

Source:         %{crate}.tar.gz
Source:         vendor.tar



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

%autosetup -n %{crate} -p1
mv %{_sourcedir}/vendor.tar vendor.tar
ls -a
mkdir -p .cargo
cp .vendor/config.toml .cargo/config.toml


%build

export CARGO_BUILD_JOBS=2
just vendor=1 build


%install
just rootdir=%{buildroot} prefix=%{_prefix} install

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

%{_bindir}/cosmic-applet-status-area
%{_datadir}/applications/com.system76.CosmicAppletStatusArea.desktop

%{_bindir}/cosmic-applet-workspaces
%{_datadir}/applications/com.system76.CosmicAppletWorkspaces.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletWorkspaces.svg

%{_bindir}/cosmic-panel-button
%{_prefix}/lib/debug/usr/bin/cosmic-panel-button-0.1.0~20240226.a6494e-1.fc40.x86_64.debug
%{_datadir}/applications/com.system76.CosmicPanelAppButton.desktop
%{_datadir}/applications/com.system76.CosmicPanelWorkspacesButton.desktop
%{_datadir}/icons/hicolor/scalable/app/com.system76.CosmicAppletStatusArea.svg
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletTiling.Off.svg
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletTiling.On.svg
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicPanelAppButton.svg
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicPanelWorkspacesButton.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-display-brightness-high-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-display-brightness-low-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-display-brightness-medium-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-display-brightness-off-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-0-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-0-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-0-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-0-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-10-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-10-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-10-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-10-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-100-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-100-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-20-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-20-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-20-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-20-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-35-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-35-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-35-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-35-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-5-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-5-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-5-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-5-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-50-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-50-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-50-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-50-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-65-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-65-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-65-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-65-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-80-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-80-limited-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-80-limited-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-80-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-90-charging-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-level-90-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-bluetooth-active-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-bluetooth-disabled-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-notification-disabled-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-notification-new-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-notification-symbolic.svg


%changelog
%autochangelog
    