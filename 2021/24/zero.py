def lines():
    while True:
        try:
            yield input()
        except:
            break

def give(s):
    for c in s:
        yield int(c)

def base(n, b):
    if n < b:
        return [n]
    return base(n // b, b) + [n % b]

digits = give("12345678912345")
apply = {
    "inp": (lambda _   : next(digits)),
    "add": (lambda a,b : a + b),
    "mul": (lambda a,b : a * b),
    "div": (lambda a,b : a // b),
    "mod": (lambda a,b : a % b),
    "eql": (lambda a,b : int(a == b))
}
mem = {c:0 for c in "xyzw"}
translate = lambda x: mem[x] if x in mem else int(x)

prog = [(line.split()[0], line.split()[1:]) for line in lines()]

for ins, args in prog:
    mem[args[0]] = apply[ins](*map(translate, args))
    print("{} {:14} -> {:14} {}".format(ins, str(args), mem[args[0]], str(base(mem[args[0]], 26))))
print(mem)
