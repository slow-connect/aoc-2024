import aoc

data = [d.split('\n') for d in data]

data = aoc.get_lst_of_lst(25)

keys = set()
locks = set()
for specs in data:
    tmp = ["".join(col) for col in zip(*specs)]
    l = [s.count('#') - 1 for s in tmp]
    if specs[0] == '.....':
        keys.add(tuple(l))
    else:
        locks.add(tuple(l))


cnt = 0
for key in keys:
    for lock in locks:
        tup = tuple(map(lambda i, j: i + j, key, lock))
        if max(tup) <= 5:
            cnt += 1
print(cnt)
