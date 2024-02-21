%global appid   com.system76.CosmicScreenshot
%global commit 98cafde5e30472f8f50c8fb5ef61ffbb4c0e3c13
Name:           cosmic-screenshot
Version:        0.1.0~20240221.98cafd
Release:        %autorelease
Summary:        Utility for capturing screenshots via XDG Desktop Portal 

License:        GPL-3.0
URL:            https://github.com/pop-os/%{name}
Source0:        https://github.com/pop-os/%{name}/archive/%{commit}.tar.gz

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
Utility for capturing screenshots via XDG Desktop Portal 

%prep
%autosetup

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
# %{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
# %{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
# %{_datadir}/metainfo/%{appid}.metainfo.xml


%changelog
* Tue Feb 20 2024 Ryan Brue <ryanbrue@hotmail.com>
- Created package
