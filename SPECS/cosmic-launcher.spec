# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-launcher
%global repo https://github.com/pop-os/cosmic-launcher

Name:           cosmic-launcher
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Layer shell frontend for Pop Launcher

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-launcher

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

cargo build


%install

install -Dm0644 target/release/cosmic-launcher %{_bindir}/cosmic-launcher
install -Dm0644 /data/com.system76.CosmicLauncher.desktop %{_datadir}/applications/com.system76.CosmicLauncher.desktop
install -Dm0644 /data/icons/com.system76.CosmicLauncher.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicLauncher.svg
install -Dm0644 /data/com.system76.CosmicLauncher.metainfo.xml %{_datadir}/metainfo/com.system76.CosmicLauncher.metainfo.xml



%files




%{_bindir}/cosmic-launcher
%{_datadir}/applications/com.system76.CosmicLauncher.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicLauncher.svg
%{_datadir}/metainfo/com.system76.CosmicLauncher.metainfo.xml



%changelog
%autochangelog
    