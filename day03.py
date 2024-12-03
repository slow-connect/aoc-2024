import aoc
import re

input = aoc.get_str(3)
def p1(input):
    substr = r'mul\(\d+,\d+\)'
    matches = re.findall(substr, input)
    res = 0
    for match in matches:
        a, b = match.replace('mul(', '').replace(')', '').split(',')
        res += int(a)*int(b)
    print(res)

def p2(input):
    multiply = True
    substr = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(substr, input)
    res = 0
    for match in matches:
        if match == "don't()":
            multiply = False
            pass
        elif match == 'do()':
            multiply = True
            pass
        else:
            if multiply:
                a, b = match.replace('mul(', '').replace(')', '').split(',')
                res += int(a)*int(b)
    print(res)

p1(input)
p2(input)
