GPL3 = "GPL-3.0"
MPL2 = "MPL-2.0"
CC = "CC-BY-SA-4.0"

def install_(path_from, path_to):
    return f"""install -Dm0644 {path_from} {path_to}]"""

def contains_(path):
    return f"""{path}"""

def install_app(bin_name, appid, add_bin, add_desktop, add_scaled, add_symbolic, add_metainfo, prescriptor):
    res = """"""
    if add_bin:
        res += install_(f"target/release/{bin_name}", f"%{{_bindir}}/{bin_name}") + "\n"
    if add_desktop:
        res += install_(f"{prescriptor}/data/{appid}.desktop", f"%{{_datadir}}/applications/{appid}.desktop") + "\n"
    if add_scaled:
        res += install_(f"{prescriptor}/data/icons/{appid}.svg", f"%{{_datadir}}/icons/hicolor/scalable/apps/{appid}.svg") + "\n"
    if add_symbolic:
        res += install_(f"{prescriptor}/data/icons/{appid}-symbolic.svg", f"%{{_datadir}}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg") + "\n" # TODO
    if add_metainfo:
        res += install_(f"{prescriptor}/data/{appid}.metainfo.xml", f"%{{_datadir}}/metainfo/{appid}.metainfo.xml") + "\n"
    return res



def contains_app(bin_name, appid, add_bin, add_desktop, add_scaled, add_symbolic, add_metainfo, prescriptor):
    res = """"""
    if add_bin:
        res += contains_(f"""%{{_bindir}}/{bin_name}\n""")
    if add_desktop:
        res += contains_(f"""%{{_datadir}}/applications/{appid}.desktop\n""")
    if add_scaled:
        res += contains_(f"""%{{_datadir}}/icons/hicolor/scalable/apps/{appid}.svg\n""")
    if add_symbolic:
        res += contains_(f"""%{{_datadir}}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg\n""") # TODO
    if add_metainfo:
        res += contains_(f"""%{{_datadir}}/metainfo/{appid}.metainfo.xml\n""")
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

RUST_PACKAGING_REQUIRES = f"""
BuildRequires: cargo-rpm-macros >= 26.1
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
ls -a
mkdir .cargo
cp .vendor/config.toml .cargo/config.toml
"""

STANDARD_BUILD = f"""
cargo build
"""

STANDARD_BUILD_RUST_PACKAGING = f"""
%{{cargo_license_summary}}
%{{cargo_license}} > LICENSE.dependencies
%{{cargo_vendor_manifest}}
"""

STANDARD_FILES = f"""

"""

STANDARD_FILES_RUST_PACKAGING = f"""
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
"""

STANDARD_GLOBALS_RUST_PACKAGING = f"""
%bcond_without check
%global __cargo_is_lib() 0
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
{install_app("cosmic-app-library","com.system76.CosmicAppLibrary",True, True, True, False, True, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-app-library","com.system76.CosmicAppLibrary",True, True, True, False, True, "")}
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
{install_app("cosmic-bg","com.system76.CosmicBackground",True, True, True, True, True, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-bg","com.system76.CosmicBackground",True, True, True, True, True, "")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicBackground/*")}
"""
}

COSMIC_COMP = {
"globals": "",
"name": "cosmic-comp",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-comp",
"reposhort": "cosmic-comp",
"commit": "latest",
"summary": "Compositor for the COSMIC Desktop Environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-comp","com.system76.CosmicComp",True, False, False, False, False, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-comp","com.system76.CosmicComp",True, False, False, False, False, "")}
"""
}

COSMIC_EDIT = {
"globals": "",
"name": "cosmic-edit",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-edit",
"reposhort": "cosmic-edit",
"commit": "latest",
"summary": "Text editor built using libcosmic for the COSMIC Desktop Environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-edit","com.system76.CosmicEdit",True, True, False, False, False, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-edit","com.system76.CosmicEdit",True, True, False, False, False, "")}
"""
}

