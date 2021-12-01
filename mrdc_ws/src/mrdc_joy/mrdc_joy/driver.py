import rclpy
from sensor_msgs.msg import Joy
from mrdc_msgs.msg import Motors


node = None
publisher = None


def onMessage(d: Joy):
    global node, publisher

    msg = Motors()
    msg.left_motor = d.axes[1] * 0.3
    msg.right_motor = d.axes[3] * 0.3
    publisher.publish(msg)


def main(args=None):
    global node, publisher
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_subscriber')
    publisher = node.create_publisher(Motors, '/mrdc/joy', 20)
    node.create_subscription(Joy, '/joy', lambda msg: onMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
