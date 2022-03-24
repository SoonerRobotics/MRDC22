import rclpy
import serial
import time
import bson

from std_msgs.msg import Bool
from mrdc_msgs.msg import Motors

node = None
subscriber = None
estop_subscriber = None
isForceStopped = False

# Drive Train Arduino
train_serial = serial.Serial("/dev/ttyUSB1", baudrate=115200)

# Arm Arduino
ball_serial = serial.Serial("/dev/ttyUSB0", baudrate=115200)


def onSerialMessage(d: Motors):
    global node, subscriber, isForceStopped

    if isForceStopped:
        return

    obj = {
        "cmd": 0x01,
        "left_motor": d.left_motor,
        "right_motor": d.right_motor
    }
    train_serial.write(bson.BSON.encode(obj))

    obj = {
        "cmd": 0x02,
        "elevator_motor": d.elevator_motor,
        "intake_motor": d.intake_motor,
        "launcher_motor": d.launcher_motor
    }
    ball_serial.write(bson.BSON.encode(obj))


def onEStopSignal(d: Bool):
    global isForceStopped
    isForceStopped = d.data


def main(args=None):
    global node, publisher

    time.sleep(4)

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_serial')
    node.create_subscription(
        Motors, '/mrdc/serial', lambda msg: onSerialMessage(msg), 20
    )
    node.create_subscription(
        Bool, '/mrdc/estop', lambda msg: onEStopSignal(msg), 20
    )

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
