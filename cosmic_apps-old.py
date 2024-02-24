GPL3 = "GPL-3.0"
MPL2 = "MPL-2.0"
CC = "CC-BY-SA-4.0"

ROOTDIR = f"%{{buildroot}}"

def standard_just_build_release():
    return f"just build-release"

def standard_just_build_vendored():
    return f"just build-vendored"

def standard_just_install():
    return f"just rootdir=%{{buildroot}} prefix=%{{_prefix}} install"

def install_(path_from, path_to, perms):
    return f"""install -Dm{perms} {path_from} {ROOTDIR}/{path_to}"""

def contains_(path):
    return f"""{path}"""

def install_app(bin_name, appid, add_bin, add_desktop, add_scaled, add_symbolic, add_metainfo, prescriptor, resdir):
    res = """"""
    if add_bin:
        res += install_(f"target/release/{bin_name}", f"%{{_bindir}}/{bin_name}", "0755") + "\n"
    if add_desktop:
        res += install_(f"{prescriptor}{resdir}/{appid}.desktop", f"%{{_datadir}}/applications/{appid}.desktop", "0644") + "\n"
    if add_scaled:
        res += install_(f"{prescriptor}{resdir}/icons/{appid}.svg", f"%{{_datadir}}/icons/hicolor/scalable/apps/{appid}.svg", "0644") + "\n"
    if add_symbolic:
        res += install_(f"{prescriptor}{resdir}/icons/{appid}-symbolic.svg", f"%{{_datadir}}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg", "0644") + "\n" # TODO
    if add_metainfo:
        res += install_(f"{prescriptor}{resdir}/{appid}.metainfo.xml", f"%{{_datadir}}/metainfo/{appid}.metainfo.xml", "0644") + "\n"
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

OLDSTANDARD_PREP = f"""
%autosetup -n %{{crate}} -p1 -a1
ls -a
mkdir -p .cargo
cp .vendor/config.toml .cargo/config.toml
"""


STANDARD_PREP = f"""
%autosetup -n %{{crate}}
mv ../%{{crate}}-vendor.tar.xz vendor.tar.xz
ls -a
mkdir -p .cargo
cp .vendor/config.toml .cargo/config.toml
"""

STANDARD_BUILD = standard_just_build_vendored()

