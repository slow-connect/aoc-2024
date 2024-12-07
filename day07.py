import aoc

data = aoc.get_lst(7)[:-1]
data = [d.replace('\n', '') for d in data]


def p1(data):
    cnt = 0
    for l in data:
        opp = l.split(' ')
        res = int(opp[0][:-1])
        val = [int(opp[k]) for k in range(1, len(opp))]
        for i in range(2**(len(val))):
            s = bin(i)[2:].zfill(len(val))
            c = 0
            for j in range(len(s)):
                if s[j] == '1':
                    c += val[j]
                else:
                    if c == 0:
                        c = val[j]
                    else:
                        c *= val[j]
            if c == res:
                cnt += res
                break
    print(cnt)

def p2(data):
    cnt = 0
    for l in data:
        opp = l.split(' ')
        res = int(opp[0][:-1])
        val = [int(opp[k]) for k in range(1, len(opp))]
        for i in range(3**(len(val)+1)):
            t = i
            s = ''
            for j in range(len(val)):
                if t//3 % 3 == 0:
                    s += '+'
                elif t//3 % 3 == 1:
                    s += '*'
                elif t//3 % 3 == 2:
                    s += '|'
                t //= 3
            c = 0
            for j in range(len(val)):
                if s[j] == '+':
                    c += val[j]
                elif s[j] == '*':
                    if c == 0:
                        c = val[j]
                    else:
                        c *= val[j]
                elif s[j] == '|':
                    if c == 0:
                        c = val[j]
                    else:
                        c = int(str(c) + str(val[j]))
                if c > res:
                    break
            if c == res:
                cnt += res
                break
    print(cnt)
p1(data)
