import aoc
import heapq

map = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
map = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

map = aoc.get_str(16)[:-1]
map = map.split('\n')
map = [list(x) for x in map]
# dist = [[float('inf') for _ in range(len(map[0]))] for _ in range(len(map))]
walls = set()
start, end = (-1, -1), (-1, -1)
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'S':
            start = (i, j)
            # dist[i][j] = 0
        elif map[i][j] == 'E':
            end = (i, j)
        elif map[i][j] == '#':
            walls.add((i, j))
            # dist[i][j] = -1
def rot90(dir):
    return (-dir[1], dir[0]), (dir[1], -dir[0])
def p1():
    dir = (0, 1)
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start, dir))
    best_dist = -1
    while pq:
        dist, pos, dir = heapq.heappop(pq)
        if pos in visited:
            continue
        visited.add((pos, dir))
        if pos == end:
            best_dist = dist
            break
        x, y = pos
        dx, dy = dir
        if (x + dx, y + dy) not in walls:
            if ((x + dx, y + dy), dir) not in visited:
                heapq.heappush(pq, (dist + 1, (x + dx, y + dy), dir))
        rot = rot90(dir)
        for d in rot:
            if (x + d[0], y + d[1]) not in walls:
                if ((x + d[0], y + d[1]), d) not in visited:
                    heapq.heappush(pq, (dist + 1001, (x + d[0], y + d[1]), d))
    return best_dist

def p2():
    best_path = p1()
    visited = set()
    pq = []
    heapq.heappush(pq, (0, [start], [(0, 1)]))
    best_seats = set()
    while pq:
        dist, path, dir_seq = heapq.heappop(pq)
        pos = path[-1]
        dir = dir_seq[-1]
        if pos in visited:
            continue
        visited.add((pos, dir))
        if pos == end and dist == best_path:
            for p in path:
                best_seats.add(p)
        x, y = pos
        dx, dy = dir
        if (x + dx, y + dy) not in walls:
            if ((x + dx, y + dy), dir) not in visited:
                heapq.heappush(pq, (dist + 1, path + [(x + dx, y + dy)], dir_seq + [dir]))
        rot = rot90(dir)
        for d in rot:
            if (x + d[0], y + d[1]) not in walls:
                if ((x + d[0], y + d[1]), d) not in visited:
                    heapq.heappush(pq, (dist + 1001, path + [(x + d[0], y + d[1])], dir_seq + [d]))

    return len(best_seats)
print(p2())
