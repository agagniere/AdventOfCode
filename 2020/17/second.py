class Bounds:
    def __init__(self, upper_limits):
        self.limits = [[0, end] for end in upper_limits]

    def __getitem__(self, item):
        return range(*self.limits[item])

    def grow(self):
        for dim in self.limits:
            dim[0] -= 1
            dim[1] += 1


X, Y, Z, W = range(4)
world = set()
bounds = Bounds([8, 8, 1, 1])
# world.add((1,0,0,0))
# world.add((2,1,0,0))
# world.add((0,2,0,0))
# world.add((1,2,0,0))
# world.add((2,2,0,0))
for y in bounds[Y]:
    for x, c in enumerate(input()):
        if c == '#':
            world.add((x, y, 0, 0))

for _ in range(6):
    prev = world
    world = set()
    bounds.grow()
    for w in bounds[W]:
        for z in bounds[Z]:
            for y in bounds[Y]:
                for x in bounds[X]:
                    neighbours = len([i for i in range(3 ** 4)
                                      if i != 3**4 // 2 and (x + (i % 3) - 1,
                                                      y + ((i // 3) % 3) - 1,
                                                      z + ((i // 9) % 3) - 1,
                                                      w + (i // 27) - 1) in prev])
                    if neighbours == 3 or (neighbours == 2 and (x, y, z, w) in prev):
                        world.add((x, y, z, w))
    for z in bounds[Z]:
        print('-' * (5 + (bounds[X].stop - bounds[X].start + 1) * (bounds[W].stop - bounds[W].start)))
        for y in bounds[Y]:
            print("{:2}{:3}".format(z if not y else ' ', y), ' '.join([''.join(['.#'[(x, y, z, w) in world] for x in bounds[X]]) for w in bounds[W]]))

print(len(world))
