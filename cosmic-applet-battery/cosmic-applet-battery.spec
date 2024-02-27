# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-applet-battery
%global repo https://github.com/pop-os/cosmic-applets

Name:           cosmic-applet-battery
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        WIP battery applet for cosmic-panel

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-applets

Source:         %{crate}.tar.gz
Source:         vendor.tar



# For now, we require all deps for all of cosmic-epoch
BuildRequires:  make
BuildRequires:  which
BuildRequires:  just
BuildRequires:  rustc
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libxkbcommon)
BuildRequires:  lld
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(glib2)
BuildRequires:  pkgconfig(gtk3)
BuildRequires:  pkgconfig(dbus)
BuildRequires:  pkgconfig(wayland)
BuildRequires:  pkgconfig(clang)
BuildRequires:  cargo
BuildRequires:  pkgconfig(mesa-libgbm)
BuildRequires:  pkgconfig(pipewire)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(rust-rav1e+nasm-rs)
BuildRequires:  libappstream-glib



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

just vendor=1 _extract_vendor
cargo build --frozen --offline --release --bin cosmic-applet-battery


%install
just rootdir=%{buildroot} prefix=%{_prefix} _install_battery

%files

%{_bindir}/cosmic-applet-battery
%{_datadir}/applications/com.system76.CosmicAppletBattery.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletBattery.svg

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


%changelog
%autochangelog
    