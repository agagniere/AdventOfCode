from utils import *

forest = store_forest()
visible = visible_trees(forest, False) | visible_trees(forest, True)
print(len(visible))
