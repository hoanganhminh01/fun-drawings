from turtle import *

BODY_COLOR = 'yellow'
GLASS_COLOR = 'cyan'

s = getscreen()
pen = Turtle()


def body():
    pen.pensize(20)
    pen.fillcolor(BODY_COLOR)
    pen.begin_fill()

    pen.right(90)
    pen.forward(50)
    pen.right(180)
    pen.circle(40, -180)
    pen.right(180)
    pen.forward(200)

    pen.right(180)
    pen.circle(100, -180)

    pen.backward(20)
    pen.left(15)
    pen.circle(500, -20)
    pen.backward(20)
    pen.circle(40, -180)
    pen.left(7)
    pen.backward(50)

    pen.up()
    pen.left(90)
    pen.forward(10)
    pen.right(90)
    pen.down()
    pen.right(240)
    pen.circle(50, -70)
    pen.end_fill()


def glass():
    pen.up()
    pen.right(230)
    pen.forward(100)
    pen.left(90)
    pen.forward(20)
    pen.right(90)

    pen.down()
    pen.fillcolor(GLASS_COLOR)
    pen.begin_fill()

    pen.right(150)
    pen.circle(90, -55)

    pen.right(180)
    pen.forward(1)
    pen.right(180)
    pen.circle(10, -65)
    pen.right(180)
    pen.forward(110)
    pen.right(180)

    pen.circle(50, -190)
    pen.right(170)
    pen.forward(80)

    pen.right(180)
    pen.circle(45, -30)
    pen.end_fill()


def backpack():
    pen.up()
    pen.right(60)
    pen.forward(100)
    pen.right(90)
    pen.forward(75)

    pen.fillcolor(BODY_COLOR)
    pen.begin_fill()

    pen.down()
    pen.forward(30)
    pen.right(255)

    pen.circle(300, -30)
    pen.right(260)
    pen.forward(30)
    pen.end_fill()


body()
glass()
backpack()
exitonclick()
