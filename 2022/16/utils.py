
def lines():
    while True:
        try:
            yield input()
        except:
            break

def parse(iterable) -> list:
    Topo = {}
    Rate = {}
    for line in iterable:
        P = line.split(' ', 9)
        name, rate, connections = P[1], P[4][5:-1], P[9]
        Rate[name] = int(rate)
        Topo[name] = list(connections.split(', '))
    return Topo, Rate
