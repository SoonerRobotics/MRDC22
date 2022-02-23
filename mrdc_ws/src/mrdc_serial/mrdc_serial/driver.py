import rclpy
import serial
import time
import json

from mrdc_msgs.msg import Motors

node = None
subscriber = None

drive_train = serial.Serial("/dev/ttyUSB0", baudrate=115200)
arm = serial.Serial("/dev/ttyUSB1", baudrate=115200)

def onMessage(d: Motors):
    global node, subscriber
    obj = {
        "left_motor": d.left_motor,
        "right_motor": d.right_motor,
    }
    drive_train.write(json.dumps(obj).encode())

    arm_obj = {
        "left_motor": d.trigger_motor,
        "right_motor": 0,
    }
    arm.write(json.dumps(arm_obj).encode())


def main(args=None):
    global node, publisher

    time.sleep(4)

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_serial')
    node.create_subscription(
        Motors, '/mrdc/joy', lambda msg: onMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
