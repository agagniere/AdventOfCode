import sys

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def print(self, depth = 0):
        print(f"{'  ' * depth}- {self.name} {self.size}")

class Dir:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.cache = None

    @property
    def size(self):
        if not self.cache:
            self.cache = sum([c.size for c in self.children])
        return self.cache

    def print(self, depth = 0):
        print(f"{'  ' * depth}- {self.name}/")
        for c in sorted(self.children, key=lambda x:x.name):
            c.print(depth + 1)

def lines():
    while True:
        try:
            yield input()
        except:
            break

def tree(session):
    current = []
    dirs  = {'/':Dir('/')}

    for line in session:
        if line[0] == '$':
            cmd = line[2:4]
            if cmd == 'cd':
                name = line[5:]
                if name == '..':
                    current.pop()
                else:
                    current.append(name)
                #print('Moved to', '/'.join(current))
            elif cmd != 'ls':
                print('Error')
        else:
            size, name = line.split()
            fullname = '/'.join(current + [name])
            if size == 'dir':
                dirs[fullname] = Dir(name)
                dirs['/'.join(current)].children.append(dirs[fullname])
            else:
                dirs['/'.join(current)].children.append(File(name, size))
    return dirs
