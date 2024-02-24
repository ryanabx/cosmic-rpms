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

cargo build --target-dir target


%install

install -Dm0755 target/release/xdg-desktop-portal-cosmic %{_libexecdir}/xdg-desktop-portal-cosmic
install -Dm0644 data/cosmic.portal %{_datadir}/xdg-desktop-portal/portals/cosmic.portal
install -Dm0644 data/cosmic-portals.conf %{_datadir}/xdg-desktop-portal/cosmic-portals.conf
find 'data'/'icons' -type f -exec echo {} \; \
		| rev \
		| cut -d'/' -f-3 \
		| rev \
		| xargs -d '\n' -I {} install -Dm0644 'data'/'icons'/{} %{_datadir}/icons/{}



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
    