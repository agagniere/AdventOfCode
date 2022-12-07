import sys

def lines():
    while True:
        try:
            yield input()
        except:
            break
