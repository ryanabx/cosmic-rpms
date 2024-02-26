#!/bin/bash -x

PACKAGE=

# Copyright ryanabx 2024
git clone --recurse-submodules https://github.com/ryanabx/cosmic-rpms
cd cosmic-rpms/$PACKAGE
. ./srpm.sh