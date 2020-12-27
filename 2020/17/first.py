class Bounds:
    def __init__(self, size):
        self.min_x = self.min_y = self.min_z = 0
        self.max_x = self.max_y = size
        self.max_z = 1

    def x(self): return range(self.min_x, self.max_x)
    def y(self): return range(self.min_y, self.max_y)
    def z(self): return range(self.min_z, self.max_z)

    def grow(self):
        self.min_x -= 1
        self.min_y -= 1
        self.min_z -= 1
        self.max_x += 1
        self.max_y += 1
        self.max_z += 1


world = set()
bounds = Bounds(8)
# world.add((1,0,0))
# world.add((2,1,0))
# world.add((0,2,0))
# world.add((1,2,0))
# world.add((2,2,0))
for y in bounds.y():
    for x, c in enumerate(input()):
        if c == '#':
            world.add((x, y, 0))

for _ in range(6):
    prev = world
    world = set()
    bounds.grow()
    for z in bounds.z():
        for y in bounds.y():
            for x in bounds.x():
                neighbours = len([i for i in range(3 ** 3)
                                  if i != 13 and (x + (i % 3) - 1, y + ((i // 3) % 3) - 1, z + (i // 9) - 1) in prev])
                if neighbours == 3 or (neighbours == 2 and (x, y, z) in prev):
                    world.add((x, y, z))
    #print('\n'.join([' '.join([''.join(['.#'[(x,y,z) in world] for x in bounds.x()]) for z in bounds.z()]) for y in bounds.y()]), end='\n\n')

print(len(world))
