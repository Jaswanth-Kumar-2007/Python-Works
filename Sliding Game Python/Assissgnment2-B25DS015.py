'''
Sliding Game Python
#Name : Jaswanth Kumar Kamireddi
#ID No. : B25DS015
#Branch : DSAI
'''

'''
Requirements
# pip install Pythonturtle random2 os-sys pypi-json
'''
#pip install Pythonturtle
import turtle
#pip install random2
import random
#pip install os-sys
import os
#pip install pypi-json
import json

'''
Beginning of the Screen
'''
#Screen Output Start
s = turtle.Turtle()
s.screen.bgcolor("LightSkyBlue")
s.screen.title("15 Sliding Game")
s.pencolor("Black")
s.fillcolor("Yellow")
s.hideturtle()
s.penup()
s.width(4)
s.goto(-50,-50)
s.pendown()
s.begin_fill()
for i in range(6):
    s.forward(100)
    s.left(60)
s.width(0)
s.end_fill()
s.penup()
s.goto(-80, 0)
s.write("Welcome", font=("Arial", 36, "bold"))

'''
Turtle Delays some Time from Start Screen to Name Input
'''
#Wait Until Some Time
turtle.delay(3000)

turtle.clearscreen()

'''
Defining New Turtle for Screen and Square
'''
#Define Turtle and Start Square
j = turtle.Turtle()
j.screen.bgcolor("Black")
j.pencolor("#00ff00")

'''
Input Your Name
'''
#Enter Name
name = []
name = turtle.textinput("Welcome to Sliding Game:", "Enter your Name")

'''
Function : name_saver
Makes the Names to store in name_data.json file
'''
#Saves All the Name of Players
def name_saver():
    global names
    names.append(name)
    n = {"name" : names}
    with open("name_data.json","w") as t:
        json.dump(n,t)
 
'''
Function : name_loader
Makes the Names to load out from file
'''
#Loads the Player Names
def name_loader():
    global names
    names = [] 
    with open("name_data.json","r") as t:
        n = json.load(t)
    names =  n["name"]

'''
Checks the Name of the File is there and procced through Next Command
'''
# CHeck the First Time or Not (File Created or Not)
file = "name_data.json"
if os.path.exists(file):
    name_loader()
    name_saver()
    namep = list(set(names))
else:
    names = []
    name_saver()
    namep = list(set(names))

'''
Input of Difficulty and Difficulty Patterns Predefined (Got from Real Game Environment)
'''
#Selection of Easy , Medium , Hard Sets from these 4 Sets
difficulty = turtle.textinput("Welcome to Sliding Game:","Enter Difficulty E/M/H")
easy1 = ['A','B','C','D','E','G','O','H','I','J','F','K','M','N',None,'L']
easy2 = ['A','B','C','D','E','F','G','H','M','J','K','L','N',None,'I','O']
easy3 = ['A','B','C','D','E','F','G','H','M','J','K','L','N','I',None,'O']
easy4 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',None,'N','O']
medium1 = ['A','B','H','C','E','F','D','L','J','N','M','K','I','O',None,'G']
medium2 = ['A','B','C','D','E','I','F','L','J','N','M','K','G','H',None,'O']
medium3 = ['A','B','C','D','E','F','L','H','J','N','M','K','I','G',None,'O']
medium4 = ['A','B','G','N','I','E','C','H','M','K','O','F',None,'J','L','D']
hard1 = ['F','E','B','D','A','C','L','G','N','M',None,'H','K','J','I','O']
hard2 = ['E','D','C','H','A','K','G','L','F','N','B','I','M','J','O',None]
hard3 = ['B','A','D',None,'E','K','C','L','M','J','F','O','N','I','H','G']
hard4 = ['C','E','B','D','A','G','L','H','N','M',None,'F','K','J','O','I']

'''
Selects the Difficulty Arrangement Randomly
'''
#Finds Easy , Medium , Hard from the 4 sets
easy = random.choice([easy1,easy2,easy3,easy4])
medium = random.choice([medium1,medium2,medium3,medium4])
hard = random.choice([hard1,hard2,hard3,hard4])

'''
turtle conditions defined
'''
#Initiation of Turtle
turtle.delay(0)
j.width(4)
j.speed(0)
j.penup()
j.goto(-200,-200)
j.pendown()

'''
Function : grid_drawer
#Draws the Sqaure
'''
#Square Outline Draw
def grid_drawer():
    for i in range(4):
       j.forward(400)
       j.left(90)

    
    for i in range(4):
       j.setheading(0)
       j.forward(100)
       if(i%2 == 0):
           j.left(90)
       else:
           j.right(90)
       j.forward(400)
    
       
    j.setheading(90)
    

    for i in range(4):
       j.forward(100)
       if(i%2 == 0):
           j.left(90)
       else:
           j.right(90)
       j.forward(400)
       j.setheading(90)
       
#Square initiation
grid_drawer()


#Storage For Saving Moves
j.width(None)
global storage
storage = []

