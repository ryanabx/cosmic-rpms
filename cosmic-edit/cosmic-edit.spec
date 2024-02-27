# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate cosmic-edit
%global repo https://github.com/pop-os/cosmic-edit

Name:           cosmic-edit
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Text editor built using libcosmic for the COSMIC Desktop Environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-edit

Source:         %{crate}.tar.gz
Source:         vendor.tar



# For now, we require all deps for all of cosmic-epoch
BuildRequires:  make
BuildRequires:  which
BuildRequires:  just
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libxkbcommon)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(glib2)
BuildRequires:  pkgconfig(gtk3)
BuildRequires:  pkgconfig(dbus)
BuildRequires:  pkgconfig(wayland)
BuildRequires:  pkgconfig(clang)
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
just build-vendored

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files

%{_bindir}/cosmic-edit
%{_datadir}/applications/com.system76.CosmicEdit.desktop



%changelog
%autochangelog
    