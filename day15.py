import aoc

data = aoc.get_str(15)
# data = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
# data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""
map, seq = data.split('\n\n')
map = map.split('\n')
map = [list(x) for x in map]
seq = seq.replace('\n', '')

start = (-1, -1)
boxes = set()
walls = set()
for x in range(len(map)):
    for y in range(len(map[x])):
        if map[x][y] == '@':
            map[x][y] = '.'
            start = (x, y)
        if map[x][y] == 'O':
            boxes.add((x, y))
        if map[x][y] == '#':
            walls.add((x, y))


get_dir = {'^': (-1, 0),  '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
def get_gps(x, y):
    return 100*x + y

def print_map(robot, boxes, walls):
    xs = set(w[0] for w in walls)
    ys = set(w[1] for w in walls)

    grid = [['.' for _ in range(max(xs)+1)] for _ in range(max(ys)+1)]

    for w in walls:
        grid[w[0]][w[1]] = '#'
    for b in boxes:
        grid[b[0]][b[1]] = 'O'

    grid[robot[0]][robot[1]] = '@'

    for y, l in enumerate(grid):
        print(f"{y:02d}", end=" ")
        print(''.join(l))



x, y = start
for s in seq:
    dx, dy = get_dir[s]
    nx, ny = x + dx, y + dy
    if (nx, ny) not in walls:
        if (nx, ny) not in boxes:
            x, y = nx, ny
        else:
            cx, cy = nx, ny
            while True:
                if (cx, cy) in walls:
                    cx, cy = -1, -1
                    break
                if (cx, cy) in boxes:
                    cx, cy = cx + dx, cy + dy
                else:
                    break
            if cx != -1 and cy != -1:
                to_add, to_remove = set(), set()
                for box in boxes:
                    sequence_x, sequence_y = [x, cx], [y, cy]
                    if (min(sequence_x) <= box[0] <= max(sequence_x)) and (min(sequence_y) <= box[1] <= max(sequence_y)):
                        to_add.add((box[0] + dx, box[1] + dy))
                        to_remove.add(box)
                boxes -= to_remove
                boxes |= to_add

                x, y = x+dx, y+dy
    # print_map((x, y), boxes, walls)

res = 0
for box in boxes:
    res += get_gps(*box)
print(res)
