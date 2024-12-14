import aoc
from time import sleep

data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
data = aoc.get_str(14)[:-1]
data = data.split('\n')
width, height = 7, 11
width, height = 101, 103
robots = []
for l in data:
    ll = l.split(' ')
    x, y = ll[0].replace('p=', '').split(',')
    dx, dy = ll[1].replace('v=', '').split(',')
    robots.append([(int(x), int(y)), (int(dx), int(dy))])

def move(pos, vel, seconds=100):
    x, y = pos
    dx, dy = vel
    return (x + seconds * dx) % width, (y + seconds * dy) % height
def inQuandrand(x, y):
    if x < (width / 2) - 1 and y < (height / 2) - 1:
        return 0
    elif x < (width / 2) - 1 and y > (height / 2):
        return 1
    elif x > (width / 2) and y < (height / 2) - 1:
        return 2
    elif x > (width / 2) and y > (height / 2):
        return 3
    else:
        return -1
def p1(robots):
    for k in range(len(robots)):
        robots[k][0] = move(robots[k][0], robots[k][1])

    quadrants = [0 for _ in range(4)]

    for r in robots:
        x = inQuandrand(r[0][0], r[0][1])
        if x >= 0:
            quadrants[x] += 1

    res = 1
    for q in quadrants:
        res = res * q
    return res
def pmap(robots):
    map = [[0 for i in range(width)] for j in range(height)]
    for r in robots:
        x, y = r[0]
        map[y][x] += 1
    for i in range(height):
        s = ''
        for j in range(width):
            if map[i][j] == 0:
                s += '.'
            else:
                s += str(map[i][j])
        print(s)
    sleep(0.5)
    for _ in range(100):
        print()
def simulate(t):
    return [((sx + t*vx) % width, (sy + t*vy) % height) for (sx, sy), (vx, vy) in robots]

from statistics import variance
bx, bxvar, by, byvar = 0, 10*100, 0, 10*1000
for t in range(max(height, width)):
    xs, ys = zip(*simulate(t))
    if (xvar := variance(xs)) < bxvar:
        bx, bxvar = t, xvar
    if (yvar := variance(ys)) < byvar:
        by, byvar = t, yvar
res = bx+((pow(width, -1, height)*(by-bx)) % height)*width
print(res)
