import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_tb3_gazebo = get_package_share_directory('turtlebot3_gazebo')

    env_vars = [SetEnvironmentVariable('LIBGL_ALWAYS_SOFTWARE', '1'), SetEnvironmentVariable('GAZEBO_AUDIO_DEVICE', 'none')]

    gzserver = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')))
    gzclient = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')))
    
    #Spawn Robot
    model_path = os.path.join(pkg_tb3_gazebo, 'models', 'turtlebot3_burger', 'model.sdf')
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'burger', '-file', model_path, '-x', '0.0', '-y', '0.0'],
        output='screen')

    #Spawn a world
    walls_path = os.path.join(pkg_tb3_gazebo, 'models', 'turtlebot3_dqn_world/inner_walls', 'model.sdf')
    
    spawn_walls = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'walls', '-file', walls_path, '-x', '1.5', '-y', '0.0', '-z', '0.0'],
        output='screen')

    obs_path = os.path.join(pkg_tb3_gazebo, 'models', 'turtlebot3_dqn_world/obstacle1', 'model.sdf')
    
    spawn_obs = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'obs', '-file', obs_path, '-x', '1.5', '-y', '0.0', '-z', '0.0'],
        output='screen')
    
    return LaunchDescription(env_vars + [gzserver, gzclient, spawn_robot, spawn_walls, spawn_obs])
