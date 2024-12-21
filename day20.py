import aoc
import heapq
# from numpy import abs

coord = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
coord = aoc.get_str(20)[:-1]
coord = coord.split('\n')

walls = set()
inner_walls = set()
start = (-1, -1)
end = (-1, -1)
for i in range(len(coord)):
    for j in range(len(coord[i])):
        if coord[i][j] == '#':
            walls.add((i, j))
            if i != 0 and i != len(coord) - 1 and j != 0 and j != len(coord[i]) - 1:
                inner_walls.add((i,j))
        if coord[i][j] == 'S':
            start = (i, j)
        if coord[i][j] == 'E':
            end = (i, j)


def get_neighbours(x, y):
    return [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

def dijkstra_day18(start, end, walls):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, [(start, 0)]))
    best_dist = -1
    best_path = []
    while pq:
        dist, path = heapq.heappop(pq)
        pos = path[-1][0]
        if pos in visited:
            continue
        visited.add((pos))
        if pos == end:
            best_dist = dist
            best_path = path
            break
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) == end:
                heapq.heappush(pq, (dist + 1, path + [((x + dx, y + dy), dist + 1)]))
            if (x + dx, y + dy) not in walls:
                if ((x + dx, y + dy)) not in visited:
                    heapq.heappush(pq, (dist + 1, path + [((x + dx, y + dy), dist + 1)]))
    return best_dist, best_path

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def get_all_in_distance(x, y, d):
    dist = []
    for i in range(-d, d+1):
        for j in range(-d, d+1):
            if abs(i) + abs(j) <= d:
                dist.append((x+i, y+j))
    return dist

init_distance, best_path = dijkstra_day18(start, end, walls)
cnt = 0
dist_dict = dict(best_path)

for i in range(len(best_path)):
    for j in range(i+1, len(best_path)):
        if manhattan_distance(best_path[i][0], best_path[j][0]) <= 20:
            saving = dist_dict[best_path[j][0]] - dist_dict[best_path[i][0]] - manhattan_distance(best_path[i][0], best_path[j][0])
            if saving >= 100:
                cnt += 1
print(cnt)

# for i in range(len(best_path) - 1):
#     for j in range(i+3, len(best_path)):
#         if manhattan_distance(best_path[i], best_path[j]) <= 2:
#             dist, path = dijkstra_day18(best_path[i], best_path[j], walls)
#             # if dist - 2 <= 100:
#                 # cnt += 1
#             if dist - 2 not in dist_dict:
#                 dist_dict[dist - 2] = 1
#             else:
#                 dist_dict[dist - 2] += 1
# dist_dict = dict(sorted(dist_dict.items()))
# dist_excepted = {2:14, 4:14, 6:2, 8:4, 10:2, 12:3, 20:1, 36:1, 38:1, 40:1, 64:1}
# r = 0
# for k in dist_dict.keys():
#     if k >= 100:
#         r +=  dist_dict[k]
# print(r)


## part 2
