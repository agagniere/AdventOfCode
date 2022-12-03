def my_print(v):
    print(f'{v:036b} : {v}')

FULL = sum([1 << i for i in range(36)])

memory = {}
while True:
    try:
        ins, arg = input().split(' = ')
        print(ins, arg)
    except:
        break
    if ins == 'mask':
        mask = sum([1 << i for i,b in enumerate(arg[::-1]) if b == '1'])
        mask_x = [i for i,b in enumerate(arg[::-1]) if b == 'X']
        or_masks = [0]
        and_masks = [FULL]
        for bit in mask_x:
            M = (1 << bit)
            prev = or_masks
            or_masks = []
            for m in prev:
                or_masks += [m|M, m]
            prev = and_masks
            and_masks = []
            for m in prev:
                and_masks += [m, m & ~M]
    else:
        address = int(ins[4:-1])
        value = int(arg)
        address |= mask
        for o, a in zip(or_masks, and_masks):
            t = (address | o) & a
            memory[t] = value
print(sum(memory.values()))
