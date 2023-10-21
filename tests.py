
import unittest
from rmath import kinematics as kn
from planning import path_planner as plan
from globals.globals import *




class TestPathPlanner(unittest.TestCase):


    
    def test_path_planning(self):

        path_found = None
        transforamtions = None
        commands = None

        path_found = plan.start_path_planning()
        
        commands = kn.calculates_positions(path_found)
        print("List of commands")
        print(commands)
        print("-----------------------")


        transformations = kn.commands_to_transformations(commands)
        print("List of Transformations")
        print("-----------------------")
        print(transformations)
    

if __name__ == '__main__':
    print("-------------------- Start --------------------------")
    print("Running Tests running...")
    print("-----------------------")
    unittest.main()
    print("--------------------  End  --------------------")
