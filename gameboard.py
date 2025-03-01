import random
size = 25

rows, cols = (size, size)

board = [[0 for i in range(cols)] for j in range(rows)]

num = 150

def print_board():
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
      

while(num > 0):
  x = random.randint(0,24)
  y = random.randint(0,24)
  if(board[x][y] != 1):
    board[x][y] = 1
    num -= 1
  
  else:
    continue
  



print_board()
