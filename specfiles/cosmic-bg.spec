%global appid   com.system76.CosmicBackground
%global commit a1f0552187a9e9c436b392908b76866dea482345
Name:           cosmic-bg
Version:        0.1.0~20240221.a1f055
Release:        %autorelease
Summary:        COSMIC session service which applies backgrounds to displays

License:        MPL-2.0
URL:            https://github.com/pop-os/cosmic-bg
Source0:        https://github.com/pop-os/cosmic-bg/archive/%{commit}.tar.gz

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
COSMIC session service which applies backgrounds to displays

%prep
%autosetup -n cosmic-bg-%{commit}

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%{_bindir}/cosmic-bg
%dir %{_datadir}/cosmic/%{appid}
%{_datadir}/cosmic/%{appid}/*
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml




%changelog
%autochangelog
