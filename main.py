#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor)
from pybricks.parameters import Port, Stop, Direction 
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from traversal.robotics import Robot, Navigator
from globals.globals import *
import rmath.kinematics as kn
import planning.path_planner as plan

print("-------------------- Start --------------------------")
print("Program running...")
print("-----------------------")

# Initialize the EV3 Brick.
ev3 = EV3Brick()

#Plan the Path using the initial variables in the globals.globals file ##########
path_found = plan.start_path_planning()
commands = kn.calculates_positions(path_found)
print(commands)

transformations = kn.commands_to_transformations(commands)

# Example List of transformations to make the robot move:
# ('T' = Translate, x distance[mm], y distance[mm])
# ('R' = Rotate, float = angle[deg]) 
print("List of Transformations", transformations)
print("-----------------------")

navigator = Navigator(transformations)
robot = Robot(Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE), Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE), navigator)

print("Converting transformations to executable commands ... ")
print("-----------------------")
commands = kn.transformation_to_commands(transformations)

print("Starting Path Traversal")
print("-----------------------")
robot.execute_commands(commands)


print("--------------------  End  --------------------")

