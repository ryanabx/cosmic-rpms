#!/bin/bash -x

git clone --recurse-submodules https://github.com/ryanabx/cosmic-rpms

cd cosmic-rpms/$COPR_PACKAGE

. ./srpm.sh