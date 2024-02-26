#!/bin/bash -x

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='cosmic-icons'
version='0.1.0'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='SPECS/cosmic-icons.spec'
pop_repo='cosmic-icons'

# Commit to target. Use "latest" if you want master
commit="latest"

# Don't edit anything past this line 
# ===================================================== #

LATEST="latest"

git clone --recurse-submodules https://github.com/pop-os/$pop_repo

if [[ "$commit" == "$LATEST" ]]
then
    commit=$(git rev-parse HEAD)
fi

echo 'the commit is $commit'
short_commit=${commit:0:6}

cd $pop_repo && git reset --hard $commit

cd ..

if [ "$pop_repo" != "$name" ]; then
    mv $pop_repo $name
else
    echo "names are equal. continuing..."
fi

tar -czf $name.tar.gz $name

rm -rf $name

git clone $repo

cp cosmic-rpms/$path_to_spec .

rm -rf cosmic-rpms

current_date=$(date +'%Y%m%d')

sed -i "/^Version:    / s/.*/Version: $version~$current_date.$short_commit/" $name.spec