'''
Assigning Numbers to Only this Respective Positions
'''
#Assigning Points
points = [(-150,150),(-50,150),(50,150),(150,150),(-150,50),(-50,50),(50,50),(150,50),(-150,-50),(-50,-50),(50,-50),(150,-50),(-150,-150),(-50,-150),(50,-150),(150,-150)]

'''
#numbers = list(range(1,17))
#alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',None]
#alphabets = ["अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ","औ","अं","अः","क","ख",None]
#alphabets = ["అ","ఆ","ఇ","ఈ","ఉ","ఊ","ఋ","ౠ","ఎ","ఏ","ఐ","ఒ","ఓ","ఔ","అం",None]
#random.shuffle(numbers)
#random.shuffle(alphabets)
'''

'''
Defines the CheckPoint Variables
'''
board = {}
empty_pos = None
timecounter = 0

'''
Function : Leaderboard
Prints the LeaderBoard By Keeping the Played members in Respective Difficulty and Time Order
'''
#Leaderboard Function
def leaderboard():
    global p
    p = 1
    turtle.clearscreen()
    y = turtle.Turtle()
    y.hideturtle()
    y.screen.bgcolor("White")
    y.pencolor("Black")
    y.penup()
    y.goto(-150, 180)
    y.write("LEADERBOARD ", font=("Arial", 36, "bold"))

    leaderboarddata = []
    
    for i in namep:
         file = f"{i}.json"
         if os.path.exists(file):
              with open(file, "r") as t:
                  d = json.load(t)
              board_data = {eval(pos): val for pos, val in d["board"].items()}
              timecounter = d.get("timecount", 0)
              difficulty = d.get("difficulty", "Easy")
              leaderboarddata.append({
                "name": i,
                "time": timecounter,
                "difficulty": difficulty
              })
    
    difficulty_order = {"Easy": 1, "Medium": 2, "Hard": 3}
    leaderboarddata.sort(key=lambda x: (difficulty_order.get(x["difficulty"], 0), x["time"]))
    # Display leaderboard
    h = 140
    SNo = 1
    for entry in leaderboarddata:
        y.goto(-250, h)
        # Format time as MM:SS
        min = entry['time'] // 60
        sec = entry['time'] % 60
        formatted_time = f"{min:02}:{sec:02}"

        y.write(f"{SNo}., Name: {entry['name']}, Time: {formatted_time}, Mode: {entry['difficulty']}",
                font=("Arial", 20, "bold"))
        h -= 40
        SNo += 1

'''
Function : l_checkpoint
#It Opens the Checkpoint
'''
def l_point():
    global board
    file = f"{name}.json"
    if os.path.exists(file):
        with open(file, "r") as t:
            d = json.load(t)
        board = {eval(pos): val for pos, val in d["board"].items()}
    else:
        pass   
               
#Selection of Diificulty and Assigning of Difficulty
global q
q = "Difficulty"

if os.path.exists(f"{name}.json"):
    choice = turtle.textinput("Checkpoint Found", "Do you want to continue? (Y/N)")
    if  choice in  ('Y','y'):
        l_point()
    else:
        if difficulty in ('E', 'e'):
            q = "Easy"
            alphabets = easy
        elif difficulty in ('M', 'm'):
            q = "Medium"
            alphabets = medium
        elif difficulty in ('H', 'h'):
            q = "Hard"
            alphabets = hard
        else:
            turtle.bye()
        board = dict(zip(points, alphabets))
else:
    if difficulty in ('E', 'e'):
        q = "Easy"
        alphabets = easy
    elif difficulty in ('M', 'm'):
        q = "Medium"
        alphabets = medium
    elif difficulty in ('H', 'h'):
        q = "Hard"
        alphabets = hard
    else:
        turtle.bye()
    board = dict(zip(points, alphabets))

'''
Starts Assigns the Numbers For Every Position there will
Be Defined New Turtle
'''
#Assign Alphabets(or Numbers) to a Position
writers = {}
for (x,y),num in board.items():
    k = turtle.Turtle()
    k.pencolor("#00ff00")
    k.hideturtle()
    k.speed(0)
    k.penup()
    k.goto(x,y)
    k.pendown()
    #num != 16
    if num is not None :
        k.write(num,font =("Arial",18,"bold"))
    else:
        empty_pos = (x,y)
    writers[(x,y)] = k

'''
Function: s_point
It defines that Save the All Position By Name
'''
def s_point():
    global q
    d = {
        "board": {str(pos): val for pos, val in board.items()},
        "timecount":timecounter,
        "difficulty":q
    }
    with open(f"{name}.json", "w") as t:
        json.dump(d, t)


'''
Displays the Time , Difficult and Counter
'''
#Time , Difficulty and Move Counter Intiation
global movecounter, p
movecounter = 0
p = 0
    
count = turtle.Turtle()
count.pencolor("#00ff00")
count.hideturtle()
count.penup()
count.goto(-200,250)
count.pendown()

