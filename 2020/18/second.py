import AST

def node_from_token(token):
    if token[0] == '+':
        return AST.Operator('+', 1)
    elif token[0] == '*':
        return AST.Operator('*', 2)
    else:
        return AST.Leaf(token)

answer = 0
while True:
    try:
        line = input()
    except:
        break
    answer += AST.evaluate(line, node_from_token)

print(answer)
