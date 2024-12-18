import aoc
import heapq

coord = aoc.get_str(18)[:-1]
coord = coord.split('\n')
coord = [s.split(',') for s in coord]
walls = set()

start = (0, 0)
end = (70, 70)
for i in range(72):
    walls.add((-1, i))
    walls.add((71, i))
    walls.add((i, -1))
    walls.add((i, 71))
for i in range(1024):
    walls.add((int(coord[i][0]), int(coord[i][1])))


def dijkstra_day16(start, end, walls):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start))
    best_dist = -1
    while pq:
        dist, pos = heapq.heappop(pq)
        if pos in visited:
            continue
        visited.add((pos))
        if pos == end:
            best_dist = dist
            break
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) not in walls:
                if ((x + dx, y + dy)) not in visited:
                    heapq.heappush(pq, (dist + 1, (x + dx, y + dy)))
    return best_dist
print("Part 1")
bestdist = dijkstra_day16(start, end, walls)
print(bestdist)

print("Part 2")
k = 1024
while bestdist != -1:
    k+= 1
    walls.add((int(coord[k][0]), int(coord[k][1])))
    bestdist = dijkstra_day16(start, end, walls)
print(','.join(coord[k]))
