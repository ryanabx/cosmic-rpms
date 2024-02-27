# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-greeter
%global repo https://github.com/pop-os/cosmic-greeter

Name:           cosmic-greeter
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Libcosmic greeter for greetd, which can be run inside cosmic-comp

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-greeter

Source:         %{crate}.tar.gz
Source:         vendor.tar



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

BuildRequires:   systemd-rpm-macros
%{?sysusers_requires_compat}


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
just build-vendored

%install

just rootdir=%{buildroot} prefix=%{_prefix} install
install -Dm0644 cosmic-greeter.toml %{buildroot}/%{_prefix}/etc/greetd/cosmic-greeter.toml
install -Dm0644 debian/cosmic-greeter.service %{buildroot}/%{_unitdir}/cosmic-greeter.service

%pre
%sysusers_create_compat debian/cosmic-greeter.sysusers

%post
%systemd_post cosmic-greeter.service

%preun
%systemd_preun cosmic-greeter.service

%postun
%systemd_postun cosmic-greeter.service


%files

%{_bindir}/cosmic-greeter

%{_bindir}/cosmic-greeter-daemon

%{_sysusersdir}/cosmic-greeter.conf
%{_tmpfilesdir}/cosmic-greeter.conf
%{_datadir}/dbus-1/system.d/com.system76.CosmicGreeter.conf
%{_prefix}/etc/greetd/cosmic-greeter.toml
%{_unitdir}/cosmic-greeter.service


%changelog
%autochangelog
    