import builtins
import rclpy
import time

node = None
subscriber = None

def onEStopMessage(d: builtins.bool):
    print(d)


def main(args=None):
    global node, publisher

    time.sleep(4)

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_estop')
    node.create_subscription(builtins.bool, '/mrdc/estop', lambda msg: onEStopMessage(msg), 20)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()