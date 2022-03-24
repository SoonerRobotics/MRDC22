import rclpy
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool
from mrdc_msgs.msg import Motors


node = None
publisher = None
estop_publisher = None


def onJoyMessage(d: Joy):
    global node, publisher, estop_publisher

    # if d.buttons[0] >= 1:
    #     msg = Bool()
    #     msg.data = True
    #     estop_publisher.publish(msg)
    #     return

    msg = Motors()
    msg.left_motor = d.axes[4] * 0.4
    msg.right_motor = d.axes[1] * 0.4
    msg.elevator_motor = d.buttons[3] * 0.9 + 1/255
    msg.intake_motor = d.buttons[1] * 0.15 + 1/255
    msg.launcher_motor = d.buttons[2] * 0.2 + 1/255
    publisher.publish(msg)


def main(args=None):
    global node, publisher, estop_publisher
    rclpy.init(args=args)

    # Create node and listen to joy
    node = rclpy.create_node('mrdc_remote')
    node.create_subscription(Joy, '/joy', lambda msg: onJoyMessage(msg), 20)

    # Create publisher so we can public to serial
    publisher = node.create_publisher(Motors, '/mrdc/serial', 20)
    estop_publisher = node.create_publisher(Bool, '/mrdc/estop', 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()