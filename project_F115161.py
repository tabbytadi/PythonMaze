import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Solving Program")
wn.setup(1300, 700)

start_x = 0
start_y = 0
end_x = 0
end_y = 0

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

grid4 = [
    "+++++++++++++++",
    "              e",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "s              ",
    "+++++++++++++++",
]

grid2 = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + + + + + +",
"+++++ + + + + +",
"+     + + +   +",
"+++++++++++++++",
 ]

grid3 = [
"+++++++++",
"+ ++ ++++",
"+ ++ ++++",
"+ ++ ++++",
"+s   ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
 ]

grid1 = [
    "++++++++++++++++++++++++++++++++++++++++++++++",
    "+ s             +                            +",
    "+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
    "+           +                 +        +     +",
    "++ +++++++ ++++++++++++++ ++++++++++++++++++++",
    "++ ++    + ++           + ++                 +",
    "++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
    "++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
    "++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
    "++ ++   ++ ++             ++          +++ ++e+",
    "++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
    "++    + ++                   ++              +",
    "+++++ + +++++++++++++++++++++++ ++++++++++++ +",
    "++ ++ +                   ++          +++ ++ +",
    "++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
    "++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
    "++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
    "++                     ++ ++ ++              +",
    "+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++",
]

def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " ":
                path.append((screen_x, screen_y))

            if character == "e":
                yellow.goto(screen_x, screen_y)
                yellow.stamp()
                end_x, end_y = screen_x, screen_y
                path.append((screen_x, screen_y))

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)

def bfs_search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y
    while len(frontier) > 0:
        current = frontier.pop(0)

        if current == (end_x, end_y):
            break

        x, y = current

        for next_move in [(x - 24, y), (x, y - 24), (x + 24, y), (x, y + 24)]:
            if next_move in path and next_move not in visited:
                solution[next_move] = x, y
                blue.goto(next_move)
                blue.stamp()
                frontier.append(next_move)
                visited.append(next_move)
                green.goto(next_move)
                green.stamp()
                time.sleep(0.05)


def dfs_search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y
    while len(frontier) > 0:
        time.sleep(0)
        current = (x, y)

        if (x, y) == (end_x, end_y):
            break

        if (x - 24, y) in path and (x - 24, y) not in visited:
            cellleft = (x - 24, y)
            solution[cellleft] = x, y
            blue.goto(cellleft)
            blue.stamp()
            frontier.append(cellleft)

        if (x, y - 24) in path and (x, y - 24) not in visited:
            celldown = (x, y - 24)
            solution[celldown] = x, y
            blue.goto(celldown)
            blue.stamp()
            frontier.append(celldown)

        if (x + 24, y) in path and (x + 24, y) not in visited:
            cellright = (x + 24, y)
            solution[cellright] = x, y
            blue.goto(cellright)
            blue.stamp()
            frontier.append(cellright)

        if (x, y + 24) in path and (x, y + 24) not in visited:
            cellup = (x, y + 24)
            solution[cellup] = x, y
            blue.goto(cellup)
            blue.stamp()
            frontier.append(cellup)

        x, y = frontier.pop()
        visited.append(current)
        green.goto(x, y)
        green.stamp()
        if (x, y) == (end_x, end_y):
            yellow.stamp()
        if (x, y) == (start_x, start_y):
            red.stamp()

def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]

maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
frontier = []
solution = {}

setup_maze(grid4)
dfs_search(start_x, start_y)
backRoute(end_x, end_y)

wn.exitonclick()