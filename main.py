#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from robotics import Robot, Navigator
import micro_numpy as np
import matricies as mx

# Initialize the EV3 Brick.
ev3 = EV3Brick()

origin = [('T', 0, 0)]
obstacles = None
transformations = [('T', 1000, 0), ('R', 90), ('T', 0, 1000), ('R', 90)]

print("List of Transformations", transformations)
print("-----------------------")


navigator = Navigator(obstacles, transformations)
robot = Robot(Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE), Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE), navigator)

# Get executable commands from Transformations
# Execute commands
commands = mx.transformation_to_commands(transformations)
robot.execute_commands(commands)




