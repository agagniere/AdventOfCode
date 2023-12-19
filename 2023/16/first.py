from collections import defaultdict

from utils import Point, lines


def count_energy(board: list[str], start: Point, direction: (int, int)) -> int:
    seen = defaultdict(set)

    def travel(pos: Point, v: (int, int)):
        while pos.y in range(len(board)) and pos.x in range(len(board[pos.y])):
            if v in seen[pos]:
                return
            seen[pos].add(v)
            c = board[pos.y][pos.x]
            if c in r'\/':
                v = {'/':(-v[1], -v[0]),
                     '\\':(v[1], v[0])}[c]
            elif c == '-' and v[1]:
                travel(pos, (-1, 0))
                v = (1, 0)
            elif c == '|' and v[0]:
                travel(pos, (0, -1))
                v = (0, 1)
            pos += v

    travel(start, direction)
    return len(seen)

if __name__ == '__main__':
    print(count_energy(list(lines()), Point(0, 0), (1, 0)))
