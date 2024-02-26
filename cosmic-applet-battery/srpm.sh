#!/bin/bash -x

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='cosmic-applet-battery'
version='0.1.0'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='cosmic-applet-battery/cosmic-applet-battery.spec'
pop_repo='cosmic-applets'

# Commit to target. Use "latest" if you want master
commit="latest"

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
short_commit=${commit:0:6}

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
