import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.fast_subscription = self.create_subscription(
            String,
            'fast_topic',
            self.fast_listener_callback,
            10)
        self.fast_subscription 

        self.slow_subscription = self.create_subscription(
            String,
            'slow_topic',
            self.slow_listener_callback,
            10)
        self.slow_subscription 

    def fast_listener_callback(self, msg):
        self.get_logger().info('[Fast] I heard: "%s"' % msg.data)

    def slow_listener_callback(self, msg):
        self.get_logger().info('[Slow] I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()