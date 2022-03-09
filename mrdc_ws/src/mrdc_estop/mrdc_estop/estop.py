import rclpy
import time
from std_msgs.msg import Bool

node = None
subscriber = None

def onEStopMessage(d: Bool):
    print(d)


def main(args=None):
    global node, publisher

    time.sleep(4)

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_estop')
    node.create_subscription(Bool, '/mrdc/estop', lambda msg: onEStopMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()