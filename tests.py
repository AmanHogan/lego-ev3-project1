
import unittest
from rmath import kinematics as kn
from planning import path_planner as plan
from globals.globals import *

class TestPathPlanner(unittest.TestCase):

    def test_robot_calculations(self):

        path_found = None
        transformations = None
        commands = None

        # Test path planning
        path_found = plan.start_path_planning()
        
        # Test angle calculations
        print("List of Angles")
        angles_list = kn.find_angles_between_positions(path_found)
        angles_list = [round(i,5) for i in angles_list]
        angles_list.pop(0)
        print(angles_list)
        print("-----------------------")

        # Test distance calculations
        print("List of distances")
        distances_list = kn.calculate_distances(path_found)
        distances_list = [round(i,5) for i in distances_list]
        print(distances_list)
        print("-----------------------")

        # Test Robot command generation
        commands = kn.positions_to_commands(path_found)
        print("List of commands")
        print(commands)
        print("-----------------------")

        # Test transformation generation
        transformations = kn.commands_to_transformations(commands)
        print("List of Transformations")
        print(transformations)
        print("-----------------------")

if __name__ == '__main__':
    print("-------------------- Start --------------------------")
    print("Running Tests running...")
    print("-----------------------")
    unittest.main()
    print("--------------------  End  --------------------")