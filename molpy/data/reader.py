import os

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')

with open(filename, 'r') as handle:
    look_and_say = handle.read()
# print(data)
