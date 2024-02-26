#!/bin/bash -x

# Copyright ryanabx 2024
git clone --recurse-submodules https://github.com/ryanabx/cosmic-rpms
cd cosmic-rpms/$COPR_PACKAGE
. ./srpm.sh