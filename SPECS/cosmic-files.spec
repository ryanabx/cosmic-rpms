# Generated by specgen.py ryanabx

# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate cosmic-files
%global repo https://github.com/pop-os/cosmic-files

Name:           cosmic-files
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        File browser built using libcosmic for the COSMIC Desktop Environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-files

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
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}


%install

install -Dm0644 target/release/cosmic-files %{_bindir}/cosmic-files
install -Dm0644 /data/com.system76.CosmicFiles.desktop %{_datadir}/applications/com.system76.CosmicFiles.desktop



%files

%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md


%{_bindir}/cosmic-files
%{_datadir}/applications/com.system76.CosmicFiles.desktop



%changelog
%autochangelog
    