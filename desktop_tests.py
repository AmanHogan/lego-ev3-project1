
import unittest
from rmath import kinematics as kn
from planning import path_planner as plan
from globals.globals import *

class TestPathPlanner(unittest.TestCase):
    def test_path_planning(self):
        path_found = plan.start_path_planning()

class TestKinnematics(unittest.TestCase):

    def test_kinematics(self):
        transformations = [('T', START_POSITION[0], START_POSITION[1]), ('R',90), ('R',90), ('R',90), ('R',90) ] 
        print("List of Transformations", transformations)
        print("-----------------------")
        print(transformations)

        print("Resultant matrix from transformations ... ", transformations)
        print("-----------------------")
        r_matrix = kn.transforms_to_matrix(transformations)
        kn.print_matrix(r_matrix)
        print("------------------------")

        # Get x, y, and orientation
        x_val = r_matrix[0][2]  
        y_val = r_matrix[1][2] 
        result_orientation = kn.get_orientation(r_matrix)
        print("Final Position (x, y):", round(x_val, 4), round(y_val, 4))
        print("Final Orientation (degrees):", result_orientation)

class TestCommandConversion(unittest.TestCase):

    def test_command_conversion(self):
        transformations = [('T', START_POSITION[0], START_POSITION[1]), ('R',90), ('R',90), ('R',90), ('R',90) ] 
        print("Converting transformations to executable commands ... ", transformations)
        print("-----------------------")
        commands = kn.transformation_to_commands(transformations)
        kn.print_commands(commands)

if __name__ == '__main__':
    print("-------------------- Start --------------------------")
    print("Running Tests running...")
    print("-----------------------")
    unittest.main()
    print("--------------------  End  --------------------")