OLDSTANDARD_BUILD = f"""
cargo build --all -r
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
"dinstall": f"""
{install_app("cosmic-app-library","com.system76.CosmicAppLibrary",True, True, True, False, True, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-app-library","com.system76.CosmicAppLibrary",True, True, True, False, True, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-app-list","com.system76.CosmicAppList",True, True, True, False, False, "cosmic-app-list/", "data")}
{install_app("cosmic-applet-audio","com.system76.CosmicAppletAudio",True, True, True, False, False, "cosmic-applet-audio/", "data")}
{install_app("cosmic-applet-battery","com.system76.CosmicAppletBattery",True, True, True, False, False, "cosmic-applet-battery/", "data")}
{install_app("cosmic-applet-bluetooth","com.system76.CosmicAppletBluetooth",True, True, True, False, False, "cosmic-applet-bluetooth/", "data")}
{install_app("cosmic-applet-graphics","com.system76.CosmicAppletGraphics",True, True, True, False, False, "cosmic-applet-graphics/", "data")}
{install_app("cosmic-applet-network","com.system76.CosmicAppletNetwork",True, True, True, False, False, "cosmic-applet-network/", "data")}
{install_app("cosmic-applet-notifications","com.system76.CosmicAppletNotifications",True, True, True, False, False, "cosmic-applet-notifications/", "data")}
{install_app("cosmic-applet-power","com.system76.CosmicAppletPower",True, True, True, False, False, "cosmic-applet-power/", "data")}
{install_app("cosmic-applet-time","com.system76.CosmicAppletTime",True, True, True, False, False, "cosmic-applet-time/", "data")}
{install_app("cosmic-applet-tiling","com.system76.CosmicAppletTiling",True, True, True, False, False, "cosmic-applet-tiling/", "data")}
{install_app("cosmic-applet-status-area","com.system76.CosmicAppletStatusArea",True, True, True, False, False, "cosmic-applet-status-area/", "data")}
{install_app("cosmic-applet-workspaces","com.system76.CosmicAppletWorkspaces",True, True, True, False, False, "cosmic-applet-workspaces/", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-app-list","com.system76.CosmicAppList",True, True, True, False, False, "cosmic-app-list/")}
{contains_app("cosmic-applet-audio","com.system76.CosmicAppletAudio",True, True, True, False, False, "cosmic-applet-audio/")}
{contains_app("cosmic-applet-battery","com.system76.CosmicAppletBattery",True, True, True, False, False, "cosmic-applet-battery/")}
{contains_app("cosmic-applet-bluetooth","com.system76.CosmicAppletBluetooth",True, True, True, False, False, "cosmic-applet-bluetooth/")}
{contains_app("cosmic-applet-graphics","com.system76.CosmicAppletGraphics",True, True, True, False, False, "cosmic-applet-graphics/")}
{contains_app("cosmic-applet-network","com.system76.CosmicAppletNetwork",True, True, True, False, False, "cosmic-applet-network/")}
{contains_app("cosmic-applet-notifications","com.system76.CosmicAppletNotifications",True, True, True, False, False, "cosmic-applet-notifications/")}
{contains_app("cosmic-applet-power","com.system76.CosmicAppletPower",True, True, True, False, False, "cosmic-applet-power/")}
{contains_app("cosmic-applet-time","com.system76.CosmicAppletTime",True, True, True, False, False, "cosmic-applet-time/")}
{contains_app("cosmic-applet-tiling","com.system76.CosmicAppletTiling",True, True, True, False, False, "cosmic-applet-tiling/")}
{contains_app("cosmic-applet-status-area","com.system76.CosmicAppletStatusArea",True, True, True, False, False, "cosmic-applet-status-area/")}
{contains_app("cosmic-applet-workspaces","com.system76.CosmicAppletWorkspaces",True, True, True, False, False, "cosmic-applet-workspaces/")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-bg","com.system76.CosmicBackground",True, True, True, True, True, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-bg","com.system76.CosmicBackground",True, True, True, True, True, "")}
""",
"install": standard_just_install()
}
# {contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicBackground/*")}

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
"dinstall": f"""
{install_app("cosmic-comp","com.system76.CosmicComp",True, False, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-comp","com.system76.CosmicComp",True, False, False, False, False, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-edit","com.system76.CosmicEdit",True, True, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-edit","com.system76.CosmicEdit",True, True, False, False, False, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "", "res")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-greeter","com.system76.CosmicGreeter",True, False, False, False, False, "", "data")}
{install_app("cosmic-greeter-daemon","",True, False, False, False, False, "", "data")}
{install_(f"debian/cosmic-greeter.sysusers", f"%{{_prefix}}/lib/sysusers.d/cosmic-greeter.conf", "0644")}
{install_(f"debian/cosmic-greeter.tmpfiles", f"%{{_prefix}}/lib/tmpfiles.d/cosmic-greeter.conf", "0644")}
{install_(f"dbus/com.system76.CosmicGreeter.conf", f"%{{_datadir}}/dbus-1/system.d/com.system76.CosmicGreeter.conf", "0644")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-greeter","com.system76.CosmicGreeter",True, False, False, False, False, "")}
{contains_app("cosmic-greeter-daemon","",True, False, False, False, False, "")}
{contains_(f"%{{_prefix}}/lib/sysusers.d/cosmic-greeter.conf")}
{contains_(f"%{{_prefix}}/lib/tmpfiles.d/cosmic-greeter.conf")}
{contains_(f"%{{_datadir}}/dbus-1/system.d/com.system76.CosmicGreeter.conf")}
""",
"install": standard_just_install()
}

COSMIC_ICONS = {
"globals": "",
"name": "cosmic-icons",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-icons",
"reposhort": "cosmic-icons",
"commit": "latest",
"summary": "System76 Cosmic icon theme for Linux",
"license": CC,
"sources": f"Source:         %{{crate}}.tar.gz",
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": f"%autosetup -n cosmic-icons",
"build": "",
"dinstall": f"""
just rootdir=%{{buildroot}} prefix=%{{_prefix}} install
""",
"files": STANDARD_FILES + f"""\n
{contains_(f"%dir %{{_datadir}}/icons/Cosmic")}
{contains_(f"%{{_datadir}}/icons/Cosmic/*")}
""",
"install": standard_just_install()
}

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
"dinstall": f"""
{install_app("cosmic-launcher","com.system76.CosmicLauncher",True, True, True, False, True, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-launcher","com.system76.CosmicLauncher",True, True, True, False, True, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-notifications","com.system76.CosmicNotifications",True, True, True, False, True, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-notifications","com.system76.CosmicNotifications",True, True, True, False, True, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-osd","com.system76.CosmicOsd",True, False, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-osd","com.system76.CosmicOsd",True, False, False, False, False, "")}
""",
"install": standard_just_install()
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
"dinstall": f"""
{install_app("cosmic-panel","com.system76.CosmicPanel",True, False, False, False, False, "", "data")}
find 'data'/'default_schema' -type f -exec echo {{}} \\; | rev | cut -d'/' -f-3 | rev | xargs -d '\\n' -I {{}} install -Dm0644 'data'/'default_schema'/{{}} '%{{_datadir}}'/'cosmic'/{{}}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-panel","com.system76.CosmicPanel",True, False, False, False, False, "")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicPanel.Dock/*")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicPanel.Panel/*")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicPanel/*")}
""",
"install": standard_just_install()
}

COSMIC_PLAYER = {
"globals": "",
"name": "cosmic-player",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-player",
"reposhort": "cosmic-player",
"commit": "latest",
"summary": "WIP COSMIC media player",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-files","com.system76.CosmicFiles",True, True, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_RANDR = {
"globals": "",
"name": "cosmic-randr",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-randr",
"reposhort": "cosmic-randr",
"commit": "latest",
"summary": "Library and utility for displaying and configuring Wayland outputs",
"license": MPL2,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-randr","",True, False, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-randr","",True, False, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_SCREENSHOT = {
"globals": "",
"name": "cosmic-screenshot",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-screenshot",
"reposhort": "cosmic-screenshot",
"commit": "latest",
"summary": "Utility for capturing screenshots via XDG Desktop Portal",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-screenshot","com.system76.CosmicScreenshot",True, True, False, False, False, "", "resources")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-screenshot","com.system76.CosmicScreenshot",True, True, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_SESSION = {
"globals": "",
"name": "cosmic-session",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-session",
"reposhort": "cosmic-session",
"commit": "latest",
"summary": "Session manager for the COSMIC desktop environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-session","",True, False, False, False, False, "", "data")}
{install_(f"data/start-cosmic", f"%{{_bindir}}/start-cosmic", "0755")}
{install_(f"data/cosmic-session.target", f"%{{_prefix}}/lib/systemd/user/cosmic-session.target", "0644")}
{install_(f"data/cosmic.desktop", f"%{{_datadir}}/wayland-sessions/cosmic.desktop", "0644")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-session","",True, False, False, False, False, "")}
{contains_(f"%{{_bindir}}/start-cosmic")}
{contains_(f"%{{_prefix}}/lib/systemd/user/cosmic-session.target")}
{contains_(f"%{{_datadir}}/wayland-sessions/cosmic.desktop")}
""",
"install": standard_just_install()
}

COSMIC_SETTINGS_DAEMON = {
"globals": "",
"name": "cosmic-settings-daemon",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-settings-daemon",
"reposhort": "cosmic-settings-daemon",
"commit": "latest",
"summary": "Settings daemon for cosmic-settings",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-settings-daemon","",True, False, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-settings-daemon","",True, False, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_SETTINGS = {
"globals": "",
"name": "cosmic-settings",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-settings",
"reposhort": "cosmic-settings",
"commit": "latest",
"summary": "The settings application for the COSMIC desktop environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-settings","com.system76.CosmicSettings",True, True, False, False, False, "", "resources")}
find 'resources'/'default_schema' -type f -exec echo {{}} \\; | rev | cut -d'/' -f-3 | rev | xargs -d '\\n' -I {{}} install -Dm0644 'resources'/'default_schema'/{{}} '%{{_datadir}}'/'cosmic'/{{}}
find 'resources'/'icons' -type f -exec echo {{}} \\; | rev | cut -d'/' -f-3 | rev | xargs -d '\\n' -I {{}} install -Dm0644 'resources'/'icons'/{{}} {{{{iconsdir}}}}/{{}}

""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-settings","com.system76.CosmicSettings",True, True, False, False, False, "")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicTheme.Dark.Builder/*")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicTheme.Dark/*")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicTheme.Light.Builder/*")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicTheme.Light/*")}
{contains_(f"%{{_datadir}}/cosmic/com.system76.CosmicTheme.Mode/*")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-dark-style-round.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-dark-style-slightly-round.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-dark-style-square.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-light-style-round.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-light-style-slightly-round.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-light-style-square.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-mode-dark.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/status/illustration-appearance-mode-light.svg")}
""",
"install": standard_just_install()
}

COSMIC_STORE = {
"globals": "",
"name": "cosmic-store",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-store",
"reposhort": "cosmic-store",
"commit": "latest",
"summary": "COSMIC App Store",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-store","com.system76.CosmicStore",True, True, False, False, False, "", "res")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-store","com.system76.CosmicStore",True, True, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_TERM = {
"globals": "",
"name": "cosmic-term",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-term",
"reposhort": "cosmic-term",
"commit": "latest",
"summary": "WIP COSMIC terminal emulator, built using alacritty_terminal that is provided by the alacritty project. cosmic-term provides bidirectional rendering and ligatures with a custom renderer based on cosmic-text.",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-term","com.system76.CosmicTerm",True, True, False, False, False, "", "res")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-term","com.system76.CosmicTerm",True, True, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_WORKSPACES = {
"globals": "",
"name": "cosmic-workspaces",
"version": "0.1.0",
"repo": "https://github.com/pop-os/cosmic-workspaces-epoch",
"reposhort": "cosmic-workspaces-epoch",
"commit": "latest",
"summary": "COSMIC Workspaces",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("cosmic-workspaces","com.system76.CosmicWorkspaces",True, True, False, False, False, "", "data")}
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-workspaces","com.system76.CosmicWorkspaces",True, True, False, False, False, "")}
""",
"install": standard_just_install()
}

COSMIC_XDG_DESKTOP_PORTAL = {
"globals": "",
"name": "xdg-desktop-portal-cosmic",
"version": "0.1.0",
"repo": "https://github.com/pop-os/xdg-desktop-portal-cosmic",
"reposhort": "xdg-desktop-portal-cosmic",
"commit": "latest",
"summary": "XDG Desktop Portals for the COSMIC Desktop Environment",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_(f"target/release/xdg-desktop-portal-cosmic",f"%{{_libexecdir}}/xdg-desktop-portal-cosmic", "0755")}
{install_(f"data/cosmic.portal", f"%{{_datadir}}/xdg-desktop-portal/portals/cosmic.portal", "0644")}
{install_(f"data/cosmic-portals.conf", f"%{{_datadir}}/xdg-desktop-portal/cosmic-portals.conf", "0644")}
find 'data'/'icons' -type f -exec echo {{}} \\; \\
		| rev \\
		| cut -d'/' -f-3 \\
		| rev \\
		| xargs -d '\\n' -I {{}} install -Dm0644 'data'/'icons'/{{}} %{{_datadir}}/icons/{{}}

""",
"files": STANDARD_FILES + f"""\n
{contains_(f"%{{_libexecdir}}/xdg-desktop-portal-cosmic")}
{contains_(f"%{{_datadir}}/dbus-1/services/org.freedesktop.impl.portal.desktop.cosmic.service")}
{contains_(f"%{{_datadir}}/xdg-desktop-portal/portals/cosmic.portal")}
{contains_(f"%{{_datadir}}/xdg-desktop-portal/cosmic-portals.conf")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/actions/screenshot-screen-symbolic.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/actions/screenshot-selection-symbolic.svg")}
{contains_(f"%{{_datadir}}/icons/hicolor/scalable/actions/screenshot-window-symbolic.svg")}
""",
"install": standard_just_install()
}

POP_LAUNCHER = {
"globals": "",
"name": "pop-launcher",
"version": "0.1.0",
"repo": "https://github.com/pop-os/launcher",
"reposhort": "launcher",
"commit": "latest",
"summary": "Modular IPC-based desktop launcher service ",
"license": GPL3,
"sources": STANDARD_SOURCES,
"buildrequires": STANDARD_BUILDREQUIRES,
"requires": STANDARD_REQUIRES,
"prep": STANDARD_PREP,
"build": STANDARD_BUILD,
"dinstall": f"""
{install_app("pop-launcher","",True, False, False, False, False, "", "data")}
#!/usr/bin/env sh
    plugins = 'calc desktop_entries files find pop_shell pulse recent scripts terminal web cosmic_toplevel'
    set -ex
    for plugin in {{{{plugins}}}}; do
        dest={{{{plugin-dir}}}}${{plugin}}
        mkdir -p ${{dest}}
        install -Dm0644 plugins/src/${{plugin}}/*.ron ${{dest}}
        ln -sf {{{{bin-path}}}} {{{{plugin-dir}}}}${{plugin}}/$(echo ${{plugin}} | sed 's/_/-/')
    done
""",
"files": STANDARD_FILES + f"""\n
{contains_app("cosmic-workspaces","com.system76.CosmicWorkspaces",True, True, False, False, False, "")}
""",
"install": standard_just_install()
}