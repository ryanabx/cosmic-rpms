%global appid   com.system76.CosmicGreeter
%global commit af0a5fd4566d4570ba5c92e880a9b09202623bb4

Name:           cosmic-greeter
Version:        0.1.0~20240221.af0a5f
Release:        %autorelease
Summary:        Login Manager for COSMIC based on GreetD
License:        GPL-3.0
URL:            https://github.com/pop-os/cosmic-greeter
Source0:        https://github.com/pop-os/cosmic-greeter/archive/%{commit}.tar.gz

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
Login Manager for COSMIC based on GreetD

%prep
%autosetup -n cosmic-greeter-%{commit}

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/cosmic-greeter
%{_datadir}/dbus-1/system.d/%{appid}.conf
%{_prefix}/lib/tmpfiles.d/cosmic-greeter.conf
%{_prefix}/lib/sysusers.d/cosmic-greeter.conf
%{_bindir}/cosmic-greeter-daemon

%changelog
%autochangelog
