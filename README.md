# MRDC22

Software for the 2022 [Midwest Robotics Design Competition](https://mrdc.ec.illinois.edu/)

## Stack
 - [ROS2 Foxy](https://docs.ros.org/en/foxy/index.html)
 - Ubuntu 20.04

## Building

```shell
cd mrdc_ws
colcon build
```

## Setup

```shell
source install/setup.sh
```

## Launching

```shell
ros2 launch mrdc_launch primary.xml
```

## VSCode Intellisense Fixes

When using VSCode to edit this project, you may find the custom ROS2 messages have no types. A solution to this problem is to source the install file and then open VSC via the console.

```shell
# This is taking place from the root of the project (MRDC22) NOT (MRDC/mrdc_ws)

source mrdc_ws/install/setup.sh
code .
```