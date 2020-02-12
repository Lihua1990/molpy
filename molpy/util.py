import numpy as np



def distance(point1, point2):

    """
    Calculate distance between two points

    Parameterss

    ----------------------------------------

    point1


    ----------------------------------------
    returns
    ----------

    float

    
    
    
    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1-point2)




    