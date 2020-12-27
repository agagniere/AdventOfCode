class Bounds:
    def __init__(self, size):
        self.min_x = self.min_y = self.min_z = self.min_w = 0
        self.max_x = self.max_y = size
        self.max_z = self.max_w = 1

    def x(self): return range(self.min_x, self.max_x)
    def y(self): return range(self.min_y, self.max_y)
    def z(self): return range(self.min_z, self.max_z)
    def w(self): return range(self.min_w, self.max_w)

    def grow(self):
        self.min_x -= 1
        self.min_y -= 1
        self.min_z -= 1
        self.min_w -= 1
        self.max_x += 1
        self.max_y += 1
        self.max_z += 1
        self.max_w += 1


world = set()
bounds = Bounds(8)
# world.add((1,0,0,0))
# world.add((2,1,0,0))
# world.add((0,2,0,0))
# world.add((1,2,0,0))
# world.add((2,2,0,0))
for y in bounds.y():
    for x, c in enumerate(input()):
        if c == '#':
            world.add((x, y, 0, 0))

for _ in range(6):
    prev = world
    world = set()
    bounds.grow()
    for w in bounds.w():
        for z in bounds.z():
            for y in bounds.y():
                for x in bounds.x():
                    neighbours = len([i for i in range(3 ** 4)
                                      if i != ((3**4)//2) and (x + (i % 3) - 1,
                                                      y + ((i // 3) % 3) - 1,
                                                      z + ((i // 9) % 3) - 1,
                                                      w + (i // 27) - 1) in prev])
                    if neighbours == 3 or (neighbours == 2 and (x, y, z, w) in prev):
                        world.add((x, y, z, w))
    # for z in bounds.z():
    #     print('')
    #     for y in bounds.y():
    #         print("{:2}{:3}".format(z, y), end=' ')
    #         print(' '.join([''.join(['.#'[(x, y, z, w) in world] for x in bounds.x()]) for w in bounds.w()]))

print(len(world))
