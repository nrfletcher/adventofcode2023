import sys
from task import get_input

lines = get_input(sys.argv[1])

for row in range(len(lines)):
    for j, char in enumerate(lines[row]):
        print(f'x: {row} y: {j} ch: {char}')