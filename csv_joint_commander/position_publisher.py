#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import pandas as pd
import numpy as np
import os

class PositionPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')
        
        # Parameters
        self.declare_parameter('rate', 10.0)
        self.declare_parameter('csv_file', '')
        
        # Get parameters
        rate = float(self.get_parameter('rate').value)
        csv_file = self.get_parameter('csv_file').value
        
        # Set CSV path
        if not csv_file:
            home = os.path.expanduser("~")
            csv_file = os.path.join(home, 'Desktop', 'demo_pickup.csv')
        
        # Load CSV
        self.data = pd.read_csv(csv_file)
        self.data.columns = self.data.columns.str.strip()
        
        # Auto-detect joints
        self.joint_names = [col for col in self.data.columns if 'joint' in col.lower()]
        if not self.joint_names:
            self.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
        
        # Publisher
        self.publisher = self.create_publisher(Float64MultiArray, '/position_controller/commands', 10)
        
        # Timer
        timer_period = 1.0 / rate
        self.timer = self.create_timer(timer_period, self.publish_frame)
        
        self.current_frame = 0
        
        self.get_logger().info(f"Ready: {len(self.data)} frames at {rate}Hz")
    
    def publish_frame(self):
        if self.current_frame >= len(self.data):
            self.current_frame = 0
        
        row = self.data.iloc[self.current_frame]
        positions = []
        
        for joint in self.joint_names:
            if joint in row.index:
                deg = float(row[joint])
                rad = deg * np.pi / 180.0
                positions.append(rad)
            else:
                positions.append(0.0)
        
        msg = Float64MultiArray()
        msg.data = positions
        self.publisher.publish(msg)
        
        if self.current_frame % 10 == 0:
            self.get_logger().info(f"Frame {self.current_frame}")
        
        self.current_frame += 1

def main():
    rclpy.init()
    node = PositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
