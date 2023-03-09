import math

from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from turtlesim.srv import Spawn


class TurtleFrameListener(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_listener')

        # Declare and acquire `target_frame` parameter
        self.target_frame = self.declare_parameter('target_frame', 'turtle1').get_parameter_value().string_value

        # TODO: Initialize the transform listener calling `TransformListener` on this Node
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, ...)
        

        # TODO: Create turtle2 velocity publisher
        # Use `geometry_msgs/Twist` as msg type and `turtle2/cmd_vel` as topic name
        self.publisher = ...
        

        # Create a client to spawn a turtle
        self.spawner = self.create_client(Spawn, 'spawn')
        while not self.spawner.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        # Initialize request with turtle name and coordinates
        request = Spawn.Request()
        request.name = 'turtle2'
        request.x = float(4)
        request.y = float(2)
        request.theta = float(0)

        # Call request to spawn turtle

        self.result = self.spawner.call_async(request)
        self.get_logger().info(f'Spawned turtle2!')


        # TODO: Create a timer that will call `self.on_timer` with a period of 1 second
        self.timer = ...
        

    def on_timer(self):

        from_frame_rel = self.target_frame
        to_frame_rel = 'turtle2'

        # Look up for the transformation between target_frame and turtle2 frames
        # and send velocity commands for turtle2 to reach target_frame
        try:
            t = self.tf_buffer.lookup_transform(
                to_frame_rel,
                from_frame_rel,
                rclpy.time.Time())
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}'
            )
            return
        
        msg = Twist()

        # TODO: Fill the angle difference between turtle2 postion and target_frame position
        # Use math.atan2 and translation x and y of the lookup transform
        rotation_rate = 1.0
        angle_diff = ...
        
        msg.angular.z = rotation_rate * angle_diff

        # TODO: Fill the distance difference between turtle2 and target_frame
        # Use math.sqrt and translation x and y of the lookup transform
        forward_speed = 0.5
        distance_diff = ...
        
        msg.linear.x = forward_speed * distance_diff

        # TODO: Publish the message
        ...
        


def main():
    rclpy.init()
    node = TurtleFrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
