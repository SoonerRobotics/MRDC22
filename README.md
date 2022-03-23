# MRDC22 ![GitHub](https://img.shields.io/github/license/SoonerRobotics/MRDC22?color=%23841617&style=flat-square)

Software for the 2022 [Midwest Robotics Design Competition](https://mrdc.ec.illinois.edu/)

<!-- ## Stack
 - [ROS2 Foxy](https://docs.ros.org/en/foxy/index.html)
 - Ubuntu 20.04 -->

## Building and Setup

```shell
# Run these from the base MRDC directory
# If you get a permission error, run: chmod u+x scripts/build.sh
./scripts/build.sh
source mrdc_ws/install/setup.sh
```

## Launching

### All In One

```shell
ros2 launch mrdc_launch primary.xml
```

### Remote Only

```shell
ros2 launch mrdc_launch remote.xml
```

### GUI Only

```shell
ros2 launch mrdc_launch gui.xml
```

### GUI and Remote

```shell
ros2 launch mrdc_remote remote_gui.xml
```

### Arduino Only

```shell
ros2 launch mrdc_launch serial.xml
```

## VSCode Intellisense Fixes

When using VSCode to edit this project, you may find the custom ROS2 messages have no types. A solution to this problem is to source the install file and then open VSC via the console.

```shell
# This is taking place from the root of the project (MRDC22) NOT (MRDC/mrdc_ws)
# If you have not built before, run the building step above

source mrdc_ws/install/setup.sh
code .
```