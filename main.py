from turtle import Turtle, Screen
import random

red = Turtle()
red.color("red")
red.penup()

green = Turtle()
green.color("green")
green.penup()

blue = Turtle()
blue.color("blue")
blue.penup()

black = Turtle()
black.color("black")
black.penup()

yellow = Turtle()
yellow.color("yellow")
yellow.penup()

orange = Turtle()
orange.color("orange")
orange.penup()

screen = Screen()
screen.setup(width= 500, height= 400)

choice = screen.textinput("Your Choice", "Which turtle do you think will win? red/green/blue/yellow/black/orange : ").lower()

red.goto(-220, 50)
green.goto(-220, 30)
blue.goto(-220, 10)
black.goto(-220, -10)
yellow.goto(-220, -30)
orange.goto(-220, -50)


def move(tim):
    todo = random.randint(1, 10)
    if todo > 5:
        tim.fd(10)

winner = "None"


game_over = False
while not game_over:
    move(red)
    move(green)
    move(blue)
    move(black)
    move(yellow)
    move(orange)

    if red.pos()==(250, 50):
        game_over=True
        winner = "red"
    elif green.pos()==(250, 30):
        game_over=True
        winner = "green"
    elif blue.pos()==(250, 10):
        game_over=True
        winner = "blue"
    elif black.pos()==(250, -10):
        game_over=True
        winner = "black"
    elif yellow.pos()==(250, -30):
        game_over=True
        winner = "yellow"
    elif orange.pos()==(250,30):
        game_over=True
        winner = "orange"


if choice == winner:
    screen.textinput(f"{winner} won","You were right")
else:
    screen.textinput(f"{winner} won", "You were wrong")
# print(red.pos())

screen.exitonclick()


