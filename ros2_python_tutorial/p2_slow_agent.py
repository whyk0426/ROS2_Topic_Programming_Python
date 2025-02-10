import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('slow_agent')
        self.slow_publisher_ = self.create_publisher(String, 'slow_topic', 10)
        slow_timer_period = 1  
        self.timer = self.create_timer(slow_timer_period, self.slow_timer_callback)
        self.j = 0

        self.fast_subscription = self.create_subscription(
            String,
            'fast_topic',
            self.fast_listener_callback,
            10)
        self.fast_subscription 

    def slow_timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.j
        self.slow_publisher_.publish(msg)
        self.get_logger().info('[Slow] Publishing: "%s"' % msg.data)
        self.j += 1
    
    def fast_listener_callback(self, msg):
        self.get_logger().info('[Fast] I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    slow_agent = MinimalPublisher()
    rclpy.spin(slow_agent)
    slow_agent.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()