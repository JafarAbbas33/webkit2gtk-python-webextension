#! /bin/sh
#
# run.sh
# Copyright (C) 2015 Adrian Perez <aperez@igalia.com>
#
# Distributed under terms of the MIT license.
#
make
export PYTHONPATH=$(pwd)
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libpython3.8.so
./browse-with-extension
