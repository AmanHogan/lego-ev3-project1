from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait, StopWatch, DataLog
import math
import kinematics as kn
import micro_numpy as np

######################################### Navigation class ############################################

class Navigator:
    """Class responsible for keeping track of where the robot is currently at.
    Uses transformation matricies to keep track of orientation and position
    """

    def __init__(self, transforms: list[tuple[str, float]] | list[tuple[str, float]]):

        # TODO: Create a variable that takes in the origin of the robot
        # and sets x, y, and orientation equal to that value

        self.transforms = transforms # sequence of transforms. EX: [('T', 1000, 0), ('R', 90)]
        self.matrix = [] # 2D matrix
        self.matricies = [] # list of 2D matricies
        self.matrix_count = 1
        self.x_val= 0 # current x position [mm]
        self.y_val = 0 # current y position [mm]
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

    ##### Constants #####
    TIRE_CIRC = 178 # Circumference of the tire in [mm]
    FULL_ROTATION = 360 
    RPM = 400 # Revolutions per minute [r/min]
    ROBOT_LENGTH = 105 # Length of the robot in [mm]
    DIST_BTWN_WHEELS = 160 # Distance between the wheels in [mm]
    ROBOT_RADIUS = (DIST_BTWN_WHEELS/2) # Radius of robot tire axel [mm]
    M_PI = 3.14159265359 
    ##### Constants #####

    def __init__(self, left_motor: Motor, right_motor: Motor, navigator: Navigator):
        self.left_motor = left_motor # controls left tire
        self.right_motor = right_motor # controls right tire
        self.navigator = navigator # object to keep track of robot position
    
    def move(self, distance:float) -> None:
        """Moves robot a given distance in [mm]

        Args:
            distance (float): Distance to be traveled [mm]
        """
        self.navigator.update() # notify naviagator

        # Angle [deg] = (distance [mm] / circum [mm]) * 360 [deg]
        # Rotate tires by the calculated amount
        angle =  (distance / Robot.TIRE_CIRC) * Robot.FULL_ROTATION

        # Turn tires
        self.left_motor. run_angle(Robot.RPM, angle, wait=False)
        self.right_motor.run_angle(Robot.RPM, angle)
    
    def turn(self, angle: float) -> None:
        """Turns robot a given angle [deg]

        Args:
            angle (float): angle to turn robot [deg]
        """

        self.navigator.update() # notify naviagtor
        
        # Calculate the angle needed to rotate the robot to be in the specified angle
        arc_length = 2 * Robot.M_PI * Robot.ROBOT_RADIUS * (angle/360)
        new_angle =  (arc_length / Robot.TIRE_CIRC) * Robot.FULL_ROTATION

        # Turn tires
        self.left_motor. run_angle(Robot.RPM, -new_angle, wait=False)
        self.right_motor.run_angle(Robot.RPM, new_angle)
    
    def execute_commands(self, robot_commands: list[tuple[str, float]]) -> None:
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
