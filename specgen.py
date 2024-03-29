import cosmic_apps
import subprocess

SPEC_FOLDER = "SPECS"
BUILD_SCRIPTS_FOLDER = "BUILD_SCRIPTS"


BUILD_APPS = [
    cosmic_apps.COSMIC_APP_LIBRARY,
    cosmic_apps.COSMIC_APPLET_APP_LIST,
    cosmic_apps.COSMIC_APPLET_AUDIO,
    cosmic_apps.COSMIC_APPLET_BATTERY,
    cosmic_apps.COSMIC_APPLET_BLUETOOTH,
    cosmic_apps.COSMIC_APPLET_NETWORK,
    cosmic_apps.COSMIC_APPLET_NOTIFICATIONS,
    cosmic_apps.COSMIC_APPLET_POWER,
    cosmic_apps.COSMIC_APPLET_STATUS_AREA,
    cosmic_apps.COSMIC_APPLET_TILING,
    cosmic_apps.COSMIC_APPLET_TIME,
    cosmic_apps.COSMIC_APPLET_WORKSPACES,
    cosmic_apps.COSMIC_APPLET_PANEL_BUTTON,
    cosmic_apps.COSMIC_BG,
    cosmic_apps.COSMIC_COMP,
    cosmic_apps.COSMIC_EDIT,
    cosmic_apps.COSMIC_FILES,
    cosmic_apps.COSMIC_GREETER,
    cosmic_apps.COSMIC_LAUNCHER,
    cosmic_apps.COSMIC_NOTIFICATIONS,
    cosmic_apps.COSMIC_OSD,
    cosmic_apps.COSMIC_PANEL,
    cosmic_apps.COSMIC_RANDR,
    cosmic_apps.COSMIC_SCREENSHOT,
    cosmic_apps.COSMIC_SESSION,
    cosmic_apps.COSMIC_SETTINGS,
    cosmic_apps.COSMIC_SETTINGS_DAEMON,
    cosmic_apps.COSMIC_STORE,
    cosmic_apps.COSMIC_TERM,
    cosmic_apps.COSMIC_WORKSPACES,
    cosmic_apps.COSMIC_XDG_DESKTOP_PORTAL,
    cosmic_apps.POP_LAUNCHER
]

BUILD_ETC = [cosmic_apps.COSMIC_ICONS]

def make_spec(specinfo):
    spec = f"""# Generated by specgen.py ryanabx
{specinfo["globals"]}
# Generated by rust2rpm 25

# prevent library files from being installed

%global crate {specinfo["name"]}
%global repo {specinfo["repo"]}

Name:           {specinfo["name"]}
Version:        # TO BE REPLACED AUTOMATICALLY

Release:        %autorelease
Summary:        {specinfo["summary"]}

License:        {specinfo["license"]}

URL:            {specinfo["repo"]}
{specinfo["sources"]}

{specinfo["buildrequires"]}

{specinfo["requires"]}

%global _description %{{expand:
%{{summary}}.}}

%description %{{_description}}

%prep
{specinfo["prep"]}

%build
{specinfo["build"]}

%install
{specinfo["install"]}

%files
{specinfo["files"]}

%changelog
%autochangelog
    """

    with open(f'{specinfo["name"]}/{specinfo["name"]}.spec', 'w') as f:
        f.write(spec)

def make_build_srpm_script(specinfo):
    scr = f"""#!/bin/bash -x

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='{specinfo["name"]}'
version='{specinfo["version"]}'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='{specinfo["name"]}/*'
pop_repo='{specinfo["reposhort"]}'

# Commit to target. Use "latest" if you want master
commit="{specinfo["commit"]}"

# Don't edit anything past this line 
# ===================================================== #

LATEST="latest"

cd ../..
# We should be in the base directory now

git clone --recurse-submodules https://github.com/pop-os/$pop_repo

cd $pop_repo

if [[ "$commit" == "$LATEST" ]]
then
    commit=$(git rev-parse HEAD)
fi

echo $commit
short_commit=${{commit:0:6}}

git reset --hard $commit

mkdir .vendor

cargo vendor > .vendor/config.toml

tar -pcf vendor.tar vendor && mv vendor.tar ../vendor.tar

rm -rf vendor && cd ..

# Back into cosmic-rpms

ls

if [ "$pop_repo" != "$name" ]; then
    mv $pop_repo $name
else
    echo "names are equal. continuing..."
fi

tar -czf $name.tar.gz $name

rm -rf $name

cp cosmic-rpms/$path_to_spec .

rm -rf cosmic-rpms

current_date=$(date +'%Y%m%d.%H')

sed -i "/^Version:    / s/.*/Version: $version~$current_date.$short_commit/" $name.spec
"""
    with open(f'{specinfo["name"]}/srpm.sh', 'w') as f:
        f.write(scr)

def make_makefile(specinfo):
    mkf = f"""srpm:
    sudo dnf install -y rustc cargo git
    . build.sh"""
    with open(f'{specinfo["name"]}/.spec/Makefile', 'w') as f:
        f.write(mkf)

for app in BUILD_APPS:
    subprocess.run(f"mkdir -p {app["name"]}", shell=True)
    make_spec(app)
    make_build_srpm_script(app)

for etc in BUILD_ETC:
    subprocess.run(f"mkdir -p {etc["name"]}", shell=True)
    make_spec(etc)
    # make_simple_srpm(etc)