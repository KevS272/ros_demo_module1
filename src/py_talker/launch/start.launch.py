from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_talker',
            executable='talker',
            name='talker',
            output='screen'
        ),
        Node(
            package='py_listener',
            executable='listener',
            name='listener',
            output='screen'
        ),
    ])