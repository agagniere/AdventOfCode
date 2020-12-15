do_op = {
    1:(lambda a,b: a + b),
    2:(lambda a,b: a * b)
}

prog = list(map(int, input().split(',')))

prog[1] = 12
prog[2] = 2

i = 0
while prog[i] != 99:
    ins, a, b, dest = prog[i:][:4]
    prog[dest] = do_op[ins](prog[a], prog[b])
    i += 4

print(prog[0])
