sheeps_size = [5, 7, 90, 300, 24, 50, 75]
for month in range(4):
    print('month', month)
    for index, item in enumerate(sheeps_size):
        # sheeps_size[index] = item + 50
        sheeps_size[index] += 50
    print(sheeps_size)
    max_size = 0
    for size in sheeps_size:
        if size > max_size:
            max_size = size
    max_size_index = sheeps_size.index(max_size)
    sheeps_size[max_size_index] = 8
    print(sheeps_size)
    print('one month passed')
total = 0
for item in sheeps_size:
    total += item
print(total)
print(total * 2)
