# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-applet-panel-button
%global repo https://github.com/pop-os/cosmic-applets

Name:           cosmic-applet-panel-button
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        WIP panel button applet for cosmic-panel

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

%debug_package

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
cargo build --frozen --offline --release --bin cosmic-panel-button


%install

just rootdir=%{buildroot} prefix=%{_prefix} _install_panel_button
just rootdir=%{buildroot} prefix=%{_prefix} _install_app_button
just rootdir=%{buildroot} prefix=%{_prefix} _install_workspaces_button


%files

%{_bindir}/cosmic-panel-button
%{_datadir}/applications/com.system76.CosmicPanelAppButton.desktop
%{_datadir}/applications/com.system76.CosmicPanelWorkspacesButton.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicPanelAppButton.svg
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicPanelWorkspacesButton.svg


%changelog
%autochangelog
    