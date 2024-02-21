%global domain  com.system76.CosmicApplets
Name:           cosmic-applets
Version:        master
Release:        %autorelease
Summary:        Applets for COSMIC Panel

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
Applets for COSMIC Panel

%prep
%autosetup

%build
just build --release --bin cosmic-app-list
just build --release --bin cosmic-applet-audio
just build --release --bin cosmic-applet-battery
just build --release --bin cosmic-applet-bluetooth
just build --release --bin cosmic-applet-graphics
just build --release --bin cosmic-applet-network
just build --release --bin cosmic-applet-notifications
just build --release --bin cosmic-applet-power
just build --release --bin cosmic-applet-status-area
just build --release --bin cosmic-applet-tiling
just build --release --bin cosmic-applet-time
just build --release --bin cosmic-applet-workspaces
just build --release --bin cosmic-panel-app-button
just build --release --bin cosmic-panel-button
just build --release --bin cosmic-panel-workspaces-button

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Tue Feb 20 2024 Ryan Brue <ryanbrue@hotmail.com>
- Created package
