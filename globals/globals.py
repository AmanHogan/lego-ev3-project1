"""Contains constants and varaibles that will be modified before compile time"""
#################### globals.globals THAT NEED TO BE CHANGED ####################

# error factor when moving on surface
CARPET_ERROR_DISTANCE = 1.13
WOOD_ERROR_DISTANCE = 1.012
TILE_ERROR_DISTANCE = 1.012
ERROR_FACTOR_DISTANCE = TILE_ERROR_DISTANCE # Change this as needed

# error factor when moving on surface
CARPET_ERROR_TURN = 1.220
WOOD_ERROR_TURN = 1.102
TILE_ERROR_TURN = .944
ERROR_FACTOR_TURN = TILE_ERROR_TURN # Change this as needed

# Change these variables as needed as needed
START_POSITION = [0.0001, 0.0001] # x and y pos of the robot [m]
GOAL_POSITION = [.610, 1.525] # x and y pos of goal [m]
NUMBER_OF_OBS = 3 # number of obstacles on grid [#] 
OBS_POSITIONS = [[.915,.305], [0,.610], [.305,1.22]] # x and y pos of center of obstacles [m]
#########################################################################

####################### ROBOT CONSTANTS #################################
TIRE_CIRCUMFERENCE = 178 # Circumference of the tire in [mm]
FULL_ROTATION = 360 # [#]
TIRE_RPM = 400 # Revolutions per minute [r/min]
ROBOT_LENGTH = 105 # Length of the robot in [mm]
DIST_BTWN_WHEELS = 158.0000 # Distance between the wheels in [mm]
ROBOT_RADIUS_MM = (DIST_BTWN_WHEELS/2.0000) # Radius of robot tire axel [mm]
M_PI = 3.14159265359  # pi constant [#]
ROBOT_RADIUS_M = .18 # Length of the robot in [m]
#########################################################################

###################### GRID/COURSE CONSTANTS (CAN CHANGE) ###############
GRID_SIZE = .300 # precision of grid [m]
OBSTACLE_DIAMETER = .30500 # diameter of obstacles [m]
OBSTACLE_RADIUS = .30500/2.0000 # radius of obstacles [m]
WORKSPACE_X_MAX = 5 # workspace x max value of grid [m]
WORKSPACE_Y_MAX = 6 # workspace y max value of grid[m]
#########################################################################