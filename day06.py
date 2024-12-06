import aoc

data = aoc.get_lst(6)[:-1]
data.append("".join(['~' for i in range(len(data[0]))]))
data.insert(0, "".join(['~' for i in range(len(data[0]))]))
for i in range(len(data)):
    data[i] = '~' + data[i] + '~'
data = [list(s) for s in data]

def p1(data):
    pos = (0, 0)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                pos = (i, j)
                break

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    k=0
    while data[pos[0]][pos[1]] != '~':
        data[pos[0]][pos[1]] = 'X'
        if data[pos[0] + directions[k][0]][pos[1] + directions[k][1]] == '#':
            k += 1
            k = k % 4
            continue
        pos = (pos[0] + directions[k][0], pos[1] + directions[k][1])
    cnt = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 'X':
                cnt += 1
    print(cnt)


def pmap(data): print("\n".join("".join(c for c in line) for line in data))


def p1_test(data):
    def isinside(x, y): return 0 < x < len(data)-1 and 0 < y < len(data[0])-1
    start = (-1, -1)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                start = (i, j)
                break
    visited = set()
    dir = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
    rotate = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    x, y = start
    d = 'up'
    while isinside(x, y):
        visited.add((x, y))
        dx, dy = x + dir[d][0], y + dir[d][1]
        # print(data[x + dx][x + dy])
        if data[dx][dy] == '#':
            d = rotate[d]
        else:
            x = dx
            y = dy
    print(len(visited))
    # for x, y in visited:
    #     data[x][y] = 'X'
    # pmap(data)

def p2(data):
    def isinside(x, y): return 0 < x < len(data) - 1 and 0 < y < len(data[0]) - 1
    start = (-1, -1)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                start = (i, j)
                break
    visited = set()
    dir = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
    rotate = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    x, y = start
    d = 'up'
    while(isinside(x, y)):
        visited.add((x, y))
        dx, dy = x + dir[d][0], y + dir[d][1]
        # print(data[x + dx][x + dy])
        if data[dx][dy] == '#':
            d = rotate[d]
        else:
            x = dx
            y = dy
    obstactles = visited - {start}
    cnt = 0
    for obs in obstactles:
        x, y = obs
        data[x][y] = '#'
        xx, yy = start
        d = 'up'
        vec_visited = set()
        while isinside(xx, yy):
            vec_visited.add((xx, yy, d))
            dx, dy = xx + dir[d][0], yy + dir[d][1]
            if data[dx][dy] == '#':
                d = rotate[d]
            else:
                xx = dx
                yy = dy
            if (xx, yy, d) in vec_visited:
                cnt += 1
                break
        data[x][y] = '.'
    print(cnt)






p1(data) # 5208 in 0.175s
p1_test(data) # 5208 in 0.143s
p2(data) # 1972 in 22.249s
