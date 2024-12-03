import aoc
from numpy import abs
from collections import Counter

data = aoc.get_lst(1)[:-1]
def p1(data):
    l1, l2 = [], []

    for i in range(len(data)):
        tmp = data[i].split()
        l1.append(int(tmp[0]))
        l2.append(int(tmp[1]))
    l1.sort()
    l2.sort()
    res = 0
    for i in range(len(data)):
        res += abs(l1[i] - l2[i])
    print(res)

def p2(data):
    l1, l2 = [], []
    for i in range(len(data)):
        tmp = data[i].split()
        l1.append(int(tmp[0]))
        l2.append(int(tmp[1]))
    l2 = Counter(l2)
    res = 0
    for val in l1:
        if val in l2:
            res += val * l2[val]
    print(res)

p1(data)
p2(data)
