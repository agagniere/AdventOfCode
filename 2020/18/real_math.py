import AST

def node_from_token(token):
    if token[0] == '+':
        return AST.Operator('+', 2)
    elif token[0] == '*':
        return AST.Operator('*', 1)
    else:
        return AST.Leaf(token)

while True:
    try:
        line = input()
    except:
        break
    result = AST.evaluate(line, node_from_token)
    print(line, '=', result)
