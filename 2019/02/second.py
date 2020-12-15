do_op = {
    1:(lambda a,b: a + b),
    2:(lambda a,b: a * b)
}

prog = list(map(int, input().split(',')))

def run(prog):
    i = 0
    while prog[i] != 99:
        ins, a, b, dest = prog[i:][:4]
        prog[dest] = do_op[ins](prog[a], prog[b])
        i += 4

for noun in range(100):
    for verb in range(100):
        local = [e for e in prog]
        local[1] = noun
        local[2] = verb
        run(local)
        if local[0] == 19690720:
            print(noun * 100 + verb)
            break
