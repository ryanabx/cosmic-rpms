%global commit e214e9867876c96b24568d8a45aaca2936269d9b

%global appid com.system76.CosmicBackground

# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate cosmic-bg
%global repo cosmic-bg

Name:           cosmic-bg
Version:        0.1.0

Release:        %autorelease
Summary:        COSMIC session service which applies backgrounds to displays.

SourceLicense:  None
# FIXME: paste output of %%cargo_license_summary here
License:        MPL-2.0
# LICENSE.dependencies contains a full license breakdown
# FIXME: No license information in crate metadata.

URL:            https://github.com/pop-os/%{repo}
Source:         %{crate}.tar.gz
Source:         %{crate}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 26.1

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
%cargo_prep -v deps

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install
install -Dm0644 data/%{appid}.desktop %{_datadir}/applications/%{appid}.desktop
install -Dm0644 data/%{appid}.metainfo.xml %{_datadir}/metainfo/%{appid}.metainfo.xml
install -Dm0644 data/icons/%{appid}.svg %{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
install -Dm0644 data/icons/%{appid}-symbolic.svg %{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/cosmic-bg
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg

%changelog
%autochangelog
