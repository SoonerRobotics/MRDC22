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

To run the ardunio code purely on the robot, use the following:
```shell
ros2 launch mrdc_launch serial.xml
```

To run the ardunio code purely on the robot with the gui, use the following:
```shell
ros2 launch mrdc_serial serialwithgui.xml
```

To run the remote code (typically the remote computer), use the following:
```shell
ros2 launch mrdc_launch remote.xml
```

If you are running everything on one computer, use the following:
```shell
ros2 launch mrdc_launch primary.xml
```

## VSCode Intellisense Fixes

When using VSCode to edit this project, you may find the custom ROS2 messages have no types. A solution to this problem is to source the install file and then open VSC via the console.

```shell
# This is taking place from the root of the project (MRDC22) NOT (MRDC/mrdc_ws)
# If you have not built before, run the building step above

source mrdc_ws/install/setup.sh
code .
```

## Controls

For the drivetrain, use the left and right thumbsticks  
For the launcher, elevator and intake use the X, Y and B buttons

## GUI Website URL
The website is hosted locally at: http://127.0.0.1:5000