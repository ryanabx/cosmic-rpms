# Generated by specgen.py ryanabx
%define debug_package %{nil}
# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-settings
%global repo https://github.com/pop-os/cosmic-settings

Name:           cosmic-settings
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        The settings application for the COSMIC desktop environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-settings

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
just build-vendored

%install
just rootdir=%{buildroot} install

%files

%{_bindir}/cosmic-settings
%{_datadir}/applications/com.system76.CosmicSettings.desktop

%{_datadir}/cosmic/com.system76.CosmicTheme.Dark.Builder/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Dark/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Light.Builder/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Light/v1/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Mode/v1/*
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-slightly-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-square.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-slightly-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-square.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-mode-dark.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-mode-light.svg


%changelog
%autochangelog
    