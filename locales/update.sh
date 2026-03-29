#!/bin/sh
# update transifex pot files

set -ex

cd $(dirname $0)
# Initialize submodule if not already initialized
git submodule update --init --recursive
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -D plot_gallery=0 -b gettext ../scientific-python-lectures pot
