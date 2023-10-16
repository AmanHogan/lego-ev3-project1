from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
import math
import matricies as kn
import micro_numpy as np

class Robot:

    TIRE_CIRC = 178
    FULL_ROTATION = 360
    RPM = 400
    ROBOT_LENGTH = 105
    DIST_BTWN_WHEELS = 160
    M_PI = 3.14159265359 

    def __init__(self, left_motor, right_motor, navigator):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.navigator = navigator
    
    def move(self, distance):
        self.navigator.update_matrix()
        angle =  (distance / Robot.TIRE_CIRC) * Robot.FULL_ROTATION
        self.left_motor. run_angle(Robot.RPM, angle, wait=False)
        self.right_motor.run_angle(Robot.RPM, angle)
    
    def turn(self, angle):
        self.navigator.update_matrix()
        arc_length = 2 * Robot.M_PI * (Robot.DIST_BTWN_WHEELS/2) * (angle/360)
        new_angle =  (arc_length / Robot.TIRE_CIRC) * Robot.FULL_ROTATION
        self.left_motor. run_angle(Robot.RPM, -new_angle, wait=False)
        self.right_motor.run_angle(Robot.RPM, new_angle)
    
    def execute_commands(self, commands):
        for command in commands:
            action, value = command
            if action == 'move':
                self.move(value)
            elif action == 'turn':
                self.turn(value)

    

class Navigator:
    def __init__(self, obstacles, transformations):
        self.obstacles = obstacles
        self.transformations = transformations
        self.current_matrix = None
        self.list_of_matricies = []
        self.action_count = 0
        self.current_x = 0
        self.current_y = 0


    def update_matrix(self):

        #print(self.transformations)

        if self.action_count == 0:
            self.current_matrix = kn.create_trans_matrix([self.transformations.pop(0)])

        else:
            self.current_matrix = np.dot(self.current_matrix, kn.create_trans_matrix([self.transformations.pop(0)]))

        self.list_of_matricies.append(self.current_matrix )
        print("Matrix:", "(", self.action_count, ")")
        kn.print_2d_matrix(self.current_matrix)
        result_x = self.current_matrix[0][2]  # The first number in the last column
        result_y = self.current_matrix[1][2]  # The second number in the last column
        result_orientation = kn.get_orientation(self.current_matrix)

        if len(self.transformations) == 0:
            print("Final Position (x, y):", result_x,"," ,result_y)
            print("Final Orientation (degrees):", result_orientation)

        else:
            print("Position (x, y):", result_x, "," , result_y)
            print("Orientation (degrees):", result_orientation)

        self.action_count +=1