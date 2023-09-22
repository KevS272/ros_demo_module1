from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    node_talker = Node(
        package='py_talker',
        executable='talker',
        name='talker',
        output='screen'
    )

    node_listener = Node(
        package='py_listener',
        executable='listener',
        name='listener',
        output='screen'
    )

    foxglove_bridge = IncludeLaunchDescription(
      XMLLaunchDescriptionSource([os.path.join(
         get_package_share_directory('foxglove_bridge'), 'launch'),
         '/foxglove_bridge_launch.xml'])
      )

    return LaunchDescription([
        node_talker,
        node_listener,
        foxglove_bridge,
    ])