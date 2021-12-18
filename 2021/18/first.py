class Snailfish:
    @classmethod
    def from_string(cls, string):
        if string.isnumeric():
            return Leaf(int(string))
        lvl = 0
        start = None
        end = None
        left = None
        right = None
        for i, c in enumerate(string):
            if c == '[':
                lvl += 1
                if lvl == 1:
                    start = i + 1
            elif lvl == 1 and c == ',':
                end = i
                left = Snailfish.from_string(string[start:end])
                start = i + 1
            elif c == ']':
                if lvl == 1:
                    end = i
                    right = Snailfish.from_string(string[start:end])
                lvl -= 1
        return Pair(left, right)

    def reduce(self):
        while True:
            did, self, _, _ = self.explode()
            if did:
                continue
            did, self = self.split()
            if not did:
                break

    def __add__(self, other):
        return Pair(self, other)

    def __repr__(self):
        return str(self)

class Leaf(Snailfish):
    def __init__(self, value):
        self.value = value

    def explode(self, level):
        return False, self, None, None

    def give(self, value, side):
        self.value += value

    def split(self):
        if self.value > 9:
            half = self.value // 2
            return True, Pair(Leaf(half), Leaf(self.value - half))
        return False, self

    def magnitude(self):
        return self.value

    def __str__(self):
        return str(self.value)

class Pair(Snailfish):
    LEFT  = 0
    RIGHT = 1
    def __init__(self, a, b):
        self.left, self.right = a, b

    def explode(self, level = 1):
        if level > 4:
            return True, Leaf(0), self.left.value, self.right.value
        did, self.left, a, b = self.left.explode(level + 1)
        if did:
            if b:
                self.right.give(b, Pair.LEFT)
            return True, self, a, None
        did, self.right, a, b = self.right.explode(level + 1)
        if did and a:
            self.left.give(a, Pair.RIGHT)
        return did, self, None, b

    def give(self, value, side):
        [self.left, self.right][side].give(value, side)

    def split(self):
        did, self.left = self.left.split()
        if not did:
            did, self.right = self.right.split()
        return did, self

    def magnitude(self):
        return self.left.magnitude() * 3 + self.right.magnitude() * 2

    def __str__(self):
        return "({}, {})".format(self.left, self.right)



def lines():
    while True:
        try:
            yield input()
        except:
            break

S = Snailfish.from_string(next(lines()))
for line in lines():
    S += Snailfish.from_string(line)
    S.reduce()
    print(S, S.magnitude())
