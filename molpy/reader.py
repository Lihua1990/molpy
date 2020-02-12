import os

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')

with open('look_and_say.dat', 'r') as handle:
    data = handle.read()
print(data)
