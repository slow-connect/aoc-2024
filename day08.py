import aoc


input_str = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
input_str = aoc.get_str(8)[:-1]
input = input_str.split("\n")
input = [list(i) for i in input]
n, m = len(input), len(input[0])
output = [['.' for i in range(len(input[j]))] for j in range(len(input))]

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def dist(p1, p2): return p2[0] - p1[0], p2[1] - p1[1]
def isinside(x, y): return 0 <= x < n and 0 <= y < m
def pmap(data): print("\n".join("".join(c for c in line) for line in data))

def p1(data):
    for c in chars:
        if c in input_str:
            pos = []
            for i in range(len(input)):
                for j in range(len(input[i])):
                    if input[i][j] == c:
                        pos.append((i, j))
            for i in range(len(pos)):
                for j in range(i+1, len(pos)):
                    dx, dy = dist(pos[i], pos[j])
                    if isinside(pos[j][0]  + dx, pos[j][1] + dy):
                        output[pos[j][0] + dx][pos[j][1] + dy] = '#'
                    if isinside(pos[i][0] - dx, pos[i][1] - dy):
                        output[pos[i][0] - dx][pos[i][1] - dy] = '#'
    # pmap(input)
    cnt = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if output[i][j] == '#':
                cnt += 1
    print(cnt)


def p2(data):
    for c in chars:
        if c in input_str:
            pos = []
            for i in range(len(input)):
                for j in range(len(input[i])):
                    if input[i][j] == c:
                        pos.append((i, j))
            for i in range(len(pos)):
                for j in range(i+1, len(pos)):
                    dx, dy = dist(pos[i], pos[j])
                    for k in range(0, max(n, m)):
                        if isinside(pos[j][0]  + k * dx, pos[j][1] + k * dy):
                            output[pos[j][0] + k * dx][pos[j][1] + k * dy] = '#'
                        if isinside(pos[i][0] - k * dx, pos[i][1] - k * dy):
                            output[pos[i][0] - k * dx][pos[i][1] - k * dy] = '#'

    # pmap(output)
    cnt = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if output[i][j] == '#':
                cnt += 1
    print(cnt)
p2(input)
