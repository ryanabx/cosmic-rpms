%global commit e87837e1f11fe08729232e4e09038fa396bd906e
Name:           cosmic-settings-daemon
Version:        0.1.0~20240221.e87837
Release:        %autorelease
Summary:        Settings daemon for cosmic-settings

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
Settings daemon for cosmic-settings

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build all

%install
%make_install DEST_DIR=%{buildroot} prefix=%{_prefix}
# mv %{buildroot}/usr/local/%{name} %{buildroot}/${_bindir}/%{name} 

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Feb 20 2024 Ryan Brue <ryanbrue@hotmail.com>
- Created package
