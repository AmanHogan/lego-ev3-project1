import math

def translation_matrix(dx, dy):
    return [[1, 0, dx], [0, 1, dy], [0, 0, 1]]

def rotation_matrix(theta_deg):
    theta_rad = math.radians(theta_deg)
    cos_theta = math.cos(theta_rad)
    sin_theta = math.sin(theta_rad)
    return [[cos_theta, -sin_theta, 0], [sin_theta, cos_theta, 0], [0, 0, 1]]

def transformation_matrix(dx, dy, theta_deg):
    translation = translation_matrix(dx, dy)
    rotation = rotation_matrix(theta_deg)
    return dot(translation, rotation)

def dot(a, b):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += a[i][k] * b[k][j]
    return result

def array(data):
    if isinstance(data, list):
        return data
    else:
        raise ValueError("Input must be a list")

def eye(n):
    result = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    return result

def arctan2(y, x):
    return math.atan2(y, x)

def deg2rad(deg):
    return math.radians(deg)

def rad2deg(rad):
    return math.degrees(rad)

def sqrt(x):
    return math.sqrt(x)

def cos(x):
    return math.cos(x)

def sin(x):
    return math.cos(x)
