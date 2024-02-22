#!/bin/bash

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='cosmic-app-library'
version='0.1.0'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='rust2rpmspecs/cosmic-app-library.spec'
pop_repo='cosmic-applibrary'

LATEST="latest"

# Commit to target. Use "latest" if you want master
commit="latest"

if [[ "$commit" == "$LATEST" ]]
then
    latest_commit=$(curl -s "https://api.github.com/repos/pop-os/$pop_repo/commits/master" | grep -oP -m 1 '"sha": "\K[^"]+')

    echo "Latest commit SHA: $latest_commit"
    commit=$latest_commit
fi

short_commit=${commit:0:6}

git clone --recurse-submodules https://github.com/pop-os/$pop_repo.git

cd $pop_repo && git reset --hard $commit

cargo vendor deps

tar -cJf $name-vendor.tar.xz deps && mv $name-vendor.tar.xz ../$name-vendor.tar.xz

rm -rf deps && cd ..

rm -rf $pop_repo

wget https://github.com/pop-os/$pop_repo/archive/$commit/${name}.tar.gz

git clone $repo

cp cosmic-rpms/$path_to_spec .

rm -rf cosmic-rpms

current_date=$(date +'%Y%m%d')

sed -i "/^Version:    / s/.*/Version: $version~$current_date.$short_commit/" $name.spec
sed -i "/^%global commit/ s/.*/%global commit $commit/" $name.spec
sed -i "/^%autosetup s/.*/%autosetup -n $pop_repo-$commit -p1 -a1
