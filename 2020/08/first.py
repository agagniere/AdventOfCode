do_op = {'acc':(lambda i,acc,arg:(i + 1, acc + arg)),
         'nop':(lambda i,acc,arg:(i + 1, acc)),
         'jmp':(lambda i,acc,arg:(i + arg, acc))}

program = []
while True:
    try:
        instruction, argument = input().split()
        program += [(instruction, int(argument))]
    except:
        break

i = 0
acc = 0
seen = set()
while not i in seen and i < len(program):
    seen.add(i)
    i, acc = do_op[program[i][0]](i, acc, program[i][1])

print(acc)
