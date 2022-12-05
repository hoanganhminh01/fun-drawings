from turtle import *
import math
import random

pen = Turtle()
screen = Screen()
screen.setup(1000, 800)

pen.speed(0)
pen.hideturtle()
pen.up()
bgcolor('dodger blue')
pen.pencolor('white')
pen.pensize(2)
n = 500


def ellipse(X, Y, a, b, ts, te, P):
    t = ts
    for i in range(n):
        x = a * math.cos(t)
        y = b * math.sin(t)
        P.append((x + X, y + Y))
        t += (te - ts) / (n - 1)


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def draw_arc(p1, p2, ext):
    pen.up()
    pen.goto(p1)
    pen.seth(pen.towards(p2))
    a = pen.heading()
    b = 360 - ext
    c = (180 - b) / 2
    d = a - c
    e = d - 90
    r = dist(p1, p2) / 2 / math.sin(math.radians(b / 2))
    pen.seth(e)
    pen.down()
    pen.circle(r, ext, 100)
    return pen.xcor(), pen.ycor()


def cloud(P):
    step = n // 10
    a = 0
    b = a + random.randint(step // 2, step * 2)
    p1 = P[a]
    p2 = P[b]
    pen.fillcolor('white')
    pen.begin_fill()
    p3 = draw_arc(p1, p2, random.uniform(70, 180))
    while b < len(P) - 1:
        p1 = p3
        if b < len(P) / 2:
            ext = random.uniform(70, 180)
            b += random.randint(step // 2, step * 2)
        else:
            ext = random.uniform(30, 70)
            b += random.randint(step, step * 2)
        b = min(b, len(P) - 1)
        p2 = P[b]
        p3 = draw_arc(p1, p2, ext)
    pen.end_fill()


def txt():
    pen.up()
    pen.setpos(-120, 70)
    pen.down()
    pen.color('dodger blue')
    pen.write("To bé Mei hì hì", font=("Goudy Old Style", 30, "bold"))


P = []
ellipse(0, 0, 300, 200, 0, math.pi, P)
ellipse(0, 0, 300, 50, math.pi, math.pi * 2, P)
cloud(P)
txt()
exitonclick()
