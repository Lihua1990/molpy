import molpy 
import numpy as np   
import os

def open_xyz(file_location):
    
    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coords = (xyz_file[:,1:])
    coords = coords.astype(np.float)
    return symbols, coords


def read_xyz(molecule, com):
    molecule_name = str(molecule) + '.xyz'
    file_loc = os.path.join(os.getcwd(), 'data', 'xyz', molecule_name)
    molecule_symbol, molecule_coords = open_xyz(file_loc)
    com = np.mean(molecule_coords, axis=0)
    return com


def get_molecule(molecule):

    molecule_name = str(molecule) + '.xyz'
    file_loc = os.path.join('data', 'xyz', molecule_name)
    molecule_symbol, molecule_coords = open_xyz(file_loc)

    # mol['geometry'] = molecule_coords
    return molecule_coords
