"""
molpy.py
A really cool molecule manipulation package.

Handles the primary functions
"""
from .util import distance
import numpy as np

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


## Class can hold data, should start with a capital letter
## self is the object itself.
## it doesn't check the data just recording the data
class Molecule:
    def __init__(self, symbols, geometry, orient=True):
        self.symbols = np.asarray(symbols, dtype=str)
        self.geometry = np.asarray(geometry, dtype=float)

        if len(self.geometry.shape) != 2:
            self.geometry = self.geometry.reshape(-1, 3)
        if self.symbols.shape[0] != self.geometry.shape[0]:
            raise ValueError("Symbol and geometry length does not match!")


    def distance(self, index1, index2):
        ## this should be refered as self.distance instead of distance
        return distance(self.geometry[index1], self.geometry[index2])


class NameMolecule(Molecule):
    """
    name: name here

    Attributes
    ----------

    Descriptions here, but not inside the def __init__
    
    """
    def __init__(self, name, symbols, geometry):

        self.name = name
        super().__init__(symbols, geometry)


        # if orient:

# Molecule(symbols, geometry)


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())

