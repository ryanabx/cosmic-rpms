# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-greeter
%global repo https://github.com/pop-os/cosmic-greeter

Name:           cosmic-greeter
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Libcosmic greeter for greetd, which can be run inside cosmic-comp

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-greeter

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

install -Dm0644 target/release/cosmic-greeter %{_bindir}/cosmic-greeter

install -Dm0644 target/release/cosmic-greeter-daemon %{_bindir}/cosmic-greeter-daemon

install -Dm0644 debian/cosmic-greeter.sysusers %{_prefix}/lib/sysusers.d/cosmic-greeter.conf
install -Dm0644 debian/cosmic-greeter.tmpfiles %{_prefix}/lib/tmpfiles.d/cosmic-greeter.conf
install -Dm0644 dbus/com.system76.CosmicGreeter.conf %{_datadir}/dbus-1/system.d/com.system76.CosmicGreeter.conf


%files




%{_bindir}/cosmic-greeter

%{_bindir}/cosmic-greeter-daemon

%{_prefix}/lib/sysusers.d/cosmic-greeter.conf
%{_prefix}/lib/tmpfiles.d/cosmic-greeter.conf
%{_datadir}/dbus-1/system.d/com.system76.CosmicGreeter.conf


%changelog
%autochangelog
    