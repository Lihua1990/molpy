import argparse
import molpy
from  .util import read_xyz, distance


def main():

    parser = argparse.ArgumentParser(description='A molecule utility that can read XYZ files.')
    parser.add_argument('filename',type=str,help='The XYZ file to read')                    #  metavar='N', 

    parser.add_argument('Index1', type=int, help='Index of the first atom') 

    parser.add_argument('Index2',type=int, help='Index of the second atom') 

    args = parser.parse_args()
    print(args)
    
    mol = molpy.util.read_xyz(args.filename)
    print(f"Reading XYZ files: {args.filename}")

    print("Calculating distance...")

    dist = distance(mol["geometry"][args.Index1], mol["geometry"][args.Index2])

    s1 = mol["symbols"][args.Index1]
    s2 = mol["symbols"][args.Index2]

    print("Reading XYZ files: {}".format(args.filename))
    print(f"The total distance between atoms {args.Index1}:{s1} and {args.Index2}:{s2} = {dist:.3f}A")
    # distance_here = util.distance(args.Index1, args.Index2)
    
    # print(distance_here)
    # print(paserser)
    # print(args)
    


