from collections import deque

do_op = {
    '+': int.__add__,
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__floordiv__
}

def lines():
    while True:
        try:
            yield input()
        except:
            break
