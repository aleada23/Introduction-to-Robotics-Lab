#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleControlNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.pose_subscriber_=self.create_subscription(Pose,"/turtle1/pose", self.pose_callback, 10)
        self.cmd_vel_publisher_=self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.get_logger().info("Turtle controller has been started.")


    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if pose.x < 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
