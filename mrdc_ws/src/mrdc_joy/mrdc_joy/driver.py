import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from std_msgs.msg import String


node = None
publisher = None

def onMessage(d: Joy):
    global node, publisher

    msg = String()
    msg.data = str(round(d.axes[1] * 255)) + "," + str(round(d.axes[4] * 255))
    publisher.publish(msg);

def main(args=None):
    global node, publisher 
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_subscriber')
    publisher = node.create_publisher(String, '/mrdc/joy', 20)
    subscription = node.create_subscription(Joy, '/joy', lambda msg: onMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()