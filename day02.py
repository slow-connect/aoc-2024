import aoc
from numpy import abs
from collections import Counter

data = aoc.get_lst(2)[:-1]
def p1(data):
    cnt = 0
    for l in data:
        p = l.split()
        p = [int(x) for x in p]
        tmp = []
        for i in range(len(p) - 1):
            tmp.append(p[i] - p[i + 1])
        tmp_abs = [abs(x) for x in tmp]
        if sum(tmp) == sum(tmp_abs) or -sum(tmp) == sum(tmp_abs):
            if max(tmp_abs) <= 3 and min(tmp_abs) >= 1:
                cnt += 1
    print(cnt)
def p2(data):
    cnt = 0
    for l in data:
        p = l.split()
        p = [int(x) for x in p]
        tmp = [p[i] - p[i + 1] for i in range(len(p) - 1)]
        def save(tmp):
            tmp_abs = [abs(x) for x in tmp]
            if sum(tmp) == sum(tmp_abs) or -sum(tmp) == sum(tmp_abs):
                if max(tmp_abs) <= 3 and min(tmp_abs) >= 1:
                    return True
            return False
        if save(tmp):
            cnt += 1
        else:
            for i in range(len(p)):
                p1 = [p[k] for k in range(len(p)) if k != i]
                tmp = [p1[k] - p1[k + 1] for k in range(len(p1) - 1)]
                if save(tmp):
                    cnt += 1
                    break
    print(cnt)
p1(data)
p2(data)
