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
        ans = self
        while True:
            did, ans, _, _ = ans.explode()
            if did:
                continue
            did, ans = ans.split()
            if not did:
                break
        return ans

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
        return Leaf(self.value + value)

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
        did, left, a, b = self.left.explode(level + 1)
        if did:
            right = self.right
            if b:
                right = self.right.give(b, Pair.LEFT)
            return True, Pair(left, right), a, None
        did, right, a, b = self.right.explode(level + 1)
        if did and a:
            left = left.give(a, Pair.RIGHT)
        return did, Pair(left, right), None, b

    def give(self, value, side):
        if side == Pair.LEFT:
            return Pair(self.left.give(value, side), self.right)
        return Pair(self.left, self.right.give(value, side))

    def split(self):
        did, left = self.left.split()
        right = self.right
        if not did:
            did, right = self.right.split()
        return did, Pair(left, right)

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

numbers = [Snailfish.from_string(line) for line in lines()]
M = 0
for i, n in enumerate(numbers):
    for j, m in enumerate(numbers):
        if i != j:
            M = max(M, (n + m).reduce().magnitude())
print(M)
