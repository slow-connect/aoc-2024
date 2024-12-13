import aoc

def det(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def inv(A):
    d = 1.0 / det(A)
    return [[A[1][1]*d, -A[0][1]*d], [-A[1][0]*d, A[0][0]*d]]
def mul(A, p):
    return [A[0][0]*p[0] + A[0][1]*p[1], A[1][0]*p[0] + A[1][1]*p[1]]
def nearest_int(x, max_diff=0.1):

    x0 = int(x)
    if x - x0 < max_diff:
        return x0
    if x - x0 > 1 - max_diff:
        return x0 + 1
    return -1

data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split('\n\n')
data = [s.split('\n') for s in data]
# print(data)
data = aoc.get_lst_of_lst(13)

def part1(data):
    shift = 0
    cost = 0
    for game in data:
        b1 = game[0]
        b2 = game[1]
        prize = game[2]
        b1 = b1.split(': ')[1]
        b2 = b2.split(': ')[1]
        prize = prize.split(': ')[1]
        b1 = b1.split(', ')
        b2 = b2.split(', ')
        prize = prize.split(', ')
        b1 = [int(b1[0][2:]), int(b1[1][2:])]
        b2 = [int(b2[0][2:]), int(b2[1][2:])]
        prize = [shift + int(prize[0][2:]), shift + int(prize[1][2:])]
        B = [[b1[0], b2[0]], [b1[1], b2[1]]]
        a, b = mul(inv(B), prize)
        if abs(a - round(a)) < 1E-8  and abs(b - round(b)) < 1E-8:
            cost += 3*int(round(a)) + int(round(b))
    print(cost)
part1(data)

def part2(data):
    shift = 10000000000000
    cost = 0
    for game in data:
        b1 = game[0]
        b2 = game[1]
        prize = game[2]
        b1 = b1.split(': ')[1].split(', ')
        b2 = b2.split(': ')[1].split(', ')
        prize = prize.split(': ')[1].split(', ')
        b1 = [int(b1[0][2:]), int(b1[1][2:])]
        b2 = [int(b2[0][2:]), int(b2[1][2:])]
        prize = [shift + int(prize[0][2:]), shift + int(prize[1][2:])]
        B = [[b1[0], b2[0]], [b1[1], b2[1]]]
        a, b = mul(inv(B), prize)
        na, nb = nearest_int(a, max_diff=1e-3), nearest_int(b, max_diff=1e-3)
        if na >= 0 and nb >= 0:

            cost += 3*na + nb
    print(cost)
part2(data)