COSMIC_FILES = {
"globals": "",
"name": "cosmic-files",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-files",
"reposhort": "cosmic-files",
"commit": "latest",
"summary": "File browser built using libcosmic for the COSMIC Desktop Environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "")}
"""
}

COSMIC_GREETER = {
"globals": "",
"name": "cosmic-greeter",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-greeter",
"reposhort": "cosmic-greeter",
"commit": "latest",
"summary": "Libcosmic greeter for greetd, which can be run inside cosmic-comp",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-greeter","com.system76.CosmicGreeter",True, False, False, False, False, "")}
{install_app("cosmic-greeter-daemon","",True, False, False, False, False, "")}
{install_(f"debian/cosmic-greeter.sysusers", f"%{{_prefix}}/lib/sysusers.d/cosmic-greeter.conf")}
{install_(f"debian/cosmic-greeter.tmpfiles", f"%{{_prefix}}/lib/tmpfiles.d/cosmic-greeter.conf")}
{install_(f"dbus/com.system76.CosmicGreeter.conf", f"%{{_datadir}}/dbus-1/system.d/com.system76.CosmicGreeter.conf")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-greeter","com.system76.CosmicGreeter",True, False, False, False, False, "")}
{contains_app("cosmic-greeter-daemon","",True, False, False, False, False, "")}
{contains_(f"%{{_prefix}}/lib/sysusers.d/cosmic-greeter.conf")}
{contains_(f"%{{_prefix}}/lib/tmpfiles.d/cosmic-greeter.conf")}
{contains_(f"%{{_datadir}}/dbus-1/system.d/com.system76.CosmicGreeter.conf")}
"""
}

# COSMIC_ICONS = {
# "globals": "",
# "name": "cosmic-icons",
# "version": "0.1.0",
# "repo": "https://github.com/pop-os/cosmic-icons",
# "reposhort": "cosmic-icons",
# "commit": "latest",
# "summary": "System76 Cosmic icon theme for Linux",
# "license": CC,
# "sources": STANDARD_SOURCES,
# "buildrequires": STANDARD_BUILDREQUIRES,
# "requires": STANDARD_REQUIRES,
# "prep": STANDARD_PREP,
# "build": STANDARD_BUILD,
# "install": f"""
# {install_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "")}
# """,
# "files": STANDARD_FILES + f"""\n
# {contains_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "")}
# """
# }

COSMIC_LAUNCHER = {
"globals": "",
"name": "cosmic-launcher",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-launcher",
"reposhort": "cosmic-launcher",
"commit": "latest",
"summary": "Layer shell frontend for Pop Launcher",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-launcher","com.system76.CosmicLauncher",True, True, True, False, True, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-launcher","com.system76.CosmicLauncher",True, True, True, False, True, "")}
"""
}

COSMIC_NOTIFICATIONS = {
"globals": "",
"name": "cosmic-notifications",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-notifications",
"reposhort": "cosmic-notifications",
"commit": "latest",
"summary": "Layer Shell notifications daemon which integrates with COSMIC",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-notifications","com.system76.CosmicNotifications",True, True, True, False, True, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-notifications","com.system76.CosmicNotifications",True, True, True, False, True, "")}
"""
}

COSMIC_OSD = {
"globals": "",
"name": "cosmic-osd",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-osd",
"reposhort": "cosmic-osd",
"commit": "latest",
"summary": "OSDs for the COSMIC desktop environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-osd","com.system76.CosmicOsd",True, False, False, False, False, "")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-osd","com.system76.CosmicOsd",True, False, False, False, False, "")}
"""
}

COSMIC_PANEL = {
"globals": "",
"name": "cosmic-panel",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-panel",
"reposhort": "cosmic-panel",
"commit": "latest",
"summary": "Panel for COSMIC Desktop Environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"install": f"""
{install_app("cosmic-panel","com.system76.CosmicPanel",True, False, False, False, False, "")}
{install_(f"debian/cosmic-greeter.sysusers", f"%{{_prefix}}/lib/sysusers.d/cosmic-greeter.conf")}
{install_(f"debian/cosmic-greeter.tmpfiles", f"%{{_prefix}}/lib/tmpfiles.d/cosmic-greeter.conf")}
{install_(f"dbus/com.system76.CosmicGreeter.conf", f"%{{_datadir}}/dbus-1/system.d/com.system76.CosmicGreeter.conf")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-panel","com.system76.CosmicPanel",True, False, False, False, False, "")}
{contains_(f"%{{_prefix}}/lib/sysusers.d/cosmic-greeter.conf")}
{contains_(f"%{{_prefix}}/lib/tmpfiles.d/cosmic-greeter.conf")}
{contains_(f"%{{_datadir}}/dbus-1/system.d/com.system76.CosmicGreeter.conf")}
"""
}