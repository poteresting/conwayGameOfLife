import random, copy, time

nextcell = []

for y in range(20):
    my_list = []
    for x in range(80):
        if random.randint(0, 1) == 0:
            my_list.append('1')
        else:
            my_list.append('0')
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
            if current[y][left] == '1':
                neighbor += 1
            if current[y][right] == '1':
                neighbor += 1
            if current[up][x] == '1':
                neighbor += 1
            if current[down][x] == '1':
                neighbor += 1
            if current[up][left] == '1':
                neighbor += 1
            if current[down][left] == '1':
                neighbor += 1
            if current[up][right] == '1':
                neighbor += 1
            if current[down][right] == '1':
                neighbor += 1

            if current[y][x] == '1' and (neighbor == 2 or neighbor == 3):
                nextcell[y][x] = '1'
            elif current[y][x] == '0' and neighbor == 3:
                nextcell[y][x] = '1'
            else:
                nextcell[y][x] = '0'
    time.sleep(1)
