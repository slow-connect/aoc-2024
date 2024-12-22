import aoc
from functools import lru_cache
from collections import Counter

init_numbers = aoc.get_int(22)
# init_numbers = [1, 2, 3, 2024]

def mix(rev, current):
    return rev ^ current
def prune(num):
    return num % 16777216

def first(num):
    t = num * 64
    return prune(mix(num, t))
def second(num):
    t = num // 32
    return prune(mix(num, t))
def third(num):
    t = num * 2048
    return prune(mix(num, t))

# @lru_cache(maxsize=None)
def sequence(num):
    return third(second(first(num)))

print('Part 1:')
secrets = Counter(init_numbers)
cnt = 0
for n in secrets.keys():
    val = n
    for _ in range(2000):
        val = sequence(val)
    cnt += secrets[n] * val
print(cnt)

print('Part 2:')
secrets = Counter(init_numbers)
sequences = {}
stringify = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', -1: 'a', -2: 'b', -3: 'c', -4: 'd', -5: 'e', -6: 'f', -7: 'g', -8: 'h', -9: 'i'}
destringify = {v:k for k, v in stringify.items()}
memo = set()
for n in secrets.keys():
    prev_val = n
    s = ''
    lst = []
    for _ in range(2000):
        val = sequence(prev_val)
        diff = (val % 10) - (prev_val % 10)
        s += stringify[diff]
        lst.append((diff, val % 10))
        prev_val = val
    sequences[n] = (lst, s)

# @lru_cache(maxsize=None)
def count_rewards(sequence):
    cnt = 0
    for n in sequences.keys():
        lst, s = sequences[n]
        i = s.find(sequence)
        if i > -1:
            cnt += secrets[n] * lst[i+len(sequence)-1][1]
    return cnt

best_cnt = 0
best_sqc = ''
for n in sequences.keys():
    lst, s = sequences[n]
    for i in range(1996):
        sqc = s[i:i+4]
        if sqc not in memo:
            memo.add(sqc)
            cnt = count_rewards(sqc)
            if cnt > best_cnt:
                best_cnt = cnt
                best_sqc = sqc
print(best_cnt)
# s = [destringify[s] for s in best_sqc]
# print(s)
