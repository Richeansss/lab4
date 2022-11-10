import math

def distance(x1, x2, y1, y2):

    dist1 = math.sqrt(pow(y1 - x1, 2) + pow(y2 - x2, 2))
    return dist1



print(f"Евклидовое растояние: {distance(10, 10, -10, -10)}")