import random

# define constants
HIT = "X" 
MISS = "/" 
SHIP = "o"
EMPTY = "-"

# new_board() function returns a board (list of lists)
# default: returns 5x5 board
# param:: rows = int (optional). default value is 5
# param:: cols = int (optional). default value is 5

def new_board(rows=10, columns=10):
    return [[EMPTY]*columns for i in range(rows)]

# print_board() function prints board on the screen  
# param:: board = list of lists
# param:: secret = boolean. If True, displays any ships as empty spots.
def print_board(board, secret=False):
    for row in board:
        text = ''
        for cell in row:
          if secret and cell == SHIP:  # if board is secret, do not display ships
            cell = EMPTY
          text += cell
        print(text)

# place_ship() function places a battleship on the board.
# param:: board = list of lists 
# param:: row = int 
# param:: col = int 
# param:: ship_len = int 
# param:: direction = 'h' for horizontal or 'v' for vertical 
def place_ship(board, row, col, ship_len, direction):
    for i in range(ship_len): 
        board[row][col] = SHIP
        if direction == 'v': 
            row += 1
        elif direction == 'h':
            col += 1
    return True 

# place_random_ship() places a battleship randomly on the bot board. 
# param:: bot = list of lists
# param:: ship_len = int (optional). default value = 3
def place_random_ship(board, ship_len=3):
    n_rows, n_cols = len(board), len(board[0])  # number of rows & columns
    max_row, max_col = n_rows - 1, n_cols - 1     # max index for rows & columns
    
    direction = random.choice(["h", "v"])       # random direction (horizontal or vertical)
    if direction == "h":      # horizontal
        max_col -= ship_len 
    else:                     # vertical  
        max_row -= ship_len 
    
    row = random.randint(0,max_row)
    col = random.randint(0, max_col)
    place_ship(board, row, col, ship_len, direction) 

# valid_move() returns True if a row/column pair is a valid spot on board
# param:: board = list of lists
# param:: row = int
# param:: col = int

def valid_move(board, row, col): 
  return row < len(board) and row >= 0 and col < len(board[0]) and col >= 0
  
# check_validity() returns True if a row/col pair is a valid 
#   starting point for battleship on board
# param:: board = list of lists
# param:: row, col = int 
# param:: ship_len = int (optional). default value is 3
# param:: direction = string (optional)
# "v" for vertical, "h" for horizontal. default value is "h"

def check_validity(board, row, col, ship_len=3, direction="h"):
  if direction == 'v': 
    row += ship_len 
  elif direction == 'h': 
    col += ship_len 
  return valid_move(board, row, col) 

# place_user_ship() places a ship on the board
# param:: board = list of lists
# param:: ship_len = int 

def place_user_ship(board, ship_len):
    print("\nPlace your battleship. The ship is {} units long.".format(ship_len))
    placed = False
    while not placed: 
      d = input("Horizontal or vertical? Type 'h' or 'v': ")
      if not (d == 'h' or d == 'v'): 
        continue 
      print("Choose starting point of your battleship.")
      row = int(input("Row: "))
      col = int(input("Column: "))
      if not check_validity(board, row, col, ship_len, d): 
        print("Your ship is off the board! Pick again.")
        continue
      placed = place_ship(board, row, col, ship_len, d) 

# count_hits() returns number of hits on board
# param:: board = list of lists

def count_hits(board): 
  hits = [x for row in board for x in row if x == HIT]
  return len(hits)


# user_move function checks if user guess hits bot ship (checks secret_bot)
# updates display_bot and returns it. 
# param:: secret_bot (list of lists)
# param:: display_bot (list of lists)

def user_move(bot):
  print("Where do you want to attack opponent?")
  row = int(input("Row:"))
  col = int(input("Col:"))
  if not valid_move(bot, row, col): 
    print("Invalid. You must pick a spot on the board.")
  elif bot[row][col] == SHIP:
    print("HIT")
    bot[row][col] = HIT
  else: 
    print("Miss")
    bot[row][col] = MISS
  return bot

# gets a random guess for the bot 
# param:: user (list of lists)
def bot_move(user_board):
  n_rows, n_cols = len(user_board), len(user_board[0])
  row = random.randint(0, n_rows-1)   # random row
  col = random.randint(0, n_cols-1)   # random col 
  print ("Computer attacks the point: ({}, {})".format(row,col))
  if user_board[row][col] == SHIP:
    print("HIT")
    user_board[row][col] = HIT
  else: 
    print("Miss")
    user_board[row][col] = MISS
  return user_board
