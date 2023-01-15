from turtle import forward, left, goto, right, penup, pendown, speed, screensize, exitonclick
from math import sqrt
import random

def draw_house(a):
    c = round(sqrt(2*a**2))

    for i in range(0, 3):
        forward(a)
        left(90)
    forward(a)

    left(135)
    forward(c)
    left(90)

    forward(c/4)
    right(45)
    forward(c/10)
    left(90)
    forward(c/20)
    left(90)
    forward(c/20)
    right(135)
    forward(c/4 - sqrt((c/10 - c/20)**2 + (c/20)**2))

    left(90)
    forward(c/2)
    left(90)

    forward(c)
    left(45)

screensize(canvwidth=800, canvheight=800)
speed(0)
penup()
goto(-360, -180)
pendown()

domeckyWidth = 720

while domeckyWidth > 10:
    randomNum = random.randint(5, 360 if domeckyWidth > 360 else domeckyWidth)
    draw_house(randomNum)
    domeckyWidth = domeckyWidth - randomNum

exitonclick()