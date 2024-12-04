import aoc

data = aoc.get_lst(4)[:-1]

def p1(data):
    cnt = 0
    sumstr = "XMAS"
    for i in range(len(data)):
        cnt += data[i].count(sumstr)
        cnt += data[i][::-1].count(sumstr)
    for i in range(len(data[0])):
        tmp = "".join([data[k][i] for k in range(len(data))])
        cnt += tmp.count(sumstr)
        cnt += tmp[::-1].count(sumstr)
    x, y = len(data), len(data[0])
    for i in range(x+y-1):
        tmp = "".join([data[i-k][k] for k in range(i+1) if i-k < x and k < y])
        cnt += tmp.count(sumstr)
        cnt += tmp[::-1].count(sumstr)
    for i in range(max(x, y)):
        tmp = "".join([data[i+k][k] for k in range(x-i)])
        cnt += tmp.count(sumstr)
        cnt += tmp[::-1].count(sumstr)
        if i > 0:
            tmp = "".join([data[k][i+k] for k in range(y-i)])
            cnt += tmp.count(sumstr)
            cnt += tmp[::-1].count(sumstr)
    print(cnt)


def p2(data):
    cnt = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == 'A':
                if   data[i-1][j-1] == "M" and data[i+1][j+1] == "S" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    cnt += 1
                elif data[i-1][j-1] == "M" and data[i+1][j+1] == "S" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                    cnt += 1
                elif data[i-1][j-1] == "S" and data[i+1][j+1] == "M" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    cnt += 1
                elif data[i-1][j-1] == "S" and data[i+1][j+1] == "M" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                    cnt += 1
    print(cnt)
p2(data)
