from utils import *

forest = store_forest()
by_columns = columns(forest)
print(max(scenic_score(x, y, row, by_columns[x]) for y,row in enumerate(forest) for x in range(len(row))))
