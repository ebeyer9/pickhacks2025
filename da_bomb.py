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

while(b_counter > 0):
    row = random.randint(0, 19)
    column = random.randint(0, 19)

    if grid [row] [column] == '0':
        grid [row] [column] = 'b'
        b_counter-=1

#Print Grid
for row in (grid):
    for column in (row):
        print(column, end = " ")
    print()