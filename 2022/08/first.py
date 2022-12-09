from utils import *

forest = store_forest()
#print('\n'.join(map(str,forest)))
R = visible_from(forest)
print(len(R))
