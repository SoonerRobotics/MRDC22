import rclpy
from sensor_msgs.msg import Joy
from mrdc_msgs.msg import Motors


node = None
publisher = None


def onMessage(d: Joy):
    global node, publisher

    # If you are getting weird motor values, this is the first place to look. I have had the below axes switch up on me before
    msg = Motors()

    # The 0.3 below is a programmatic speed limiter, change if needed
    msg.left_motor = d.axes[1] * -0.3
    msg.right_motor = d.axes[4] * 0.3
    msg.trigger_motor = 0.0 if d.axes[5] >= 0 else -(d.axes[5] * 1.5)
    publisher.publish(msg)


def main(args=None):
    global node, publisher
    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_joy')
    publisher = node.create_publisher(Motors, '/mrdc/joy', 20)
    node.create_subscription(Joy, '/joy', lambda msg: onMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
