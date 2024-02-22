%global appid   com.system76.CosmicTerm
%global commit 01052fae0b3eea67e791ea3d07994c1fa20e8d03

Name:           cosmic-term
Version:        0.1.0~20240221.01052f
Release:        %autorelease
Summary:        COSMIC Terminal Emulator
License:        GPL-3.0
URL:            https://github.com/pop-os/cosmic-term
Source0:        https://github.com/pop-os/cosmic-term/archive/%{commit}.tar.gz

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

%description
COSMIC Terminal Emulator

%prep
%autosetup -n cosmic-term-%{commit}

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/cosmic-term
%{_datadir}/applications/%{appid}.desktop

%changelog
%autochangelog
