import rclpy
import serial
import time
import json

from std_msgs.msg import Bool
from mrdc_msgs.msg import Motors

node = None
subscriber = None
estop_subscriber = None
isForceStopped = False

# Drive Train Arduino
dt_serial = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Arm Arduino
arm_serial = serial.Serial("/dev/ttyUSB1", baudrate=115200)


def onSerialMessage(d: Motors):
    global node, subscriber, isForceStopped

    if isForceStopped:
        return

    obj = {
        "left_motor": d.left_motor,
        "right_motor": d.right_motor,
    }
    dt_serial.write(json.dumps(obj).encode())

    arm_obj = {
        "left_motor": d.trigger_motor,
        "right_motor": 0,
    }
    arm_serial.write(json.dumps(arm_obj).encode())


def onEStopSignal(d: Bool):
    global isForceStopped
    isForceStopped = d


def main(args=None):
    global node, publisher

    time.sleep(4)

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_serial')
    subscriber = node.create_subscription(
        Motors, '/mrdc/serial', lambda msg: onSerialMessage(msg), 20
    )
    estop_subscriber = node.create_subscription(
        Bool, '/mrdc/estop', lambda msg: onEStopSignal(msg), 20
    )

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

    dt_serial.close()
    arm_serial.close()


if __name__ == '__main__':
    main()
