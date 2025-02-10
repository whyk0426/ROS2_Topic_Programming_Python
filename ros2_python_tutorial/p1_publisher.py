import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.fast_publisher_ = self.create_publisher(String, 'fast_topic', 10)
        fast_timer_period = 0.5  
        self.timer = self.create_timer(fast_timer_period, self.fast_timer_callback)
        self.i = 0

        self.slow_publisher_ = self.create_publisher(String, 'slow_topic', 10)
        slow_timer_period = 1  
        self.timer = self.create_timer(slow_timer_period, self.slow_timer_callback)
        self.j = 0

    def fast_timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.fast_publisher_.publish(msg)
        self.get_logger().info('[Fast] Publishing: "%s"' % msg.data)
        self.i += 1

    def slow_timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.j
        self.slow_publisher_.publish(msg)
        self.get_logger().info('[Slow] Publishing: "%s"' % msg.data)
        self.j += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()