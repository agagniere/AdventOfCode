from utils import *

board = store_lines()
*starts, end = extract_start_end(board)
for y, row in enumerate(board):
    starts += [Point(x, y) for x, c in enumerate(row) if c == 'a']
print(min_steps_to_reach(starts, end, board))
