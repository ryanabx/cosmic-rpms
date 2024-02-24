# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-session
%global repo https://github.com/pop-os/cosmic-session

Name:           cosmic-session
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Session manager for the COSMIC desktop environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-session

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

cargo build


%install

install -Dm0755 target/release/cosmic-session %{_bindir}/cosmic-session]

install -Dm0755 data/start-cosmic %{_bindir}/start-cosmic]
install -Dm0644 data/cosmic-session.target %{_prefix}/lib/systemd/user/cosmic-session.target]
install -Dm0644 data/cosmic.desktop %{_datadir}/wayland-sessions/cosmic.desktop]


%files




%{_bindir}/cosmic-session

%{_bindir}/start-cosmic
%{_prefix}/lib/systemd/user/cosmic-session.target
%{_datadir}/wayland-sessions/cosmic.desktop


%changelog
%autochangelog
    