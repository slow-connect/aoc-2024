import aoc

data = "2333133121414131402"
data = aoc.get_str(9)[:-1]
data = [int(x) for x in data]

def p1(data):
    filesystem = []
    empty_index = []
    storage = []
    k = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for _ in range(data[i]):
                storage.append(len(filesystem))
                filesystem.append(k)

            k += 1
        else:
            for _ in range(data[i]):
                empty_index.append(len(filesystem))
                filesystem.append('.')
    j = -1
    for i in range(len(filesystem)):
        if filesystem[i] == '.':
            filesystem[i] = filesystem[storage[j]]
            filesystem[storage[j]] = '.'
            j -= 1
        if i == len(storage) - 1:
            break

    checksum = 0
    for i in range(len(filesystem)):
        if filesystem[i] == '.':
            break
        checksum += filesystem[i] * i
    print(checksum)

def p2(data):
    files = dict()
    free_space = dict()
    file_id = 0
    disk_index = 0

    files[0] = [disk_index, data[0]]
    disk_index += data[0]
    file_id += 1

    for i in range(len(data)//2):
        free_space[disk_index] = data[i*2+1]
        disk_index += data[i*2+1]

        files[file_id] = [disk_index, data[i*2+2]]
        disk_index += data[i*2+2]
        file_id += 1

    free_index_sorted = sorted(free_space.keys())  # Sort the free space indices

    for f_id in reversed(range(1, len(data)//2 + 1)):
        for free_index in free_index_sorted:
            if free_index > files[f_id][0]:
                break
            if free_space[free_index] == files[f_id][1]:
                files[f_id][0] = free_index
                del free_space[free_index]
                free_index_sorted = sorted(free_space.keys())
                break
            elif free_space[free_index] > files[f_id][1]:
                files[f_id][0] = free_index
                free_space[free_index + files[f_id][1]] = free_space[free_index] - files[f_id][1]
                del free_space[free_index]
                free_index_sorted = sorted(free_space.keys())
                break

    check_sum = 0
    for this_file in files:
        idx, length = files[this_file]
        for i in range(idx, idx + length):
            check_sum += this_file * i
    print(check_sum)

p1(data)
p2(data)
