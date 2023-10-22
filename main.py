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

# Plan the path
ev3.speaker.set_speech_options(voice='f3')
ev3.speaker.say("Beginning Path plannig")
path_found = plan.start_path_planning()
ev3.speaker.say("Path Found")

# Get angles between points on path found
print("List of Angles")
angles = kn.find_angles_between_positions(path_found)
angles = [round(i,5) for i in angles]
angles.pop(0)
print(angles)
print("-----------------------")

# Get distances between points on path found
print("List of distances")
distances = kn.calculate_distances(path_found)
distances = [round(i,5) for i in distances]
print(distances)
print("-----------------------")

# Convert path found to robot commands
ev3.speaker.say("Converting Path to Robot Commands")
commands = kn.positions_to_commands(path_found)
print("List of commands")
print(commands)
print("-----------------------")

# Convert Robot commands to transformations
transformations = kn.commands_to_transformations(commands)
print("List of Transformations")
print(transformations)
print("-----------------------")

# Navigator (Handles transformations)
# Robot (Handles commands)
# Link transforms <-> commands, to keep track of movement
navigator = Navigator(transformations)
robot = Robot(Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE), Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE), navigator)

# Start robot commands
ev3.speaker.say("Executing Commands")
print("Starting Path Traversal")
print("-----------------------")
robot.execute_commands(commands)
print("--------------------  End  --------------------")

