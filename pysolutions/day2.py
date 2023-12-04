import sys
from task import get_input

if len(sys.argv) > 1:
    print(sys.argv[1])

lines = get_input(sys.argv[1])
print(lines)