from utils import *

board = store_lines()
start, end = extract_start_end(board)
print(start, end)
print(min_steps_to_reach([start], end, board))
