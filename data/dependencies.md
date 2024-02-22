# Dependency Tracking for COSMIC

### cosmic-applets

### cosmic-applibrary (cosmic-app-library)

### cosmic-bg

### cosmic-comp

#### in fedora repos

anyhow = {version = "1.0.51", features = ["backtrace"]} | rust-anyhow+backtrace-devel @ 1.0.79

bitflags = "2.4" | rust-bitflags-devel @ 2.4.2

bytemuck = "1.12" | rust-bytemuck-devel @ 1.14.1

calloop = {version = "0.12.2", features = ["executor"]} | rust-calloop+executor-devel @ 0.12.4

#### in fedora repos, needs updating

i18n-embed = {version = "0.14", features = ["fluent-system", "desktop-requester"]} | rust-i18n-embed+desktop-requester-devel @ 0.13.9-2, rust-i18n-embed+fluent-system-devel @ 0.13.9-2

i18n-embed-fl = "0.7" | rust-i18n-embed-fl-devel @ 0.6.7-2


#### path-based dependency

cosmic-comp-config = {path = "cosmic-comp-config"}

#### git-based dependency

cosmic-config = {git = "https://github.com/pop-os/libcosmic/", features = ["calloop", "macro"]}

cosmic-protocols = {git = "https://github.com/pop-os/cosmic-protocols", branch = "main", default-features = false, features = ["server"]}

#### Not found in fedora repos

edid-rs = {version = "0.1"}

egui = {version = "0.23.0", optional = true}

egui_plot = {version = "0.23.0", optional = true}

glow = "0.12.0"

#### unsorted so far
[dependencies]
iced_tiny_skia = {git = "https://github.com/pop-os/libcosmic/"}
indexmap = "2.0"
keyframe = "1.1.1"
lazy_static = "1.4.0"
libc = "0.2.149"
libcosmic = {git = "https://github.com/pop-os/libcosmic/", default-features = false}
libsystemd = {version = "0.7", optional = true}
log-panics = {version = "2", features = ["with-backtrace"]}
once_cell = "1.18.0"
ordered-float = "4.0"
png = "0.17.5"
puffin = {version = "0.17.0", optional = true}
puffin_egui = {version = "0.23.0", optional = true}
regex = "1"
renderdoc = {version = "0.11.0", optional = true}
ron = "0.8"
rust-embed = {version = "8.0", features = ["debug-embed"]}
sanitize-filename = "0.5.0"
sendfd = "0.4.1"
serde = {version = "1", features = ["derive"]}
serde_json = "1"
thiserror = "1.0.26"
time = {version = "0.3.30", features = ["macros", "formatting", "local-offset"]}
tiny-skia = "0.11"
tracing = {version = "0.1.37", features = ["max_level_debug", "release_max_level_info"]}
tracing-journald = "0.3.0"
tracing-subscriber = {version = "0.3.16", features = ["env-filter", "tracing-log"]}
wayland-backend = "0.3.2"
wayland-scanner = "0.31.0"
xcursor = "0.3.3"
xdg = "^2.1"
xdg-user = "0.2.1"
xkbcommon = "0.7"
zbus = "3.15.0"

[dependencies.id_tree]
branch = "feature/copy_clone"
git = "https://github.com/Drakulix/id-tree.git"

[dependencies.smithay]
default-features = false
features = [
  "backend_drm",
  "backend_gbm",
  "backend_egl",
  "backend_libinput",
  "backend_session_libseat",
  "backend_udev",
  "backend_winit",
  "backend_vulkan",
  "backend_x11",
  "desktop",
  "use_system_lib",
  "renderer_glow",
  "renderer_multi",
  "wayland_frontend",
  "xwayland",
]
git = "https://github.com/smithay/smithay.git"
rev = "74ef59a3f"
version = "0.3"

[dependencies.smithay-egui]
features = ["svg"]
git = "https://github.com/Smithay/smithay-egui.git"
optional = true
rev = "cdc652e0"

[features]
debug = ["egui", "egui_plot", "smithay-egui", "renderdoc", "puffin", "puffin_egui", "anyhow/backtrace"]
default = ["systemd"]
systemd = ["libsystemd"]

[profile.dev]
lto = "thin"

[profile.fastdebug]
debug = true
inherits = "release"

[profile.release]
lto = "fat"

[patch."https://github.com/Smithay/smithay.git"]
smithay = {git = "https://github.com/smithay//smithay", rev = "094fa3f7c3"}

### cosmic-edit

### cosmic-files

### cosmic-greeter

### cosmic-icons

### cosmic-launcher

### cosmic-notifications

### cosmic-osd

### cosmic-panel

### cosmic-randr

### cosmic-screenshot

### cosmic-session

### cosmic-settings-daemon

### cosmic-settings

### cosmic-store

### cosmic-term

### cosmic-workspaces-epoch (cosmic-workspaces)

### xdg-desktop-portal-cosmic

### launcher (pop-launcher)

## Optional to package

### system76-power