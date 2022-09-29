import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'skew_urdf'
    file_subpath = 'urdf/robot.urdf.xacro'


    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    #print(xacro_file)
    robot_description_raw = xacro.process_file(xacro_file).toxml()
    # Write urdf created from xacro to file
    path = get_package_share_directory(pkg_name)
    final_ur_path = os.path.join(path, 'urdf_compiled')
    os.mkdir(final_ur_path)
    f = open(os.path.join(final_ur_path, 'skew.urdf'), 'w')
    f.write(robot_description_raw)
    f.close()

    # Run the node
    return LaunchDescription([
    ])