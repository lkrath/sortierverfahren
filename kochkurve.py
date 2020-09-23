# Kochkurve mit turtle

import turtle

t = turtle.Turtle()

t.speed(300)
t.penup()
t.rt(180)
t.forward(250)
t.rt(180)
t.pendown()

def kochkurve(k, n):
    if k > 0:
        kochkurve(k-1, n/3)
        t.lt(60)
        kochkurve(k-1, n/3)
        t.rt(120)
        kochkurve(k-1, n/3)
        t.lt(60)
        kochkurve(k-1, n/3)
    else:
        t.forward(n)

def koch_schneeflocke(k, n):
    t.penup()
    t.lt(90)
    t.forward(145)
    t.rt(90)
    t.pendown()
    for i in range(3):
        kochkurve(k, n)
        t.rt(120)

koch_schneeflocke(7, 500)
t.hideturtle()
turtle.Screen().exitonclick()