import sys
from task import get_input

lines = get_input(sys.argv[1])

def parttwo():
    # If we see a gear, check for adjacent numbers (check all 8 surrounding spots, and count instances)
    # If total adjacent is == 2, get those two numbers, multiply them, and add to our total
    gearratiosums = 0
    partnumsums = 0
    gears = {}

    for row in range(len(lines)):
        curr_num = ''
        begin = 0
        for j, char in enumerate(lines[row]):
            
            if char in '1234567890':
                curr_num += char
            if char in '1234567890' and j > 0 and len(curr_num) == 1:
                begin = j

            if len(curr_num) > 0 and char not in '1234567890' or (j == len(lines[0]) - 1 and len(curr_num) > 0):
                for rowi in range(row - 1, row + 2):
                    for colj in range(begin - 1, j + 1):
                        if rowi >= 0 and rowi < len(lines) and j >= 0 and j < len(lines[0]):
                            if lines[rowi][colj] == '*':
                                gear = str(rowi) + str(colj)
                                if gear in gears:
                                    gears[gear].append(int(curr_num))
                                else:
                                    gears[gear] = [int(curr_num)]
                                partnumsums += int(curr_num)
                curr_num = ''

    for gear in gears:
        if len(gears[gear]) == 2:
            gearratiosums += gears[gear][0] * gears[gear][1]
    print(gearratiosums)


def partone():
    partnumsums = 0

    for row in range(len(lines)):
        curr_num = ''
        begin = 0
        for j, char in enumerate(lines[row]):
            
            if char in '1234567890':
                curr_num += char
            if char in '123456789' and j > 0 and len(curr_num ) == 1:
                begin = j

            if len(curr_num) > 0 and char not in '1234567890' or (j == len(lines[0]) - 1 and len(curr_num) > 0):
                for rowi in range(row - 1, row + 2):
                    for colj in range(begin - 1, j + 1):
                        if rowi >= 0 and rowi < len(lines) and j >= 0 and j < len(lines[0]):
                            if lines[rowi][colj] not in '1234567890.':
                                print(f'added: {curr_num} val: {lines[rowi][colj]}')
                                partnumsums += int(curr_num)
                curr_num = ''

    print(partnumsums)

parttwo()