import aoc
import heapq
from collections import deque



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

def find_reachable_nines(start_x, start_y, grid):
  visited, reachable_nines = set(), set()
  queue = deque([(start_x, start_y, 0)])

  while queue:
    x, y, current_height = queue.popleft()

    if (x, y) in visited:
      continue

    visited.add((x, y))

    if grid[x][y] == 9:
      reachable_nines.add((x, y))
      continue

    for next_x, next_y in get_neighbors(x, y, grid):
      next_height = grid[next_x][next_y]

      if next_height == current_height + 1:
        queue.append((next_x, next_y, next_height))

  return reachable_nines



trailheads = find_trailstarts(map)
p1 = 0
for x, y in trailheads:
    reachable_nines = find_reachable_nines(start_x=x, start_y=y, grid=map)
    score = len(reachable_nines)
    p1 += score
print(p1)


cnt = 0
while pq:
    path, length = heapq.heappop(pq)
    current = path[-1]
    if length == 10:
        cnt += 1
    else:
        for nb in get_neighbors(current[0], current[1], map):
            if map[nb[0]][nb[1]] == map[current[0]][current[1]] + 1:
                new_path = path.copy() + [nb]
                heapq.heappush(pq, (new_path, length + 1))
print(cnt)
