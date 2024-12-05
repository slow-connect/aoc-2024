import aoc

data = aoc.get_lst(5)
data = [s.strip() for s in data]
page_order = []
updates = []
e = False
for line in data:
    if line == '':
        e = True
    elif e:
        updates.append(line)
    else:
        page_order.append(line.split('|'))

page_dict = {}
for i in range(len(page_order)):
    if page_order[i][0] not in page_dict:
        page_dict[page_order[i][0]] = [page_order[i][1]]
    else:
        page_dict[page_order[i][0]].append(page_order[i][1])


cnt_p1 = 0
cnt_p2 = 0
for l in updates:
    inOrder = True
    order = l.split(',')
    n = 0
    for num in order:
        if num in page_dict:
            for i in range(n):
                if order[i] in page_dict[num]:
                    inOrder = False
                    break
        n += 1
    if inOrder:
        cnt_p1 += int(order[len(order) // 2])
    else:
        n = 0
        while (n < len(order)):
            if order[n] in page_dict:
                for i in range(n):
                    if order[i] in page_dict[order[n]]:
                        order[n], order[i] = order[i], order[n]
                        n=-1
                        break
            n += 1
        cnt_p2 += int(order[len(order) // 2])
print(cnt_p1)
print(cnt_p2)
