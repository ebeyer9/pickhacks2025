import random

grid = [['0']*20 for i in range (20)]

#Randomly Generate Bomb Tiles
bomb_num = 150

while(bomb_num > 0):
    row = random.randint(0, 19)
    column = random.randint(0, 19)

    if grid [row] [column] != 'b':
        grid [row] [column] = 'b'
        bomb_num-=1

#Exterminate Starting Point
row = random.randint(0, 19)
column = random.randint(0, 19)
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

for i in range(19):
    for j in range(19):
        if grid[i][j] == '.' or grid[i][j] == 'b':
            continue
        else:
            for k in range(-1, 2, 1):
                for l in range(-1, 2, 1):
                    if i + k < 0 or j + l < 0 or i + k > 19 or j + l > 19:
                        continue
                    elif grid[i+k][j+l]:




#Print Grid
for row in (grid):
    for column in (row):
        print(column, end = " ")
    print()