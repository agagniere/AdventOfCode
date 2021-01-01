class Node:
    def __init__(self, precedence):
        self.precedence = precedence

    def __lt__(self, other):
        return self.precedence < other.precedence

    def push(self, other):
        other.left = self
        return other


class Operator(Node):
    def __init__(self, operator, precedence):
        super().__init__(precedence)
        self.operator = operator
        self.left = None
        self.right = None

    def push(self, other):
        if other < self:
            self.right = self.right.push(other) if self.right else other
            return self
        return super().push(other)

    def eval(self):
        return {'+':(lambda a,b:a+b), '*':(lambda a,b:a*b)}[self.operator](self.left.eval(), self.right.eval())


class Leaf(Node):
    def __init__(self, label):
        super().__init__(0)
        self.value = int(label)

    def eval(self):
        return self.value


class Tree(Node):
    def __init__(self):
        super().__init__(0)
        self.root = None

    def add(self, node):
        self.root = self.root.push(node) if self.root else node

    def eval(self):
        return self.root.eval()


def tokenize(expr):
    return expr.replace('(', '( ').replace(')', ' )').split()


def evaluate(expr, convert):
    stack = [Tree()]
    for token in tokenize(expr):
        if token == '(':
            stack += [Tree()]
            stack[-2].add(stack[-1])
        elif token == ')':
            stack.pop()
        else:
            stack[-1].add(convert(token))
    return stack[0].eval()


'''
def manual_tokenize(expr):
    end = 0
    while end < len(expr):
        if expr[end] in '()+*':
            yield expr[end]
            end += 1
        else:
            beg = end
            while end < len(expr) and expr[end] in string.digits:
                end += 1
            yield expr[beg:end]
        while end < len(expr) and expr[end] == ' ':
            end += 1


def split_tokenize(expr):
    for sub in expr.split():
        if sub[0] in '()':
            yield sub[0]
            yield sub[1:]
        elif sub[-1] in '()':
            yield sub[:-1]
            yield sub[-1]
        else:
            yield sub
'''
