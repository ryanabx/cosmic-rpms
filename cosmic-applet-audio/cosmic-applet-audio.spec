# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-applet-audio
%global repo https://github.com/pop-os/cosmic-applets

Name:           cosmic-applet-audio
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        WIP audio applet for cosmic-panel

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
cargo build --frozen --offline --release --bin cosmic-applet-audio


%install
just rootdir=%{buildroot} prefix=%{_prefix} _install_audio

%files

%{_bindir}/cosmic-applet-audio
%{_datadir}/applications/com.system76.CosmicAppletAudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletAudio.svg



%changelog
%autochangelog
    