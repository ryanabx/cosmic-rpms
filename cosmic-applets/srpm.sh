#!/bin/bash -x

# Variables. LOOK CLOSELY AND MAKE SURE THESE ARE CORRECT

name='cosmic-applets'
version='0.1.0'

repo='https://github.com/ryanabx/cosmic-rpms'
path_to_spec='cosmic-applets/cosmic-applets.spec'

cd ../..
# We should be in the base directory now

cp cosmic-rpms/$path_to_spec .

rm -rf cosmic-rpms

current_date=$(date +'%Y%m%d')

sed -i "/^Version:    / s/.*/Version: $version~$current_date/" $name.spec
