from utils import Point, lines

board = list(lines())

adjacent = {}
for y, line in enumerate(board):
    for x, c in enumerate(line):
        if c != '.' and not c.isdigit():
            adjacent |= {neigh: c for neigh in Point(x, y).neighbors()}

total = 0
for y, line in enumerate(board):
    number = 0
    is_adjacent = False
    for x, c in enumerate(line):
        if c.isdigit():
            number *= 10
            number += ord(c) - ord('0')
            is_adjacent = is_adjacent or (x,y) in adjacent
        else:
            if number and is_adjacent:
                total += number
            number = 0
            is_adjacent = False
    if number and is_adjacent:
        total += number

print(total)
