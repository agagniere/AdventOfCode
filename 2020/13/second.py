input()
bus = [(int(b), i) for i, b in enumerate(input().split(',')) if b != 'x']

#  (t + a) % n == 0     <=>    t % b == (b - a) % b
na = sorted([(b, (b - i) % b) for b, i in bus])

print("We're looking for a t such that:")
for n, a in na:
    print("t = {:4} [{}]".format(a, n))

step, t = na.pop()
while na:
    n, a = na.pop()
    print("Starting from {:15}, we look for a number congruent to {:4} modulo {:4}, by steps of {}".format(t, a, n, step))
    while (t % n) != a:
        t += step
    step *= n

print(t)
