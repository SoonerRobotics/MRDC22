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
sudo install/setup.sh
```

## Launching

```shell
ros2 launch mrdc_launch primary.xml
```