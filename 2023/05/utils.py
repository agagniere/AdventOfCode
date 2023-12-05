import sys

def lines():
    while True:
        try:
            yield input()
        except:
            break

def debug(fmt, *args, **kwargs):
    kwargs['file'] = sys.stderr
    print(fmt, *args, **kwargs)
