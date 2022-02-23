import rclpy
import serial
import time
import json

from mrdc_msgs.msg import Motors

node = None
subscriber = None

# Drive Train Arduino
dt_serial = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Arm Arduino
arm_serial = serial.Serial("/dev/ttyUSB1", baudrate=115200)

def onSerialMessage(d: Motors):
    global node, subscriber
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


def main(args=None):
    global node, publisher

    time.sleep(4)

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_serial')
    node.create_subscription(
        Motors, '/mrdc/serial', lambda msg: onSerialMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

    dt_serial.close()
    arm_serial.close()


if __name__ == '__main__':
    main()