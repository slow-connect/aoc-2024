import aoc

input = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""".split('\n\n')
input = [s.split('\n') for s in input]

input = aoc.get_lst_of_lst(24)

def und(a, b): return a & b
def oder(a, b): return a | b
def xor(a, b): return a ^ b

fun = {'AND': und, 'OR': oder, 'XOR': xor}

state, circuit = input
state = [s.split(': ') for s in state]
state = {s[0]: int(s[1]) for s in state}
state = dict(state)

circuit = [c.split(' ') for c in circuit]

def part1(circuit, state):
    while len(circuit) > 0:
        new_circuits = []
        for c in circuit:
            if (c[0] in state) and (c[2] in state):
                state[c[4]] = fun[c[1]](state[c[0]], state[c[2]])
            else:
                new_circuits.append(c)
        circuit = new_circuits
    output = {}
    cnt = 0
    x, y = 0, 0
    out = [0 for key in state.keys() if key[0] == 'z']
    x_b, y_b = [0 for key in state.keys() if key[0] == 'x'], [0 for key in state.keys() if key[0] == 'y']
    for k, v in state.items():
        if k[0] == 'z':
            output[k] = v
            out[int(k[1:])] = v
            cnt += v * 2**int(k[1:])
        if k[0] == 'x':
            x += v * 2**int(k[1:])
            x_b[int(k[1:])] = v
        if k[0] == 'y':
            y += v * 2**int(k[1:])
            y_b[int(k[1:])] = v
    a = ''.join([str(i) for i in x_b])
    b = ''.join([str(i) for i in y_b])
    c = ''.join([str(i) for i in out])
    a = int(a, 2)
    b = int(b, 2)
    c = int(c, 2)
    print(cnt)

# part1(circuit, state)6

print('Part 2')
## from paper and pencil
changes = {'z05': 'frn', 'frn': 'z05', 'wtt': 'z39', 'z39': 'wtt', 'vtj': 'wnf', 'wnf':'vtj', 'gmq': 'z21', 'z21': 'gmp'}

l = []
for k, v in changes.items():
    l.append(k)

l = sorted(l)
print(','.join(l))
