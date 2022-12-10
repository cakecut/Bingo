import turtle 
from helper import HIT, MISS, SHIP, EMPTY

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("pink")
t.up()
t.ht()
t.speed(0)
#t.tracer(1, 3)
t.color("black")

# display_board() returns list with updated characters  
# param:: board = list of lists
# param:: secret = boolean. If True, changes any ships into empty spots.

def display(board, secret=False):
    d = []
    for row in board:
        r = []
        for x in row:
          if secret and x == SHIP:  # if board is secret, do not display ships
            x = EMPTY
          cell = x
          r.append(cell)
        d.append(r) 
    return d

# draw_rect() draws a rectangle 
# param:: l = int (length) 
# param:: w = int (width)
def draw_rect(l, w): 
  t.begin_fill()
  for i in range(2): 
    t.forward(l)
    t.left(90)
    t.forward(w)
    t.left(90)
  t.end_fill()
  
  
def draw_hit(gap=20): 
    t.color('red')
    t.forward(gap/4)
    t.write(HIT, align="center", font=("Arial", 15, "bold"))
    t.color('white')
    t.backward(gap/4)
    
def draw_ship(gap=20): 
    t.color('orange')
    draw_rect(gap*2/3, gap*2/3)
    t.color('white')

def draw_board(board, secret=False):
    board = display(board, secret) 
    n_rows, n_cols = len(board), len(board[0])
    gap=20
    
    # draw column numbers
    t.forward(gap)
    for i in range(n_cols):
        t.write(i)
        t.forward(gap)
    t.backward(gap*(n_cols+1))
    
    # draw each row 
    for i in range(n_rows):
        t.right(90)
        t.forward(gap)          
        t.left(90)
        t.write(i)                      
        t.forward(gap)
        for j in range(n_cols):
            n = board[i][j]
            if n == HIT: 
              draw_hit(gap)
            elif n == SHIP: 
              draw_ship(gap)
            elif n == MISS: 
              t.dot(gap/3)
            else: 
              t.write(n)
            t.forward(gap)
        t.backward(gap*(n_cols+1))

# draw_text() draws large text on the screen 
def draw_text(text):
    t.write(text, align="center", font= ("Arial", 10, "bold")) 

# draw_boards() draws boards for the user and bot
def draw_boards(bot, user):
    t.clear()
    t.goto(0, 180)
    draw_text("Computer") 
    t.goto(-80, 150)
    draw_board(bot, True)   
    t.goto(0, -20)
    draw_text("You") 
    t.goto(-80, -50)
    draw_board(user)