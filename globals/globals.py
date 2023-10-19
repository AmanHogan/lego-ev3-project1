#################### globals.globals THAT NEED TO BE CHANGED ####################
# Change this as needed
ERROR_FACTOR_DISTANCE = 1.13 # error factor when moving on surface
# CARPET = 1.13
# WOOD = 1.00 
# TILE = ?

# Change this as needed
ERROR_FACTOR_TURN = 1.22 # error factor when turning on surface
# CARPET = 1.22
# WOOD = 1.18
# TILE = ?

# Change these variables as needed as needed
START_POSITION = [0.0001, 0.0001] # x and y pos of the robot [m]
GOAL_POSITION = [2,2] # x and y pos of goal [m]
NUMBER_OF_OBS = 1 # number of obstacles on grid [#] 
OBS_POSITIONS = [[1, 1]] # x and y pos of center of obstacles [m]
#########################################################################

####################### ROBOT CONSTANTS #################################
TIRE_CIRCUMFERENCE = 178 # Circumference of the tire in [mm]
FULL_ROTATION = 360 # [#]
TIRE_RPM = 400 # Revolutions per minute [r/min]
ROBOT_LENGTH = 105 # Length of the robot in [mm]
DIST_BTWN_WHEELS = 158.0000 # Distance between the wheels in [mm]
ROBOT_RADIUS_MM = (DIST_BTWN_WHEELS/2.0000) # Radius of robot tire axel [mm]
M_PI = 3.14159265359  # pi constant [#]
ROBOT_RADIUS_M = ROBOT_RADIUS_MM/1000 # Length of the robot in [m]
#########################################################################

###################### GRID/COURSE CONSTANTS (CAN CHANGE) ###############
GRID_SIZE = .3000 # precision of grid [m]
OBSTACLE_DIAMETER = .30500 # diameter of obstacles [m]
OBSTACLE_RADIUS = .30500/2.0000 # radius of obstacles [m]
WORKSPACE_X_MAX = 5 # workspace x max value of grid [m]
WORKSPACE_Y_MAX = 6 # workspace y max value of grid[m]
#########################################################################