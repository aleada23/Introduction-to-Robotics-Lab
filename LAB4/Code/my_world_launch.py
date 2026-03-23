import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    #Path to the Gazebo Launch
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_tb3_gazebo = get_package_share_directory('turtlebot3_gazebo')

    #Include the Gazebo Server
    gzserver = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')))

    #Include the Gazebo Client (The GUI)
    gzclient = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')))
    
    #Robot Spawner
    model_path = os.path.join(
    get_package_share_directory('turtlebot3_gazebo'),
    'models', 'turtlebot3_burger', 'model.sdf')
    spawn_robot = Node(
    package='gazebo_ros',
    executable='spawn_entity.py',
    arguments=[
        '-entity', 'burger',
        '-file', model_path, 
        '-x', '0.0', '-y', '0.0', '-z', '0.01'],output='screen')
    
    return LaunchDescription([gzserver, gzclient, spawn_robot])
