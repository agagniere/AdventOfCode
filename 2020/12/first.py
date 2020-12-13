import math

def forward(x, y, d, a):
    rad = math.pi * d / 180
    return (x + math.cos(rad) * a, y + math.sin(rad) * a, d)

do_op = {
    'N':(lambda x,y,d,a:(x,y+a,d)),
    'S':(lambda x,y,d,a:(x,y-a,d)),
    'E':(lambda x,y,d,a:(x+a,y,d)),
    'W':(lambda x,y,d,a:(x-a,y,d)),
    'L':(lambda x,y,d,a:(x,y,d+a)),
    'R':(lambda x,y,d,a:(x,y,d-a)),
    'F':forward
}

x=0
y=0
d=0

while True:
    try:
        line = input()
    except:
        break
    action = line[0]
    arg = int(line[1:])
    x,y,d = do_op[action](x,y,d,arg)

print(x, y, d)
print(round(abs(x) + abs(y)))
