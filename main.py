from turtle import *
from random import *

screen = Screen()
screen.title("Turtle Racer")
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a colour:\n Red, Orange, Blue, Green, Purple ")
colours = ['red', 'orange', 'blue', 'green', 'purple']
name = ['red', 'orange', 'blue', 'green', 'purple']
turtles = []

finish_line = Turtle()
finish_line.color("black")
finish_line.pu()
finish_line.hideturtle()
finish_line.goto(200, 200)
finish_line.seth(270)
while finish_line.ycor() != -200:
    finish_line.pd()
    finish_line.fd(20)
    finish_line.pu()
    finish_line.fd(20)

y_cor = -60
for x in range(len(name)):
    name[x] = Turtle(shape="turtle")
    turtles.append(name[x])
    name[x].color(colours[x])
    name[x].penup()
    name[x].goto(x - 230, y=y_cor)
    y_cor += 30
if user_bet:
    is_race_on = True

winner = 0
while is_race_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))

        if turtle.xcor() >= 200:
            winner = turtle.pencolor()
            is_race_on = False

if winner == user_bet:
    print("User guess correctly")
else:
    print("User guessed incorrectly")

screen.exitonclick()
