import numpy as np


def distance(point1, point2):
    """
    Calculate distance between two points

    Parameters
    ----------------------------------------
    point1: array_like
        The first point
    point2: array_like
        The second point
        
    Returns
    ----------
    float
        The distance between point1 and point2
    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)


def read_xyz(filename):
    """
    Read XYZ files.

    Parameters
    ----------
    filename: string_like. Name of the file to read.

    Returns
    ----------
    float
        The distance between point1 and point2. 
    """

    with open(filename, "r") as handle:
        data = handle.readlines()

    data = data[2:]
    data = [x.split() for x in data]
    symbols = [x[0] for x in data]

    xyz = []
    for line in data:
        xyz.append([float(line[1]), float(line[2]), float(line[3])])

    return {"symbols": np.array(symbols), "geometry": xyz} # return as a dict


def fibo(n): 
    """
    Write Fibonacci series up to n

    Parameters
    ----------
   n: integer
        The threshold of printed number.

    Returns
    ----------
    int
        The next number up to. 
    """       
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b


