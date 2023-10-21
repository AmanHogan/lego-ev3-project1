"""Performs more complex matrix operations related to kinematics and converts transforms -> commandsand transforms -> matricie
"""
import math
from globals import *
import rmath.micro_numpy as np

##################################################
# kinematics : Performs more complex 
# matrix operations related to kinematics 
# and converts transforms -> commands
# and transforms -> matricies
# 10/17/2023
##################################################

def transforms_to_matrix(transformations)-> list[list[float]]:
    """Converts a list of transforms of format (EX format: [('T', 1000, 0), ('R', 90))
    into a rotation or translation matrix. Then multiplies the set of matricies to get a result.

    Args:
        transformations (list[tuple[str,float]] | list[tuple[str, float, float]]): 
        A list of transforms of format (EX format: [('T', 1000, 0), ('R', 90))

    Returns:
        list[list[float]]: The product of 1 or more matricies. 2D matrix
    """
    
    result = np.eye(3) # initializes result with indentity matrix

    for transform in transformations:

        # Get translation Matrix
        if transform[0] == 'T':
            dx, dy = transform[1:]
            t_matrix = np.array([[1, 0, dx],[0, 1, dy], [0, 0, 1]])
            result = np.dot(result, t_matrix)

        # Get rotation matrix
        elif transform[0] == 'R':
            theta_deg = transform[1]
            r_matrix = np.array([[np.cos(np.deg2rad(theta_deg)), -np.sin(np.deg2rad(theta_deg)), 0], [np.sin(np.deg2rad(theta_deg)), np.cos(np.deg2rad(theta_deg)), 0], [0, 0, 1]])
            result = np.dot(result, r_matrix)

    # Return matrix product of the list of transforms
    return result


def get_orientation(matrix) -> float:
    """Gets orientation of the robot using the arc tan of positions
    supplied in the matrix

    Args:
        matrix (list[list[float]]): 2D matrix

    Returns:
        float: angles in degrees of the orientation of the matrix
    """

    # Extract the elements of the matrix
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

    # Calculate the angle using arctan2
    angle_rad = math.atan2(b, a)
    angle_deg = math.degrees(angle_rad)
    
    return angle_deg

def transformation_to_commands(transformations) -> list[tuple[str, int]]:
    """Converts transformations of format :  (EX format: [('T', 1000, 0), ('R', 90)) into
    executable commands for the robot in format : ('move', <float>) or ('turn', <float>)

    Args:
        transformations (list[tuple[str,float]] | list[tuple[str, float, float]]): 
        A list of transforms of format (EX format: [('T', 1000, 0), ('R', 90))

    Returns:
        list[tuple[str, int]]: A sequence of commands to be executed by the robot to move and turn
    """    
    commands = []
    current_angle = 0

    for transformation in transformations:

        if transformation[0] == 'T':
            dx, dy = transformation[1], transformation[2]
            distance = np.sqrt(dx ** 2 + dy ** 2)
            commands.append(("move", distance))

        elif transformation[0] == 'R':
            current_angle = transformation[1]
            commands.append(("turn", current_angle))

    return commands


def print_commands(commands) -> None:
    """Takes a list of commands that are used to drive the robot,
    and prints them out.

    Args:
        commands (List[Tuple[str, int]]): list of commands
    """
    for command in commands:
        print(command)

def print_matrix(matrix) -> None:
    """Prints a given 2D matrix

    Args:
        matrix (List[List[int]]): 2D matrix
    """
    print("------------------------")
    for row in matrix:
        formatted_row = ["{:.4f}".format(value) for value in row]
        print(" ".join(formatted_row))
    print("------------------------")




def calculate_angle_differences(angles):
    diffs = [angles[0]]
    for i in range(1, len(angles)):
        new_angle = angles[i] - angles[i - 1]
        if new_angle > 180:
            new_angle -= 360
        diffs.append(new_angle)
    return diffs

def calculate_distances(positions):
    dists = []
    for i in range(len(positions) - 1):
        distance = math.sqrt((positions[i + 1][0] - positions[i][0]) ** 2 +
                            (positions[i + 1][1] - positions[i][1]) ** 2)
        dists.append(distance)
    return dists

def generate_commands(positions, angles):
    diffs = calculate_angle_differences(angles)
    dists = calculate_distances(positions)
    
    commands = []
    for i in range(len(positions) - 1):
        commands.append(("turn", diffs[i]))
        commands.append(("move", dists[i]))
    
    return commands

def commands_to_transformations(commands):
    transformations = []
    current_x, current_y, current_angle = 0, 0, 0

    for command in commands:
        action, value = command

        if action == 'move':
            angle_rad = math.radians(current_angle)
            dx = value * math.cos(angle_rad) 
            dy = value * math.sin(angle_rad)
            transformations.append(('T', dx, dy))
            current_x += dx
            current_y += dy
        elif action == 'turn':
            transformations.append(('R', value))
            current_angle += value

    return transformations


def calculates_positions(positions):
    # Example usage:

    angles = find_angles_between_positions(positions)
    diffs = []
    diffs.append(angles[0])

    for i in range(len(angles) -1):
        new_angle = angles[i+1]-angles[i]
        if new_angle > 180:
            new_angle -= 360
        diffs.append(new_angle)
        


    dists = []
    for i in range(len(positions)-1) :
        distance = math.sqrt((positions[i+1][0] - positions[i][0])** 2 + ((positions[i+1][1] - positions[i][1]) ** 2))
        dists.append(distance)

    # Remove the first element from the dists list.
    commands = []
    for i in range(len(positions)-1):
        commands.append(("turn", diffs[i]))
        commands.append(("move",dists[i] * 1000.0000))
        
    print("------------------------")
    print("Angles",diffs)
    print("Distances", dists)
    print("------------------------")


    return commands



def find_angles_between_positions(positions):
    """Calculates the angles between a list of positions in degrees.

    Args:
    positions: A list of tuples containing the coordinates of the positions.

    Returns:
    A list of the angles between the positions in degrees, in the range [0, 360].
    """

    angles = []
    diffs = []
    counter = 0
  
    for i in range(len(positions) - 1): 
        p1 = positions[i]
        p2 = positions[i + 1]

        angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])

        # Convert the angle to degrees.
        angle_in_degrees = math.degrees(angle)

        # Wrap the angle to the range [0, 360].
        angle_in_degrees %= 360

        angles.append(angle_in_degrees)

        counter += 1


    return angles
# Example usage
if __name__ == "__main__":

    print("------------------------")

    # Example Transformations
    path_found = [(0.0, 0.0), (0.3, 0.3), (0.3, 0.6), (0.6, 0.9), (0.6, 1.2), (0.9, 1.5), (1.2, 1.8), (1.5, 1.8), (1.8, 2.1), (2.1, 2.1)]


   
    print("Converting positions to executable commands ... ")
    print("-----------------------")
    angles = find_angles_between_positions(path_found)
    angles.pop(0)
    commands = generate_commands(path_found, angles)
    print("------------------------")
    print("Angles:", angles)
    print("Distances:", calculate_distances(path_found))
    print("Commands:", commands)
    print("------------------------")
