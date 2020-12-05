dep = {
    '>':(lambda x,y:(x+1,y)),
    '<':(lambda x,y:(x-1,y)),
    '^':(lambda x,y:(x,y+1)),
    'v':(lambda x,y:(x,y-1))
}

pos = (0,0)
robot = (0,0)
seen = {pos:2}
santa_turn = True
for c in input():
    if santa_turn:
        pos = dep[c](*pos)
        seen[pos] = 1 + seen.get(pos, 0)
    else:
        robot = dep[c](*robot)
        seen[robot] = 1 + seen.get(robot, 0)
    santa_turn = not santa_turn

print(len(seen))
