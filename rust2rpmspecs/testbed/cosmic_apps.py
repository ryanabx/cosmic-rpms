GPL3 = "GPL-3.0"
MPL2 = "MPL-2.0"

STANDARD_SOURCES = f"""
Source:         %{{crate}}.tar.gz
Source:         %{{crate}}-vendor.tar.xz
"""

STANDARD_REQUIRES = f"""
# For now, we require all deps for all of cosmic-epoch
Requires:       libseat
Requires:       pop-icon-theme
Requires:       greetd
Requires:       greetd-selinux
Requires:       cage
Requires:       mozilla-fira-mono-fonts
Requires:       mozilla-fira-sans-fonts
"""

STANDARD_BUILDREQUIRES = f"""
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
"""

STANDARD_PREP = f"""
%autosetup -n %{{crate}} -p1 -a1
cat .vendor/config.toml >> .cargo/config
"""

STANDARD_BUILD = f"""
cargo build
%{{cargo_license_summary}}
%{{cargo_license}} > LICENSE.dependencies
%{{cargo_vendor_manifest}}
"""

STANDARD_FILES = f"""
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
"""


COSMIC_APP_LIBRARY = {
"globals": f"""
%global appid com.system76.CosmicAppLibrary
""",
"name": "cosmic-app-library",
"repo": "https://github.com/pop-os/cosmic-applibrary",
"summary": "A boilerplate template to get started with GTK, Rust, Meson, Flatpak, Debian made for Cosmic.",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
install -Dm0644 target/release/${{crate}} %{{_bindir}}/${{crate}}
install -Dm0644 data/%{{appid}}.desktop %{{_datadir}}/applications/%{{appid}}.desktop
install -Dm0644 data/%{{appid}}.metainfo.xml %{{_datadir}}/metainfo/%{{appid}}.metainfo.xml
install -Dm0644 data/icons/%{{appid}}.svg %{{_datadir}}/icons/hicolor/scalable/apps/%{{appid}}.svg
""",
"files": STANDARD_FILES + f"""\n
%{{_bindir}}/%{{crate}}
%{{_datadir}}/applications/%{{appid}}.desktop
%{{_datadir}}/metainfo/%{{appid}}.metainfo.xml
%{{_datadir}}/icons/hicolor/scalable/apps/%{{appid}}.svg
"""
}