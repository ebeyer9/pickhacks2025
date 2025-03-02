import random

grid = [['0']*20 for i in range (20)]
display_grid = [['N']*20 for i in range (20)]


def generate_board():
    #Randomly Generate Bomb Tiles
    bomb_num = 100

    while(bomb_num > 0):
        row = random.randint(0, 19)
        column = random.randint(0, 19)

        if grid [row] [column] != 'b':
            grid [row] [column] = 'b'
            bomb_num-=1

def break_board(row, column):
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
                display_grid [row + i] [column + j] = 'Y'
            
            for k in range(-1, 2, 1):
                for l in range(-1, 2, 1):
                    if row + i + k < 0 or column + j + l < 0 or row + i + k > 19 or column + j + l > 19:
                        continue
                    elif grid[row + i + k][column + j + l] == 'b':
                        grid[row + i + k][column + j + l] = '0'
                        b_counter+=1

                

    #Put Bombs Back In
    while(b_counter > 0):
        row = random.randint(0, 19)
        column = random.randint(0, 19)
        dont_place = False

        if grid[row][column] == '0':
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if row + i < 0 or column + j < 0 or row + i > 19 or column + j > 19:
                        continue
                    elif grid[row + i][column + j] == '.':
                        dont_place = True
            if dont_place == False:
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
    unveil()


def unveil():
    do_it_again = True
    while do_it_again == True:
        do_it_again = False
        for i in range(20):
            for j in range(20):
                if grid[i][j] == '.' and display_grid[i][j] == 'Y':
                    for k in range(-1, 2, 1):
                        for l in range(-1, 2, 1):
                            if i + k < 0 or j + l < 0 or i + k > 19 or j + l > 19:
                                continue
                            elif display_grid[i+k][j+l] == 'Y':
                                continue
                            elif grid[i+k][j+l] != 'b':
                                display_grid[i+k][j+l] = 'Y'
                                do_it_again = True
                            else:
                                continue

def click(r, c):
    global display_grid
    if grid[r][c] == 'b':
        display_grid[r][c] = 'Y'
        print("You Fucking Suck")
    else:
        display_grid[r][c] = 'Y'
        unveil()

def return_symbol(r, c):
    if display_grid[r][c] == 'N':
        return 'N'
    else:
        return grid[r][c]

def check_win():
    counter = 0
    for i in range(20):
        for j in range(20):
            if display_grid[i][j] == 'b' or display_grid[i][j] == 'N':
                counter = counter + 1
    print("Counter")
    print(counter)
    if counter == 100:
        return True
    else:
        return False


def print_board():
    for i in range(20):
        for j in range(20):
            if display_grid[i][j] == 'N':
                print('$', end = " ")
            else:
                print(grid[i][j], end = " ")
        print()

# print_board()

# print()
# for i in range(20):
#     for j in range(20):
#         print(grid[i][j], end = " ")
#     print()