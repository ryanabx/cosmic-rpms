import cosmic_apps

SPEC_FOLDER = "SPECS"
BUILD_SCRIPTS_FOLDER = "BUILD_SCRIPTS"

BUILD_APPS = [
    cosmic_apps.COSMIC_APP_LIBRARY,
    cosmic_apps.COSMIC_APPLETS
]

def make_spec(specinfo):
    spec = f"""
# Generated by specgen.py ryanabx
{specinfo["globals"]}
# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

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

    with open(f'{SPEC_FOLDER}/{specinfo["name"]}.spec', 'w') as f:
        f.write(spec)

def make_build_srpm_script(specinfo):
    scr = f"""
#!/bin/bash -x

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='{specinfo["name"]}'
version='{specinfo["version"]}'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='{SPEC_FOLDER}/{specinfo["name"]}.spec'
pop_repo='{specinfo["reposhort"]}'

# Commit to target. Use "latest" if you want master
commit="{specinfo["commit"]}"

# Don't edit anything past this line 
# ===================================================== #

LATEST="latest"

if [[ "$commit" == "$LATEST" ]]
then
    latest_commit=$(curl -s "https://api.github.com/repos/pop-os/$pop_repo/commits/master" | grep -oP -m 1 '"sha": "\\K[^"]+')

    echo "Latest commit SHA: $latest_commit"
    commit=$latest_commit
fi

short_commit=${{commit:0:6}}

git clone --recurse-submodules https://github.com/pop-os/$pop_repo

cd $pop_repo && git reset --hard $commit

mkdir .vendor

cargo vendor > .vendor/config.toml

tar -cJf $name-vendor.tar.xz vendor && mv $name-vendor.tar.xz ../$name-vendor.tar.xz

rm -rf vendor && cd ..

ls

mv $pop_repo $name

tar -czf $name.tar.gz $name

rm -rf $name

git clone $repo

cp cosmic-rpms/$path_to_spec .

rm -rf cosmic-rpms

current_date=$(date +'%Y%m%d')

sed -i "/^Version:    / s/.*/Version: $version~$current_date.$short_commit/" $name.spec
"""
    with open(f'{BUILD_SCRIPTS_FOLDER}/{specinfo["name"]}.sh', 'w') as f:
        f.write(scr)

for app in BUILD_APPS:
    make_spec(app)
    make_build_srpm_script(app)
