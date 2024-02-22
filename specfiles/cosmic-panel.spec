%global appid   com.system76.CosmicPanel
%global commit 887e1936c605ae4223f4c04a7ed35dda855390bd
Name:           cosmic-panel
Version:        0.1.0~20240221.887e19
Release:        %autorelease
Summary:        Panel for COSMIC Desktop Environment

License:        GPL-3.0
URL:            https://github.com/pop-os/cosmic-panel
Source0:        https://github.com/pop-os/cosmic-panel/archive/%{commit}.tar.gz

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
Panel for COSMIC Desktop Environment

%prep
%autosetup -n cosmic-panel-%{commit}

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%{_bindir}/cosmic-panel
%{_datadir}/cosmic/%{appid}.Dock/*
%{_datadir}/cosmic/%{appid}.Panel/*
%{_datadir}/cosmic/%{appid}/*
# %{_datadir}/applications/%{appid}.desktop
# %{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
# %{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
# %{_datadir}/metainfo/%{appid}.metainfo.xml


%changelog
%autochangelog
