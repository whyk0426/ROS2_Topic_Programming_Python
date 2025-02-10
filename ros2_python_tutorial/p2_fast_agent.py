import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('fast_agent')
        self.fast_publisher_ = self.create_publisher(String, 'fast_topic', 10)
        fast_timer_period = 0.5  
        self.timer = self.create_timer(fast_timer_period, self.fast_timer_callback)
        self.i = 0

        self.slow_subscription = self.create_subscription(
            String,
            'slow_topic',
            self.slow_listener_callback,
            10)
        self.slow_subscription 

    def fast_timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.fast_publisher_.publish(msg)
        self.get_logger().info('[Fast] Publishing: "%s"' % msg.data)
        self.i += 1

    def slow_listener_callback(self, msg):
        self.get_logger().info('[Slow] I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    fast_agent = MinimalPublisher()
    rclpy.spin(fast_agent)
    fast_agent.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()