import random, copy, time

nextcell = []

for y in range(23):
    my_list = []
    for x in range(80):
        if random.randint(0, 1) == 0:
            my_list.append('o')
        else:
            my_list.append(' ')
    nextcell.append(my_list)

while True:
    print('\n\n\n\n\n\n')
    
    for y in range(23):
        for x in range(80):
            print(nextcell[y][x], end='')
        print()
    current = copy.deepcopy(nextcell)

    for y in range(23):
        for x in range (80):
            neighbor = 0
            left = (x-1) % 80
            right = (x+1) % 80
            up = (y-1) % 23
            down = (y+1) % 23
            if current[y][left] == 'o':
                neighbor += 1
            if current[y][right] == 'o':
                neighbor += 1
            if current[up][x] == 'o':
                neighbor += 1
            if current[down][x] == 'o':
                neighbor += 1
            if current[up][left] == 'o':
                neighbor += 1
            if current[down][left] == 'o':
                neighbor += 1
            if current[up][right] == 'o':
                neighbor += 1
            if current[down][right] == 'o':
                neighbor += 1

            if current[y][x] == 'o' and (neighbor == 2 or neighbor == 3):
                nextcell[y][x] = 'o'
            elif current[y][x] == ' ' and neighbor == 3:
                nextcell[y][x] = 'o'
            else:
                nextcell[y][x] = ' '
    time.sleep(0.2)
