import sys
from task import get_input

lines = get_input(sys.argv[1])

games = {}
count = 0

for line in lines:
    char  = line[5]
    game_num = ''
    pos = 5
    while char != ':':
        game_num += char
        pos += 1
        char = line[pos]
    games[game_num] = 0

print(games)