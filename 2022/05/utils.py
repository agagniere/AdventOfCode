import sys
from itertools import zip_longest

def lines():
    while True:
        try:
            yield input()
        except:
            break
