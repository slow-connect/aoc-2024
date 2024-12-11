import aoc
from math import log10 as log
from math import floor
import functools

data = aoc.get_str(11)[:-1]
data = [int(d) for d in data.split(' ')]


@functools.lru_cache(maxsize=None)
def results(d):
    if d == 0:
        return (1, None)
    elif floor(log(d)) % 2 == 1:
        num = len(str(d))
        div = 10 ** (num // 2)
        return (d // div, d % div)
    else:
        return (d * 2024, None)

@functools.lru_cache(maxsize=None)
def count_stone(d, count):

    left, right = results(d)

    if count == 1:
        if right is None:
            return 1
        else:
            return 2
    else:
        output = count_stone(left, count - 1)
        if right is not None:
            output += count_stone(right, count - 1)
        return output

# part 1:
output = 0
count = 25
for s in data:
    output += count_stone(s, count)
print(output)


output = 0
# part 2:
count = 75
for s in data:

    output += count_stone(s, count)
print(output)
