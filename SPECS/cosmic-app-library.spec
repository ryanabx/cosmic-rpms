%global count 1
%global commit e214e9867876c96b24568d8a45aaca2936269d9b
%global shortcommit %{lua:print(macros.commit:sub(1,7))}

%global APPID com.system76.CosmicAppLibrary

# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate cosmic-app-library

Name:           cosmic-app-library
Version:        0.1.0~%{count}.%{shortcommit}
Release:        %autorelease
Summary:        A boilerplate template to get started with GTK, Rust, Meson, Flatpak, Debian made for Cosmic.

SourceLicense:  None
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown
# FIXME: No license information in crate metadata.

URL:            https://github.com/pop-os/cosmic-applibrary
Source:         https://github.com/pop-os/cosmic-applibrary/archive/%{commit}
Source:         cosmic-app-library-0.1.0-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n cosmic-applibrary-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install
install -Dm0644 %{_datadir}/applications/%{APPID}.desktop
install -Dm0644 %{_datadir}/metainfo/%{APPID}.metainfo.xml

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/cosmic-app-library
%{_datadir}/applications/%{APPID}.desktop
%{_datadir}/metainfo/%{APPID}.metainfo.xml



%changelog
%autochangelog
