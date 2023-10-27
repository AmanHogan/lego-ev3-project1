"""Contains constants and varaibles that will be modified before compile time"""

################################ COMPILE TIME CONSTANTS ####################

# error factor when moving on surface
CARPET_ERROR_DISTANCE = 1.13
TILE_ERROR_DISTANCE = 1.00
ERROR_FACTOR_DISTANCE = TILE_ERROR_DISTANCE # Change this as needed

# error factor when moving on surface
CARPET_ERROR_TURN = 1.220
TILE_ERROR_TURN = .950
ERROR_FACTOR_TURN = TILE_ERROR_TURN # Change this as needed

START_POSITION = [.305*2,.305*2] # x and y pos of the robot [m] # Change this as needed
GOAL_POSITION =  [0.305*13,.305*7]# x and y pos of goal [m] # Change this as needed
NUMBER_OF_OBS = 22# number of obstacles on grid [#] # Change this as needed

# x and y pos of center of obstacles [m] # Change this as needed
OBS_POSITIONS = [
  [.305*4,.305*1],[.305*4,.305*2],[.305*4,.305*3],[.305*4,.305*4],[.305*4,.305*5],
  [.305*7,.305*4],[.305*7,.305*5],[.305*7,.305*6],[.305*7,.305*7],[.305*7,.305*8],[.305*7,.305*9],[.305*7,.305*10],
  [.305*11,.305*3],[.305*12,.305*3],[.305*12,.305*4],[.305*13,.305*3],[.305*13,.305*4],
  [.305*10, .305*3], [.305*10, .305*4], [.305*10, .305*5], [.305*10, .305*6], [.305*10, .305*7], [.305*10, .305*8]] 

GRID_SIZE = .1000 # precision of grid [m] # Change this as needed
OBSTACLE_DIAMETER = .30500 # diameter of obstacles [m] # Change this as needed
OBSTACLE_RADIUS = .30500/2.0000 # radius of obstacles [m]
#########################################################################

####################### ROBOT CONSTANTS #################################
TIRE_CIRCUMFERENCE = 178 # Circumference of the tire in [mm]
FULL_ROTATION = 360 # [#]
TIRE_RPM = 250 # Revolutions per minute [r/min] # Change this as needed
ROBOT_LENGTH = 105 # Length of the robot in [mm]
DIST_BTWN_WHEELS = 158.0000 # Distance between the wheels in [mm]
ROBOT_RADIUS_MM = (DIST_BTWN_WHEELS/2.0000) # Radius of robot tire axel [mm]
M_PI = 3.14159265359  # pi constant [#]
ROBOT_RADIUS_M = .18 # Length of the robot in [m] # Change this as needed
#########################################################################