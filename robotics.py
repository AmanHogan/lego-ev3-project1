from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait, StopWatch, DataLog
from globals import *
import kinematics as kn
import micro_numpy as np


##################################################
# robotuic : Acts as a replacement 
# for pybricks.robotics module. Contains classes 
# for movement and navigation
# 10/17/2023
##################################################

######################################### Navigation class ############################################

class Navigator:
    """Class responsible for keeping track of where the robot is currently at.
    Uses transformation matricies to keep track of orientation and position
    """

    def __init__(self, transforms):

        # TODO: Create a variable that takes in the origin of the robot
        # and sets x, y, and orientation equal to that value

        self.transforms = transforms # sequence of transforms. EX: [('T', 1000, 0), ('R', 90)]
        self.matrix = [] # 2D matrix
        self.matricies = [] # list of 2D matricies
        self.matrix_count = 1
        self.x_val= START_POSITION[0] # current x position [mm]
        self.y_val = START_POSITION[1] # current y position [mm]
        self.orien = 0 # current orientation [deg]
        # print(self.transforms)

    def update(self) -> None:
        """Updates the logical position of the robot and keeps track of previous positions
        """
        # First matrix
        if self.matrix_count == 1:
            self.matrix = kn.transforms_to_matrix([self.transforms.pop(0)]) # convert transform to matrix format

        # Every matrix after the first
        else:
            # Dot product of matricies
            # T (i->j) = T(i) * T(j)
            self.matrix = np.dot(self.matrix, kn.transforms_to_matrix([self.transforms.pop(0)]))

        self.matricies.append(self.matrix) # add to list of matricies
        
        print("Matrix:", "(", self.matrix_count, ")")
        kn.print_matrix(self.matrix)
        
        self.x_val = self.matrix[0][2] # x
        self.y_val = self.matrix[1][2] # y
        self.orien = kn.get_orientation(self.matrix) # orientation

        print("Position (x, y):", self.x_val, "," , self.y_val)
        print("Orientation (degrees):", self.orien)

        self.matrix_count +=1

######################################### Robot class ############################################

class Robot:
    """Custom defined Robot class for the lego ev3 robot. Responsible for moving and turning the robot.
    """
    def __init__(self, left_motor: Motor, right_motor: Motor, navigator: Navigator):
        self.left_motor = left_motor # controls left tire
        self.right_motor = right_motor # controls right tire
        self.navigator = navigator # object to keep track of robot position
    
    def move(self, distance) -> None:
        """Moves robot a given distance in [mm]

        Args:
            distance (float): Distance to be traveled [mm]
        """
        self.navigator.update() # notify naviagator

        # Angle [deg] = (distance [mm] / circum [mm]) * 360 [deg]
        # Rotate tires by the calculated amount
        angle =  ((distance) / TIRE_CIRCUMFERENCE) * FULL_ROTATION
        angle = angle * ERROR_FACTOR_DISTANCE
        
        # Turn tires
        self.left_motor. run_angle(TIRE_RPM, angle, wait=False)
        self.right_motor.run_angle(TIRE_RPM, angle)


    def turn(self, angle) -> None:
        """Turns robot a given angle [deg]

        Args:
            angle (float): angle to turn robot [deg]
        """
        self.navigator.update() # notify naviagtor
        
        # Calculate the angle needed to rotate the robot to be in the specified angle
        arc_length = 2 * M_PI * ROBOT_RADIUS_MM * (angle/360)
        new_angle =  ((arc_length) / TIRE_CIRCUMFERENCE) * FULL_ROTATION
        new_angle =  new_angle * ERROR_FACTOR_TURN
        
        # Turn tires
        self.left_motor. run_angle(TIRE_RPM, -new_angle, wait=False)
        self.right_motor.run_angle(TIRE_RPM, new_angle)

    
    def execute_commands(self, robot_commands) -> None:
        """ Takes a list of commands in format ('move', <float>) or ('turn', <float>)
        Then executes these commands one-by-one

        Args:
            robot_commands (list[tuple[str, float]]): list of commands 
            in format ('move', <float>) or ('turn', <float>)
        """
        for command in robot_commands:
            action, value = command
            if action == 'move':
                self.move(value)
            elif action == 'turn':
                self.turn(value)

############################################################################################
