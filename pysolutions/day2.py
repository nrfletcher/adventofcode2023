import sys
from task import get_input

lines = get_input(sys.argv[1])

def parttwo():
    games = {}
    tsum = 0

    for line in lines:
        red_max, green_max, blue_max = 0, 0, 0
        char  = line[5]
        chars = len(line)
        game_num = ''
        pos = 5
        overflow = False

        while char != ':':
            game_num += char
            pos += 1
            char = line[pos]

        curr_num = ''
        curr_color = ''
        while pos < chars:
            if line[pos] in ';,' or line[pos] == ' ' or pos == chars - 1:
                if len(curr_num) > 0 and len(curr_color) > 0:
                    int_val = int(curr_num)
                    match curr_color:
                        case 'red':
                            if int_val > red_max:
                                red_max = int_val
                        case 'blue':
                            if int_val > blue_max:
                                blue_max = int_val
                        case 'green':
                            if int_val > green_max:
                                green_max = int_val
                        case _:
                            print('Invalid string')
                    curr_num = ''
                    curr_color = ''

            elif line[pos] == 'r':
                curr_color = 'red'
                pos += 3
            elif line[pos] == 'g':
                curr_color = 'green'
                pos += 5
            elif line[pos] == 'b':
                curr_color = 'blue'
                pos += 4
            elif line[pos] in '1234567890':
                curr_num += line[pos]

            pos += 1

        int_val = int(curr_num)
        match curr_color:
            case 'red':
                if int_val > red_max:
                    red_max = int_val
            case 'blue':
                if int_val > blue_max:
                    blue_max = int_val
            case 'green':
                if int_val > green_max:
                    green_max = int_val
            case _:
                print('Invalid string')

        print(f'{red_max} {green_max} {blue_max}')
        tsum += (red_max * blue_max * green_max)

    print(tsum)

def day2():
    games = {}
    count = 0
    red_max, green_max, blue_max = 12, 13, 14 

    for line in lines:
        print('NEW GAME')
        curr_red, curr_green, curr_blue = 0, 0, 0
        char  = line[5]
        chars = len(line)
        game_num = ''
        pos = 5
        overflow = False

        while char != ':':
            game_num += char
            pos += 1
            char = line[pos]

        curr_num = ''
        curr_color = ''
        while pos < chars:
            if line[pos] in ';,' or line[pos] == ' ' or pos == chars - 1:
                if len(curr_num) > 0 and len(curr_color) > 0:
                    print(f'num: {curr_num} color: {curr_color}')
                    int_val = int(curr_num)
                    match curr_color:
                        case 'red':
                            if int_val > red_max:
                                overflow = True
                        case 'blue':
                            if int_val > blue_max:
                                overflow = True
                        case 'green':
                            if int_val > green_max:
                                overflow = True
                        case _:
                            print('Invalid string')
                    curr_num = ''
                    curr_color = ''

            elif line[pos] == 'r':
                curr_color = 'red'
                pos += 3
            elif line[pos] == 'g':
                curr_color = 'green'
                pos += 5
            elif line[pos] == 'b':
                curr_color = 'blue'
                pos += 4
            elif line[pos] in '1234567890':
                curr_num += line[pos]

            pos += 1

        print(f'num: {curr_num} color: {curr_color}')
        int_val = int(curr_num)
        match curr_color:
            case 'red':
                if int_val > red_max:
                    overflow = True
            case 'blue':
                if int_val > blue_max:
                    overflow = True
            case 'green':
                if int_val > green_max:
                    overflow = True
            case _:
                print('Invalid string')

        games[game_num] = overflow

    total = 0
    for game in games:
        if games[game] == False:
            total += int(game)

    print(games)
    print(total)

parttwo()