mask = [0, 0]
memory = {}
while True:
    try:
        ins, arg = input().split(' = ')
    except:
        break
    if ins == 'mask':
        mask[0] = ~sum([1 << i for i,b in enumerate(arg[::-1]) if b == '0'])
        mask[1] = sum([1 << i for i,b in enumerate(arg[::-1]) if b == '1'])
    else:
        memory[ins[4:-1]] = int(arg) & mask[0] | mask[1]

print(sum(memory.values()))
