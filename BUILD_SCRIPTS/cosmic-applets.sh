#!/bin/bash -x

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='cosmic-applets'
version='0.1.0'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='SPECS/cosmic-applets.spec'
pop_repo='cosmic-applets'

# Commit to target. Use "latest" if you want master
commit="latest"

# Don't edit anything past this line 
# ===================================================== #

LATEST="latest"

if [[ "$commit" == "$LATEST" ]]
then
    latest_commit=$(curl -s "https://api.github.com/repos/pop-os/$pop_repo/commits/master" | grep -oP -m 1 '"sha": "\K[^"]+')

    echo "Latest commit SHA: $latest_commit"
    commit=$latest_commit
fi

short_commit=${commit:0:6}

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
