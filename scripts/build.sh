#!/bin/bash

cd ./mrdc_ws

colcon build --symlink-install

source install/setup.sh
