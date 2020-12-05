def bisection(s, lower, upper, upper_char):
    for c in s:
        mid = (lower + upper) // 2
        if c == upper_char:
            lower = mid
        else:
            upper = mid
    return lower

seen = set()
highest_id = 0
lowest_id = 1000
for i in range(900):
    ticket = input()
    row = bisection(ticket[:7], 0, 128, 'B')
    col = bisection(ticket[7:], 0, 8, 'R')
    seat = 8 * row + col
    highest_id = max(highest_id, seat)
    lowest_id = min(lowest_id, seat)
    seen.add(seat)

print(next(filter(lambda x: x not in seen, range(lowest_id, highest_id))))
