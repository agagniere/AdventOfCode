class Cell:
    def __init__(self, value):
        self.value = int(value)
        self.marked = False
    def mark(self):
        self.marked = True

    def __int__(self):
        return self.value
    def __bool__(self):
        return self.marked
    def __str__(self):
        return f"({self.value}, {self.marked})"
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        return int(self) == int(other)
    def __hash__(self):
        return int(self).__hash__()


draws = list(map(int, input().split(',')))

boards = []
current = []
quick_access = {}
while True:
    try:
        line = input()
    except:
        if current:
            boards += [current]
        break
    if line:
        row = [Cell(n) for n in line.split()]
        for i, cell in enumerate(row):
            quick_access[cell] = quick_access.get(cell, []) + [(len(boards), len(current), i, cell)]
        current += [row]
    elif current:
        boards += [current]
        current = []

won = set()
for n in draws:
    for b, r, c, cell in quick_access[n]:
        cell.mark()
        if all(boards[b][r]) or all([row[c] for row in boards[b]]):
            if not b in won:
                S = sum([sum(map(int, filter(lambda x:not x, row))) for row in boards[b]])
                print (n, b, S, n * S)
            won.add(b)
