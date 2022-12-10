#!/bin/python3
from helper import (new_board, print_board, place_random_ship, place_user_ship, user_move, bot_move, count_hits)
from draw import draw_boards
from random import randint

# define constants
miss="q"
hit ="w"
ship="e"
empty="r"

# create boards for user and bot. 
user=new_board()
bot=new_board()



# place random ship for bot (and user).  
ship_lenth=3
place_user_ship(user,ship_lenth)
place_random_ship(bot,ship_lenth)
# create a function to capture the user's move
def user_move(bot):
  print("Which point  do want to attac k your apponent")
  row=int(input("row:"))
  col=int(input("colum:"))

# create a function to capture the bot's move
  
  if bot[row][col]==ship: 
    print("SHIP SUNKIN")
    bot[row][col]=hit
# repeat game code: 
while True:
  user_move(bot)
  draw_boards(bot,user)
  bot_move(user)
  draw_boards(bot,user)
  # draw boards for bot and user (hint: can use draw_boards() in draw.py) 
  

  # get user move 
  
  
  # get bot move 
  
  
  # break loop if bot hits or user hits are greater than battleship size
  
  


