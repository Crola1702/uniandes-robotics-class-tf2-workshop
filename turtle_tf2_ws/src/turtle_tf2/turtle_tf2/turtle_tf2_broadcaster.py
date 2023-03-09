import math

import numpy as np
import rclpy
import tf_transformations # Requires `python3 -m pip install transforms3d`

from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose

def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = math.cos(ai)
    si = math.sin(ai)
    cj = math.cos(aj)
    sj = math.sin(aj)
    ck = math.cos(ak)
    sk = math.sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss

    return q
class TurtleFramePublisher(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_publisher')

        # Declare and acquire `turtlename` parameter
        self.turtlename = self.declare_parameter('turtlename', 'turtle').get_parameter_value().string_value

        # TODO: Initialize the transform broadcaster calling `TransformBroadcaster` on this Node
        self.tf_broadcaster = ...
        

        # We will use the subscription to get the pose of the turtle to broadcast the transform
        # TODO: Create a subscriber to '/{turtlename}/pose'
        # Use `Pose` as msg type and `turtle_pose_cb` as callback function
        ...
        

        self.get_logger().info(f'{self.get_name()} has been started')
        self.get_logger().info(f'Publishing {self.turtlename} transform')
        
    def turtle_pose_cb(self, msg):
        t = TransformStamped() # Create a TransformStamped message object

        t.header.stamp = self.get_clock().now().to_msg() # Set the time stamp to the current time
        t.header.frame_id = 'world' # Set the parent frame of the transform
        t.child_frame_id = self.turtlename # Set the child frame of the transform

        # TODO: Set the translation of the transform with `t.transform.translation`
        ...
        



        # Set the rotation of the transform
        # TODO: Set the rotation of the transform with `t.transform.rotation`
        # q = [x, y, z, w]
        q = tf_transformations.quaternion_from_euler(0, 0, msg.theta)  # Get the orientation of the turtle as a quaternion
        ...
        

        # TODO: Send the transform via `tf_broadcaster`
        ...
        

def main(args=None):
    rclpy.init(args=args)
    node = TurtleFramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
    
