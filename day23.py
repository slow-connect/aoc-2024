import aoc
import networkx as nx

GRAPH = nx.Graph()

data = aoc.get_str(23)[:-1]
data = data.split('\n')
data = [d.split('-') for d in data]
for d in data:
    GRAPH.add_edge(d[0], d[1])


all_cliques= nx.enumerate_all_cliques(GRAPH)
print('part 1')
triangles = [x for x in all_cliques if len(x) == 3]
cnt = 0
for s in triangles:
    for i in s:
        if i[0] == 't':
            cnt += 1
            break
print(cnt)
print('part 2')
employees = nx.find_cliques(GRAPH)
s = ''
for e in employees:
    if len(','.join(e)) > len(s):
        s = sorted(e)
        s = ','.join(s)
print(s)
