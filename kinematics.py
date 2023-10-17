import math
import micro_numpy as np

def create_trans_matrix(transformations)-> list[list[float]]:
    result = np.eye(3)

    for transformation in transformations:
        if transformation[0] == 'T':
            dx, dy = transformation[1:]
            translation_matrix = np.array([[1, 0, dx],
                                           [0, 1, dy],
                                           [0, 0, 1]])
            result = np.dot(result, translation_matrix)
        elif transformation[0] == 'R':
            theta_deg = transformation[1]
            rotation_matrix = np.array([[np.cos(np.deg2rad(theta_deg)), -np.sin(np.deg2rad(theta_deg)), 0],
                                        [np.sin(np.deg2rad(theta_deg)), np.cos(np.deg2rad(theta_deg)), 0],
                                        [0, 0, 1]])
            result = np.dot(result, rotation_matrix)

    return result


def get_orientation(matrix):
    # Extract the elements of the matrix
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

    # Calculate the angle using arctan2
    angle_rad = math.atan2(b, a)
    angle_deg = math.degrees(angle_rad)
    
    return angle_deg

def transformation_to_commands(transformations) -> list[tuple[str, int]]:
    result = np.eye(3)  # Initialize with the identity matrix
    for transformation in transformations:
        if transformation[0] == 'T':
            dx, dy = transformation[1:]
            translation_matrix = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
            result = np.dot(result, translation_matrix)
        elif transformation[0] == 'R':
            theta_deg = transformation[1]
            rotation_matrix = np.array([[np.cos(np.deg2rad(theta_deg)), -np.sin(np.deg2rad(theta_deg)), 0], [np.sin(np.deg2rad(theta_deg)), np.cos(np.deg2rad(theta_deg)), 0], [0, 0, 1]])
            result = np.dot(result, rotation_matrix)
    
    commands = []
    current_angle = 0
    for transformation in transformations:
        if transformation[0] == 'T':
            dx, dy = transformation[1], transformation[2]
            distance = np.sqrt(dx ** 2 + dy ** 2)
            commands.append(("move", distance))
        elif transformation[0] == 'R':
            angle_deg = transformation[1]
            current_angle += angle_deg
            commands.append(("turn", current_angle))
    return commands

def print_commands(commands: list[tuple[str, int]]) -> None:
    """Takes a list of commands that are used to drive the robot,
    and prints them out.

    Args:
        commands (List[Tuple[str, int]]): list of commands
    """
    for command in commands:
        print(command)

def print_matrix(matrix: list[list[float]]) -> None:
    """Prints a given 2D matrix

    Args:
        matrix (List[List[int]]): 2D matrix
    """
    print("-----------------------")
    for row in matrix:
        formatted_row = ["{:.4f}".format(value) for value in row]
        print(" ".join(formatted_row))
    print("-----------------------")



# Example usage
if __name__ == "__main__":

    transformations = [('T', 1000, 0), ('R', 90), ('T', 0, 1000), ('R', 90)]

    commands = transformation_to_commands(transformations)

    result_matrix = create_trans_matrix(transformations)
    result_x = result_matrix[0][2]  # The first number in the last column
    result_y = result_matrix[1][2]  # The second number in the last column
    result_orientation = get_orientation(result_matrix)

    print_commands(commands)
    print("Final Position (x, y):", result_x, result_y)
    print("Final Orientation (degrees):", result_orientation)
   





