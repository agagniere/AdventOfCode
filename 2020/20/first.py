border_map = {}
tiles = {}

with open('input.txt', 'r') as f:
    for tile in f.read().split('\n\n'):
        lines = tile.split('\n')
        name = int(lines[0][5:9])
        borderU = lines[1]
        borderD = lines[-1]
        borderL = tile[len(lines[0]) + 1::len(lines[1]) + 1]
        borderR = tile[len(lines[0]) + len(lines[1])::len(lines[1]) + 1]
        borders = []
        for border in [borderU, borderD, borderL, borderR]:
            rev = border[::-1]
            if rev in border_map:
                border_map[rev] += [name]
                borders += [rev]
            else:
                border_map[border] = border_map.get(border, []) + [name]
                borders += [border]
        tiles[name] = borders

answer = 1
for tile, borders in tiles.items():
    neigh = 0
    for border in borders:
        if (border in border_map and len(border_map[border]) > 1) or (border[::-1] in border_map and len(border_map[border[::-1]]) > 1):
            neigh += 1
    if neigh == 2:
        print(tile)
        answer *= tile

print(answer)
