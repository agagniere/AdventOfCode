from first import part1
from second import part2

tests = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)
]

for string, one, two in tests:
    a = part1(string)
    b = part2(string)
    if one == a and two == b:
        print('OK', string)
    else:
        print(f'Wrong, got {a}, {b} and not {one}, {two} for {string}')
