import aoc


data = """Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
data = aoc.get_str(17)
data = data.split('\n\n')
register = data[0].split('\n')
registers = {'A': int(register[0].split(': ')[1]), 'B': int(register[1].split(': ')[1]), 'C': int(register[2].split(': ')[1])}
init_registers = registers.copy()


programm = data[1].split(': ')[1]
programm = [int(x) for x in programm.split(',')]
programm_str = ','.join([str(p) for p in programm])

def combo(val):
    if 0 <= val <= 3:
        return val
    elif val == 4:
        return registers['A']
    elif val == 5:
        return registers['B']
    elif val == 6:
        return registers['C']
    else:
        print('invalid combo')
        exit(-1)
def adv(c):
    # writes in A
    registers['A'] = registers['A'] // (2**combo(c))
def bxl(c):
    registers['B'] =  c ^ registers['B']
def bst(c):
    # register B
    registers['B'] = combo(c) % 8
def jnz(c):
    # jump to c
    if registers['A'] == 0:
        return -1
    else:
        return c
def bxc(c):
    # write it register B
    registers['B'] =  registers['B'] ^ registers['C']
def out(c):
    return combo(c) % 8
def bdv(c):
    # writes in B
    registers['B'] = int(registers['A'] / (2**combo(c)))
def cdv(c):
    # writes in C
    registers['C'] = int(registers['A'] / (2**combo(c)))



opp = {0: adv, 1: bxl, 2: bst, 3:jnz, 4:bxc, 5: out, 6: bdv, 7: cdv}
output = {0: 'A', 1:'B', 2:'B', 3:'cnt', 4: 'B', 5: 'O', 6: 'B', 7: 'C'}
programcounter = 0
output = ''
print("start")
while True:
    if programcounter + 1 >= len(programm):
        print('end')
        print(output[:-1])
        break
    instruction = programm[programcounter]
    c = programm[programcounter + 1]
    if instruction == 3:
        cnt = opp[instruction](c)
        if cnt == -1:
            programcounter += 2
        else:
            programcounter = cnt
    elif instruction == 5:
        output += str(opp[instruction](c)) + ','
        programcounter += 2
    else:
        opp[instruction](c)
        programcounter += 2

def p2():
    # Reverse engineering
    pass
