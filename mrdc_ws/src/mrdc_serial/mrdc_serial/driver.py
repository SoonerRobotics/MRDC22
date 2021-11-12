# import serial

# import time
# import json
# import math

# arduino = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
# def main(args=None):
#     print("Waiting on arduino connection")
#     time.sleep(4)
#     print("Connected, sending data")
#     while True:
#         speed = math.sin(time.time())
#         obj = {
#             "speed": speed
#         }
#         print(json.dumps(obj).encode())
#         arduino.write(json.dumps(obj).encode())
#         time.sleep(0.1)

#         print(arduino.readline().decode())

# if __name__ == '__main__':
#     main()

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


node = None
subscriber = None

def onMessage(d: String):
    global node, subscriber
    print(d.data)


def main(args=None):
    global node, publisher 
    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_serial_joy')
    subscription = node.create_subscription(String, '/mrdc/joy', lambda msg: onMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()