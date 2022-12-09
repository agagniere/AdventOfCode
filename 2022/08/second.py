from utils import *

forest = dict_forest()
print(max(scenic_score(forest, tree) for tree in forest.keys()))
