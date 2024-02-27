# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate xdg-desktop-portal-cosmic
%global repo https://github.com/pop-os/xdg-desktop-portal-cosmic

Name:           xdg-desktop-portal-cosmic
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        XDG Desktop Portals for the COSMIC Desktop Environment

License:        GPL-3.0

URL:            https://github.com/pop-os/xdg-desktop-portal-cosmic

Source:         %{crate}.tar.gz
Source:         vendor.tar



# For now, we require all deps for all of cosmic-epoch
BuildRequires:  make
BuildRequires:  which
BuildRequires:  just
BuildRequires:  rustc
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libxkbcommon)
BuildRequires:  lld
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(glib2)
BuildRequires:  pkgconfig(gtk3)
BuildRequires:  pkgconfig(dbus)
BuildRequires:  pkgconfig(wayland)
BuildRequires:  pkgconfig(clang)
BuildRequires:  cargo
BuildRequires:  pkgconfig(mesa-libgbm)
BuildRequires:  pkgconfig(pipewire)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(rust-rav1e+nasm-rs)
BuildRequires:  libappstream-glib



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
make all VENDOR=1

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix}

%files

%{_libexecdir}/xdg-desktop-portal-cosmic
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.cosmic.service
%{_datadir}/xdg-desktop-portal/portals/cosmic.portal
%{_datadir}/xdg-desktop-portal/cosmic-portals.conf
%{_datadir}/icons/hicolor/scalable/actions/screenshot-screen-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/screenshot-selection-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/screenshot-window-symbolic.svg


%changelog
%autochangelog
    