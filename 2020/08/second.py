do_op = {'acc':(lambda i,acc,arg:(i + 1, acc + arg)),
         'nop':(lambda i,acc,arg:(i + 1, acc)),
         'jmp':(lambda i,acc,arg:(i + arg, acc))}

# Read input
program = []
while True:
    try:
        instruction, argument = input().split()
        program += [(instruction, int(argument))]
    except:
        break
print("Read", len(program), "instructions")

# Identify instructions that lead to the end
targets = set([len(program) - 1])
previous_len = -1
while previous_len != len(targets):
    previous_len = len(targets)
    for i in range(len(program))[::-1]:
        ins, arg = program[i]
        next_i, _ = do_op[ins](i, 0, arg)
        if next_i in targets:
            targets.add(i)
print("Found", len(targets), "instructions that lead to the end")

# Execute the program, looking out for a switch that would lead to the end
acc = 0
i = 0
error_found = False
seen = {}
n = 0
while i < len(program) and i not in seen:
    n += 1
    seen[i] = n
    ins, arg = program[i]
    if not error_found and ins != 'acc':
        other_ins = 'jmp' if ins == 'nop' else 'nop'
        next_i, _ = do_op[other_ins](i, 0, arg)
        if next_i in targets:
            error_found = True
            ins = other_ins
            print("Fixed the program by changing the line {} from {} to {}".format(i, ins, other_ins))
    i, acc = do_op[ins](i, acc, arg)

print("Accumulator value after the execution :", acc)

#print("-" * 30)
#for i, (ins, arg) in enumerate(program):
#    print("{:3} | {:3} {:5} | {} | {:3}".format(i, ins, arg, 'T' if i in targets else ' ', seen[i] if i in seen else ' '))
#print("-" * 30)
