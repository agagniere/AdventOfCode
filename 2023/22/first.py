from utils import Point, lines
from collections import namedtuple

def parse(lines):
    for line in lines:
        start, end = line.split('~')
        start, end = Point(*map(int, start.split(','))), Point(*map(int, end.split(',')))
        result = []
        assert(s <= e for s,e in zip(start, end))
        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):
                result += [Point(x, y, z) for z in range(start.z, end.z + 1)]
        yield tuple(result)

Block = namedtuple('Block', ['index', 'cubes', 'supported_by', 'supporting'])

if __name__ == '__main__':
    blocks = sorted(parse(lines()), key=lambda l: (l[0].z, l[0].y, l[0].x))
    down = {}
    downed_blocks = []
    for i, block in enumerate(blocks):
        if block[0].z == 1:
            downed_blocks.append(Block(i, block, set(), set()))
            for cube in block:
                down[cube] = i
        else:
            supported_by = set()
            fall_height = 0
            while fall_height < block[0].z - 1:
                for cube in block:
                    N = cube + (0, 0, -fall_height - 1)
                    if N in down:
                        supported_by.add(down[N])
                if supported_by:
                    break
                fall_height += 1
            B = Block(i, tuple(cube + (0,0,-fall_height) for cube in block), supported_by, set())
            downed_blocks.append(B)
            for S in supported_by:
                downed_blocks[S].supporting.add(i)
            for cube in B.cubes:
                down[cube] = i

    R = 0
    for block in downed_blocks:
        print(block.index, block.supported_by, block.supporting)
        for S in block.supporting:
            if len(downed_blocks[S].supported_by) == 1:
                break
        else:
            R += 1
    print(R)
