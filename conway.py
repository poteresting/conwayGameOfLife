import random, copy, time

nextcell = []

for y in range(20):
    my_list = []
    for x in range(80):
        if random.randint(0, 1) == 0:
            my_list.append('O')
        else:
            my_list.append('.')
    nextcell.append(my_list)

while True:
    print('\n\n\n\n\n\n')
    
    for y in range(20):
        for x in range(80):
            print(nextcell[y][x], end='')
        print()
    current = copy.deepcopy(nextcell)

    for y in range(20):
        for x in range (80):
            neighbor = 0
            left = (x-1) % 80
            right = (x+1) % 80
            up = (y-1) % 20
            down = (y+1) % 20
            if current[y][left] == 'O':
                neighbor += 1
            if current[y][right] == 'O':
                neighbor += 1
            if current[up][x] == 'O':
                neighbor += 1
            if current[down][x] == 'O':
                neighbor += 1
            if current[up][left] == 'O':
                neighbor += 1
            if current[down][left] == 'O':
                neighbor += 1
            if current[up][right] == 'O':
                neighbor += 1
            if current[down][right] == 'O':
                neighbor += 1

            if current[y][x] == 'O' and (neighbor == 2 or neighbor == 3):
                nextcell[y][x] = 'O'
            elif current[y][x] == '.' and neighbor == 3:
                nextcell[y][x] = 'O'
            else:
                nextcell[y][x] = '.'
    time.sleep(1)