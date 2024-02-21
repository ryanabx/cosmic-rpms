%global appid   com.system76.CosmicSettings
Name:           cosmic-settings
Version:        master
Release:        1%{?dist}
Summary:        The settings application for the COSMIC desktop environment

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
The settings application for the COSMIC desktop environment

%prep
%autosetup

%build
just build-release

%install
just rootdir=%{buildroot} install

%files
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
# %{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
# %{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
# %{_datadir}/metainfo/%{appid}.metainfo.xml


%changelog
* Tue Feb 20 2024 Ryan Brue <ryanbrue@hotmail.com>
- Created package
