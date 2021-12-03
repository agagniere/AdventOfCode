def filter_down(remaining, compare):
    bit = 0
    while len(remaining) > 1:
        stat = sum(map(lambda line:int(line[bit]), remaining))
        target = "01"[compare(stat, len(remaining) // 2 + (len(remaining) % 2))]
        remaining = list(filter(lambda line: line[bit] == target, remaining))
        print("{:2} {:5} {:1} {:5}".format(bit, stat, target, len(remaining)))
        bit += 1
    return remaining[0]

lines = []
while True:
    try:
        lines += [input()]
    except:
        break

o2  = int(filter_down(lines, int.__ge__), base=2)
co2 = int(filter_down(lines, int.__lt__), base=2)
print(o2, co2, o2 * co2)
