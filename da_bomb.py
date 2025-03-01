import random

grid = [['0']*20 for i in range (20)]
display_grid = [['N']*20 for i in range (20)]

def generate_board():
    #Randomly Generate Bomb Tiles
    bomb_num = 150

    while(bomb_num > 0):
        row = random.randint(0, 19)
        column = random.randint(0, 19)

        if grid [row] [column] != 'b':
            grid [row] [column] = 'b'
            bomb_num-=1

def first_click(row, column):
    #Exterminate Starting Point
    b_counter = 0

    for i in range (-2, 3, 1):
        for j in range (-2, 3, 1):
            if row + i < 0 or column + j < 0 or row + i > 19 or column + j > 19:
                continue
            else:
                if grid [row + i] [column + j] == 'b':
                    b_counter+=1
                grid [row + i] [column + j] = '.'

    #Put Bombs Back In
    while(b_counter > 0):
        row = random.randint(0, 19)
        column = random.randint(0, 19)

        if grid[row][column] == '0':
            grid[row][column] = 'b'
            b_counter-=1

    #Fill Rest of Grid
    num_counter = 0

    for i in range(20):
        for j in range(20):
            if grid[i][j] == '.' or grid[i][j] == 'b':
                continue
            else:
                for k in range(-1, 2, 1):
                    for l in range(-1, 2, 1):
                        if i + k < 0 or j + l < 0 or i + k > 19 or j + l > 19:
                            continue
                        elif grid[i+k][j+l] == 'b':
                            num_counter+=1
                        else:
                            continue

                if num_counter == 0:
                    grid[i][j] = '.'
                else:
                    grid[i][j] = num_counter
                num_counter = 0
    






def print_board():
    for i in range(20):
        for j in range(20):
            if display_grid[i][j] == 'N':
                print('$', end = " ")
            else:
                print(grid[i][j], end = " ")
        print()