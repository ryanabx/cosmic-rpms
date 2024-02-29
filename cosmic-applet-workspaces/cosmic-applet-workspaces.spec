# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-applet-workspaces
%global repo https://github.com/pop-os/cosmic-applets

Name:           cosmic-applet-workspaces
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        WIP workspaces applet for cosmic-panel

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-applets

Source:         %{crate}.tar.gz
Source:         vendor.tar



# For now, we require all deps for all of cosmic-epoch
BuildRequires:  make
BuildRequires:  which
BuildRequires:  git
BuildRequires:  just
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  dbus-devel
BuildRequires:  wayland-devel
BuildRequires:  clang-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  rust-rav1e+nasm-rs-devel
BuildRequires:  libappstream-glib
BuildRequires:  pipewire-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libseat-devel
BuildRequires:  libinput-devel
BuildRequires:  pam-devel
BuildRequires:  flatpak-devel



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
cargo build --frozen --offline --release --bin cosmic-applet-workspaces


%install
just rootdir=%{buildroot} prefix=%{_prefix} _install_workspace

%files

%{_bindir}/cosmic-applet-workspaces
%{_datadir}/applications/com.system76.CosmicAppletWorkspaces.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletWorkspaces.svg



%changelog
%autochangelog
    