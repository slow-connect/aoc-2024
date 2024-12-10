import aoc
import heapq

map = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split('\n')[1:]
map = aoc.get_str(10).split('\n')[:-1]
map = [[int(x) for x in row] for row in map]
n, m = len(map), len(map[0])

def find_trailstarts(map):
    nulls = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                nulls.append((i, j))

    return nulls


def pmap(data): print("\n".join("".join(str(c) for c in line) for line in data))
def get_neighbors(x, y, map):
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  neighbors = []
  height = len(map)
  width = len(map[0])

  for dx, dy in directions:
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < height and 0 <= new_y < width:
      neighbors.append((new_x, new_y))

  return neighbors



starts = find_trailstarts(map)

pq = []

for s in starts:
    heapq.heappush(pq, ([s], 1))


ends = []
while pq:
    path, length = heapq.heappop(pq)
    current = path[-1]
    if length == 10:
        ends.append((path[0], current))
    else:
        for nb in get_neighbors(current[0], current[1], map):
            if map[nb[0]][nb[1]] == map[current[0]][current[1]] + 1:
                new_path = path.copy() + [nb]
                heapq.heappush(pq, (new_path, length + 1))
print(len(set(ends)))
print(len(ends))
