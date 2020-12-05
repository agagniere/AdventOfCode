dep = {
    '>':(lambda x,y:(x+1,y)),
    '<':(lambda x,y:(x-1,y)),
    '^':(lambda x,y:(x,y+1)),
    'v':(lambda x,y:(x,y-1))
}

pos = (0,0)
seen = {pos:1}
for c in input():
    pos = dep[c](*pos)
    seen[pos] = 1 + seen.get(pos, 0)

print(len(seen))
