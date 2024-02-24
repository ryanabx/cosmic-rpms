# Generated by specgen.py ryanabx

# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate cosmic-bg
%global repo https://github.com/pop-os/cosmic-bg

Name:           cosmic-bg
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        COSMIC session service which applies backgrounds to displays

License:        MPL-2.0

URL:            https://github.com/pop-os/cosmic-bg

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

install -Dm0644 target/release/cosmic-bg %{_bindir}/cosmic-bg
install -Dm0644 /data/com.system76.CosmicBackground.desktop %{_datadir}/applications/com.system76.CosmicBackground.desktop
install -Dm0644 /data/icons/com.system76.CosmicBackground.svg %{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicBackground.svg
install -Dm0644 /data/icons/com.system76.CosmicBackground-symbolic.svg %{_datadir}/icons/hicolor/symbolic/apps/%com.system76.CosmicBackground-symbolic.svg
install -Dm0644 /data/com.system76.CosmicBackground.metainfo.xml %{_datadir}/metainfo/com.system76.CosmicBackground.metainfo.xml



%files




%{_bindir}/cosmic-bg
%{_datadir}/applications/com.system76.CosmicBackground.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicBackground.svg
%{_datadir}/icons/hicolor/symbolic/apps/%com.system76.CosmicBackground-symbolic.svg
%{_datadir}/metainfo/com.system76.CosmicBackground.metainfo.xml

%{_datadir}/cosmic/com.system76.CosmicBackground/*


%changelog
%autochangelog
    