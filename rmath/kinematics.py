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


# Example usage
if __name__ == "__main__":

    print("------------------------")

    # Example Transformations
    transformations = [('T', 1000, 0), ('R', 90), ('T', 0, 1000), ('R', 90)]

    # Convert to Transformations to commands
    commands = transformation_to_commands(transformations)

    # Convert Transformations to resltant matrix
    r_matrix = transforms_to_matrix(transformations)

    # Get x, y, and orientation
    x_val = r_matrix[0][2]  
    y_val = r_matrix[1][2] 
    result_orientation = get_orientation(r_matrix)

    print("Input Transformations")
    print(transformations)
    print("------------------------")
    print("Commands")
    print_commands(commands)
    print("------------------------")
    print("Final Matrix")
    print_matrix(r_matrix)
    print("Final Position (x, y):", round(x_val, 4), round(y_val, 4))
    print("Final Orientation (degrees):", result_orientation)
    print("------------------------")