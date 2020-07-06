import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_robominer_description = get_package_share_directory('robominer_description')

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )

    # RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_robominer_description, 'launch', 'urdf.rviz')],
        condition=IfCondition(LaunchConfiguration('rviz'))
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
             default_value=[os.path.join(pkg_robominer_description, 'worlds', 'robominer.world'), ''],
             description='SDF world file'),
        DeclareLaunchArgument(
            'robominer',
            default_value=[os.path.join(pkg_robominer_description, 'urdf', 'robominer.xacro'), ''],
            description='URDF robot file'),
          gazebo
    ])
    '''
    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(pkg_robominer_description, 'worlds', 'robominer.world'), ''],
          description='SDF world file'),
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),
          gazebo,
          follow,
          rviz
    ])
    '''
    '''
    # Follow node
    follow = Node(
        package='dolly_follow',
        node_executable='dolly_follow',
        output='screen',
        remappings=[
            ('cmd_vel', '/dolly/cmd_vel'),
            ('laser_scan', '/dolly/laser_scan')
        ]
    )
    '''

