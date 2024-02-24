GPL3 = "GPL-3.0"
MPL2 = "MPL-2.0"

def install_app(bin_name, appid, add_bin, add_desktop, add_scaled, add_symbolic, add_metainfo, prescriptor):
    res = """"""
    if add_bin:
        res += f"""install -Dm0644 target/release/{bin_name} %{{_bindir}}/{bin_name}\n"""
    if add_desktop:
        res += f"""install -Dm0644 {prescriptor}/data/{appid}.desktop %{{_datadir}}/applications/{appid}.desktop\n"""
    if add_scaled:
        res += f"""install -Dm0644 {prescriptor}/data/icons/{appid}.svg %{{_datadir}}/icons/hicolor/scalable/apps/{appid}.svg\n"""
    if add_symbolic:
        res += f"""install -Dm0644 {prescriptor}/data/icons/{appid}-symbolic.svg %{{_datadir}}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg\n""" # TODO
    if add_metainfo:
        res += f"""install -Dm0644 {prescriptor}/data/{appid}.metainfo.xml %{{_datadir}}/metainfo/{appid}.metainfo.xml\n"""
    return res

def contains_app(bin_name, appid, add_bin, add_desktop, add_scaled, add_symbolic, add_metainfo, prescriptor):
    res = """"""
    if add_bin:
        res += f"""%{{_bindir}}/{bin_name}\n"""
    if add_desktop:
        res += f"""%{{_datadir}}/applications/{appid}.desktop\n"""
    if add_scaled:
        res += f"""%{{_datadir}}/icons/hicolor/scalable/apps/{appid}.svg\n"""
    if add_symbolic:
        res += f"""%{{_datadir}}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg\n""" # TODO
    if add_metainfo:
        res += f"""%{{_datadir}}/metainfo/{appid}.metainfo.xml\n"""
    return res

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
mkdir .cargo
cp .vendor/config.toml .cargo/config.toml
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
"globals": "",
"name": "cosmic-app-library",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-applibrary",
"reposhort": "cosmic-applibrary",
"commit": "latest",
"summary": "A boilerplate template to get started with GTK, Rust, Meson, Flatpak, Debian made for Cosmic.",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{contains_app("cosmic-app-library","com.system76.CosmicAppLibrary",True, True, True, False, True, "")}
""",
"files": STANDARD_FILES + f"""\n
{install_app("cosmic-app-library","com.system76.CosmicAppLibrary",True, True, True, False, True, "")}
"""
}

COSMIC_APPLETS = {
"globals": "",
"name": "cosmic-applets",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-applets",
"reposhort": "cosmic-applets",
"commit": "latest",
"summary": "WIP applets for cosmic-panel",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": f"""
cargo build --bin cosmic-app-list
cargo build --bin cosmic-applet-audio
cargo build --bin cosmic-applet-battery
cargo build --bin cosmic-applet-bluetooth
cargo build --bin cosmic-applet-graphics
cargo build --bin cosmic-applet-network
cargo build --bin cosmic-applet-notifications
cargo build --bin cosmic-applet-power
cargo build --bin cosmic-applet-time
cargo build --bin cosmic-applet-tiling
cargo build --bin cosmic-applet-status-area
cargo build --bin cosmic-applet-workspaces
%{{cargo_license_summary}}
%{{cargo_license}} > LICENSE.dependencies
%{{cargo_vendor_manifest}}
""",
"install": f"""
{install_app("cosmic-app-list","com.system76.CosmicAppList",True, True, True, False, False, "cosmic-app-list")}
{install_app("cosmic-applet-audio","com.system76.CosmicAppletAudio",True, True, True, False, False, "cosmic-applet-audio")}
{install_app("cosmic-applet-battery","com.system76.CosmicAppletBattery",True, True, True, False, False, "cosmic-applet-battery")}
{install_app("cosmic-applet-bluetooth","com.system76.CosmicAppletBluetooth",True, True, True, False, False, "cosmic-applet-bluetooth")}
{install_app("cosmic-applet-graphics","com.system76.CosmicAppletGraphics",True, True, True, False, False, "cosmic-applet-graphics")}
{install_app("cosmic-applet-network","com.system76.CosmicAppletNetwork",True, True, True, False, False, "cosmic-applet-network")}
{install_app("cosmic-applet-notifications","com.system76.CosmicAppletNotifications",True, True, True, False, False, "cosmic-applet-notifications")}
{install_app("cosmic-applet-power","com.system76.CosmicAppletPower",True, True, True, False, False, "cosmic-applet-power")}
{install_app("cosmic-applet-time","com.system76.CosmicAppletTime",True, True, True, False, False, "cosmic-applet-time")}
{install_app("cosmic-applet-tiling","com.system76.CosmicAppletTiling",True, True, True, False, False, "cosmic-applet-tiling")}
{install_app("cosmic-applet-status-area","com.system76.CosmicAppletStatusArea",True, True, True, False, False, "cosmic-applet-status-area")}
{install_app("cosmic-applet-workspaces","com.system76.CosmicAppletWorkspaces",True, True, True, False, False, "cosmic-applet-workspaces")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-app-list","com.system76.CosmicAppList",True, True, True, False, False, "cosmic-app-list")}
{contains_app("cosmic-applet-audio","com.system76.CosmicAppletAudio",True, True, True, False, False, "cosmic-applet-audio")}
{contains_app("cosmic-applet-battery","com.system76.CosmicAppletBattery",True, True, True, False, False, "cosmic-applet-battery")}
{contains_app("cosmic-applet-bluetooth","com.system76.CosmicAppletBluetooth",True, True, True, False, False, "cosmic-applet-bluetooth")}
{contains_app("cosmic-applet-graphics","com.system76.CosmicAppletGraphics",True, True, True, False, False, "cosmic-applet-graphics")}
{contains_app("cosmic-applet-network","com.system76.CosmicAppletNetwork",True, True, True, False, False, "cosmic-applet-network")}
{contains_app("cosmic-applet-notifications","com.system76.CosmicAppletNotifications",True, True, True, False, False, "cosmic-applet-notifications")}
{contains_app("cosmic-applet-power","com.system76.CosmicAppletPower",True, True, True, False, False, "cosmic-applet-power")}
{contains_app("cosmic-applet-time","com.system76.CosmicAppletTime",True, True, True, False, False, "cosmic-applet-time")}
{contains_app("cosmic-applet-tiling","com.system76.CosmicAppletTiling",True, True, True, False, False, "cosmic-applet-tiling")}
{contains_app("cosmic-applet-status-area","com.system76.CosmicAppletStatusArea",True, True, True, False, False, "cosmic-applet-status-area")}
{contains_app("cosmic-applet-workspaces","com.system76.CosmicAppletWorkspaces",True, True, True, False, False, "cosmic-applet-workspaces")}
"""
}

COSMIC_BG = {
"globals": "",
"name": "cosmic-bg",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-bg",
"reposhort": "cosmic-bg",
"commit": "latest",
"summary": "COSMIC session service which applies backgrounds to displays",
"license": MPL2,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{contains_app("cosmic-bg","com.system76.CosmicBackground",True, True, True, True, True, "")}
""",
"files": STANDARD_FILES + f"""\n
{install_app("cosmic-bg","com.system76.CosmicBackground",True, True, True, True, True, "")}
%{{_datadir}}/cosmic/com.system76.CosmicBackground/*
"""
}