lst = [55, 69, 77, 84, 10, 2, 60, 11, 4]

for i in range(1, len(lst)):
    current = lst[i]
    pos = i

    while current < lst[pos-1] and pos > 0:
        lst[pos] = lst[pos-1]
        pos = pos -1

    lst[pos] = current

print(lst)
