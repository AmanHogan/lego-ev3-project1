import math

def dot(a, b) -> list[list[float]]:
    """Multiplies (dot products) two matricies and returns result

    Args:
        a (list[list[float]]): 2D Matrix
        b (list[list[float]]): 2D Matrix

    Returns:
        list[list[float]]: Product of two matricies
    """
    result = [[0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000]]
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
    result = [[1.0000 if i == j else 0.0000 for i in range(n)] for j in range(n)]
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
