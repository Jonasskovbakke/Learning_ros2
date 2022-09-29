from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("robot", package_name="skew_srdf").to_moveit_configs()
    return generate_demo_launch(moveit_config)
