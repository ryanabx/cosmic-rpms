# Generated by specgen.py ryanabx

# Generated by rust2rpm 25

# prevent library files from being installed

%global crate pop-launcher
%global repo https://github.com/pop-os/launcher

Name:           pop-launcher
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        Modular IPC-based desktop launcher service 

License:        GPL-3.0

URL:            https://github.com/pop-os/launcher

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

cargo build


%install

install -Dm0755 target/release/pop-launcher %{_bindir}/pop-launcher

#!/usr/bin/env sh
    plugins = 'calc desktop_entries files find pop_shell pulse recent scripts terminal web cosmic_toplevel'
    set -ex
    for plugin in {{plugins}}; do
        dest={{plugin-dir}}${plugin}
        mkdir -p ${dest}
        install -Dm0644 plugins/src/${plugin}/*.ron ${dest}
        ln -sf {{bin-path}} {{plugin-dir}}${plugin}/$(echo ${plugin} | sed 's/_/-/')
    done


%files




%{_bindir}/cosmic-workspaces
%{_datadir}/applications/com.system76.CosmicWorkspaces.desktop



%changelog
%autochangelog
    