time = turtle.Turtle()
time.pencolor("#00ff00")
time.hideturtle()
time.penup()
time.goto(200,250)
time.pendown()

difficulty = turtle.Turtle()
difficulty.pencolor("#00ff00")
difficulty.hideturtle()
difficulty.penup()
difficulty.goto(-50,250)
difficulty.pendown()

'''
Function : update_move
Updates all the Count
'''
def count_move():
    global movecounter
    count.clear()
    count.write(f"Moves:{movecounter}",font =("Arial",14,"bold"))

'''
Function : difficultycheck
Displays the Diificulty on Screen
'''
def difficultycheck():
    global q
    difficulty.write(f"Mode:{q}",font =("Arial",14,"bold"))

'''
Function : update_time
Displays the Time By Repeating Function For Every 1s
'''
def update_time():
    global timecounter,p
    count_move()
    difficultycheck()
    if p == 0:
        timecounter += 1
    else:
        timecounter += 0
    time.clear()
    minutes = timecounter // 60
    seconds = timecounter % 60
    time.write(f"Time: {minutes:02}:{seconds:02}", align="center", font=("Arial",14,"bold"))
    turtle.ontimer(update_time, 1000)

def closewindow():
    turtle.bye()
    
'''
Function : checkwin()
#Checks that the Board is Satisfied Win
'''
# Win Checking Condition
def checkwin():
    global p,storage
    ordered = [(-150,150),(-50,150),(50,150),(150,150),(-150,50),(-50,50),(50,50),(150,50),(-150,-50),(-50,-50),(50,-50),(150,-50),(-150,-150),(-50,-150),(50,-150),(150,-150)]
    nums = [board[pos] for pos in ordered]
    # nums == list(range(1,17))
    # nums == ["अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ","औ","अं","अः","क","ख",None]
    # nums == ["అ","ఆ","ఇ","ఈ","ఉ","ఊ","ఋ","ౠ","ఎ","ఏ","ఐ","ఒ","ఓ","ఔ","అం",None]
    if nums == ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',None]:
        turtle.clearscreen()
        w = turtle.Turtle()
        w.hideturtle()
        p = 1
        w.write(" YOU WIN! ", align="center", font=("Arial", 36, "bold"))
        w.penup()
        w.goto(-250,-200)
        w.write(f"Congratulations , {name}\n You Won the Game ",font=("Arial", 36, "bold"))
        print(storage)
        turtle.clearscreen()
        leaderboard()
        turtle.listen()
        turtle.onkey(closewindow,"c")
        turtle.onkey(closewindow,"C")
        
        
#Time Intiation
update_time()
name_saver()

'''
Function : writers
#Works like Swap Function Clears the Screen and Rewrite Numbers
'''
def writes(pos):
    writers[pos].clear()
    val = board[pos]
    # val != 16
    if val is not None:
        writers[pos].write(val, font=("Arial",18,"bold"))

'''
Function : up(),down(),left(),right()
#Works per the Movement of the Tiles By Swapping Numbers
'''
#Up Function
def up():
    global empty_pos,movecounter,storage
    x,y = empty_pos
    if (x,y-100) in board:
        board[(x,y)], board[(x,y-100)] = board[(x,y-100)], board[(x,y)]
        writes((x,y))
        writes((x,y-100))
        empty_pos = (x,y-100)
        storage.append(empty_pos)
        movecounter += 1
        count_move()
        checkwin()
        s_point()

# Down Function
def down():
    global empty_pos,movecounter,storage
    x,y = empty_pos
    if (x,y+100) in board:
        board[(x,y)], board[(x,y+100)] = board[(x,y+100)], board[(x,y)]
        writes((x,y))
        writes((x,y+100))
        empty_pos = (x,y+100)
        storage.append(empty_pos)
        movecounter += 1
        count_move()
        checkwin()
        s_point()

#Left Function
def left():
    global empty_pos,movecounter,storage
    x,y = empty_pos
    if (x+100,y) in board:
        board[(x,y)], board[(x+100,y)] = board[(x+100,y)], board[(x,y)]
        writes((x,y))
        writes((x+100,y))
        empty_pos = (x+100,y)
        storage.append(empty_pos)
        movecounter += 1
        count_move()
        checkwin()
        s_point()

# Right Function
def right():
    global empty_pos,movecounter,storage
    x,y = empty_pos
    if (x-100,y) in board:
        board[(x,y)], board[(x-100,y)] = board[(x-100,y)], board[(x,y)]
        writes((x,y))
        writes((x-100,y))
        empty_pos = (x-100,y)
        storage.append(empty_pos)
        movecounter += 1
        count_move()
        checkwin()
        s_point()
        


'''
This Below Code Make the Record Input and Runs until win
'''
turtle.listen()
turtle.onkey(up ,"Up")
turtle.onkey(down ,"Down")
turtle.onkey(left ,"Left")
turtle.onkey(right,"Right")
turtle.onkey(leaderboard,"l")
turtle.onkey(leaderboard,"L")


turtle.mainloop()
        
        

