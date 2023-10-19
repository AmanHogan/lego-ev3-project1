#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from robotics import Robot, Navigator
from globals import *
import micro_numpy as np
import kinematics as kn
import math
import path_planner as plan

print("-------------------- Start --------------------------")
print("Program running...")
print("-----------------------")

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Plan the Path using the initial variables in the globals file
path_found = plan.start_path_planning()

# TODO: Somehow convert the path_found to a list of transformations
# Example: transformations = path_to_transforms(path_found)

# Example List of transformations to make the robot move:
# ('T' = Translate, x distance[mm], y distance[mm])
# ('R' = Rotate, float = angle[deg]) 
transformations = [('T', START_POSITION[0], START_POSITION[1]), ('R',90), ('R',90), ('R',90), ('R',90) ] 

print("List of Transformations", transformations)
print("-----------------------")

navigator = Navigator(transformations)
robot = Robot(Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE), Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE), navigator)

print("Converting transformations to executable commands ... ", transformations)
print("-----------------------")
commands = kn.transformation_to_commands(transformations)

print("Starting Path Traversal")
print("-----------------------")
robot.execute_commands(commands)

print("--------------------  End  --------------------")

