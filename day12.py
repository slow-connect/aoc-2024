import aoc
import heapq

data = aoc.get_str(12)[:-1]
data = data.split('\n')
data = [list(d.strip()) for d in data]
data0 = ['~' for _ in range(len(data[0]))]
data = [data0] + data + [data0]
for i in range(len(data)):
    data[i] = ['~'] + data[i] + ['~']
n, m = len(data), len(data[0])
visited = [[True for _ in range(len(data[i]))] for i in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '~':
            visited[i][j] = True
        else:
            visited[i][j] = False


def get_neighbors(x:int, y:int, n=n, m=m) -> list[tuple[int, int]]:
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in dir:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < n and 0 <= new_y < m:
            neighbors.append((new_x, new_y))
    return neighbors

p1 = 0
p2 = 0
for j in range(n):
    for i in range(m):
        if not visited[i][j]:
            area = 1
            perimeter = 0
            sides = 0
            label = data[i][j]
            group = set()
            group.add((i, j))
            pq = []
            heapq.heappush(pq, (i, j))
            visited[i][j] = True
            while pq:
                x, y = heapq.heappop(pq)
                for n in get_neighbors(x, y):
                    if data[n[0]][n[1]] == label and not visited[n[0]][n[1]]:
                        area += 1
                        visited[n[0]][n[1]] = True
                        heapq.heappush(pq, n)
                        group.add(n)
            for x, y in group:
                for n in get_neighbors(x, y):
                    if data[n[0]][n[1]] != label:
                        perimeter += 1
            left = set()
            right = set()
            up = set()
            down = set()
            for x, y in group:
                if (x-1, y) not in group:
                    up.add((x, y))
                if (x+1, y) not in group:
                    down.add((x, y))
                if (x, y-1) not in group:
                    left.add((x, y))
                if (x, y+1) not in group:
                    right.add((x, y))
            for (x, y) in up:
                if (x, y) in left:
                    sides += 1
                if (x, y) in right:
                    sides += 1
                if (x-1, y-1) in right and (x, y) not in left:
                    sides += 1
                if (x-1, y+1) in left and (x, y) not in right:
                    sides += 1
            for (x, y) in down:
                if (x, y) in left:
                    sides += 1
                if (x, y) in right:
                    sides += 1
                if (x+1, y-1) in right and (x, y) not in left:
                    sides += 1
                if (x+1, y+1) in left and (x, y) not in right:
                    sides += 1
            # print(label, area, perimeter)
            p1 += area * perimeter
            p2 += area * sides
print(p1)
print(p2)
