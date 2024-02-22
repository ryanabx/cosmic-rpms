%global commit edd405ed84186ee24307deb7da6f25efc85986e9
Name:           cosmic-icons
Version:        0.1.0~20240221.edd405
Release:        %autorelease
Summary:        System76 Cosmic icon theme for Linux

License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/cosmic-icons
Source0:        https://github.com/pop-os/cosmic-icons/archive/%{commit}.tar.gz

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
System76 Cosmic icon theme for Linux

%prep
%autosetup -n cosmic-icons-%{commit}

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%dir %{_datadir}/icons/Cosmic
%{_datadir}/icons/Cosmic/*


%changelog
%autochangelog
