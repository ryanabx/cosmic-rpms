# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-randr
%global repo https://github.com/pop-os/cosmic-randr

Name:           cosmic-randr
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Library and utility for displaying and configuring Wayland outputs

License:        MPL-2.0

URL:            https://github.com/pop-os/cosmic-randr

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

install -Dm0755 target/release/cosmic-randr %{buildroot}/%{_bindir}/cosmic-randr



%files




%{_bindir}/cosmic-randr



%changelog
%autochangelog
    