#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class GazeboController(Node):

    def __init__(self):
        super().__init__("gazebo_controller")
        # In Gazebo/Real Robots, feedback comes from /odom
        self.odom_sub = self.create_subscription(Odometry, "/odom", self.odom_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.get_logger().info("Gazebo Velocity Controller Started.")

    def odom_callback(self, msg: Odometry):
        # Extract X and Y from the Pose part of the Odometry message
        curr_x = msg.pose.pose.position.x
        curr_y = msg.pose.pose.position.y
        
        cmd = Twist()
        
        # Simple Logic
        if abs(curr_x) > 2.0 or abs(curr_y) > 2.0:
            cmd.linear.x = 0.2   # Slow down for the turn
            cmd.angular.z = 0.5  # Turn back toward center
        else:
            cmd.linear.x = 0.5   # Cruise speed
            cmd.angular.z = 0.0
            
        self.cmd_pub.publish(cmd)
        self.get_logger().info(f"Curr_x: {curr_x}, Curr_y: {curr_y}")

def main(args=None):
    rclpy.init(args=args)
    node = GazeboController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
