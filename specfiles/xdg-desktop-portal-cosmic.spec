%global DBUS_NAME = org.freedesktop.impl.portal.desktop.cosmic
Name:           xdg-desktop-portal-cosmic
Version:        master
Release:        %autorelease
Summary:        XDG Desktop Portals for the COSMIC Desktop Environment

License:        GPL-3.0
URL:            https://github.com/pop-os/%{name}
Source0:        https://github.com/pop-os/%{name}/archive/refs/heads/%{version}.tar.gz

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
XDG Desktop Portals for the COSMIC Desktop Environment

%prep
%autosetup

%build
%make_build all

%install
%make_install DEST_DIR=%{buildroot} prefix=%{_prefix}

%files
%license LICENSE
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/%{DBUS_NAME}.service
%{_datadir}/xdg-desktop-portal/portals/cosmic.portal
%{_datadir}/xdg-desktop-portal/cosmic-portals.conf

%changelog
* Tue Feb 20 2024 Ryan Brue <ryanbrue@hotmail.com>
- Created package
