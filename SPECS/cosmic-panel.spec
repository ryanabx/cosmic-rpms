# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-panel
%global repo https://github.com/pop-os/cosmic-panel

Name:           cosmic-panel
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Panel for COSMIC Desktop Environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-panel

Source:         %{crate}.tar.gz
Source:         %vendor.tar.xz



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
mv ../vendor.tar.xz vendor.tar.xz
ls -a
mkdir -p .cargo
cp .vendor/config.toml .cargo/config.toml


%build
just build-vendored

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files




%{_bindir}/cosmic-panel

%{_datadir}/cosmic/com.system76.CosmicPanel.Dock/*
%{_datadir}/cosmic/com.system76.CosmicPanel.Panel/*
%{_datadir}/cosmic/com.system76.CosmicPanel/*


%changelog
%autochangelog
    