# Generated by specgen.py ryanabx

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
ls -a
mkdir -p .cargo
cp .vendor/config.toml .cargo/config.toml


%build

cargo build --all -r


%install

install -Dm0755 target/release/cosmic-settings %{buildroot}/%{_bindir}/cosmic-settings
install -Dm0644 resources/com.system76.CosmicSettings.desktop %{buildroot}/%{_datadir}/applications/com.system76.CosmicSettings.desktop

find 'resources'/'default_schema' -type f -exec echo {} \; | rev | cut -d'/' -f-3 | rev | xargs -d '\n' -I {} install -Dm0644 'resources'/'default_schema'/{} '%{_datadir}'/'cosmic'/{}
find 'resources'/'icons' -type f -exec echo {} \; | rev | cut -d'/' -f-3 | rev | xargs -d '\n' -I {} install -Dm0644 'resources'/'icons'/{} {{iconsdir}}/{}



%files




%{_bindir}/cosmic-settings
%{_datadir}/applications/com.system76.CosmicSettings.desktop

%{_datadir}/cosmic/com.system76.CosmicTheme.Dark.Builder/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Dark/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Light.Builder/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Light/*
%{_datadir}/cosmic/com.system76.CosmicTheme.Mode/*
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
    