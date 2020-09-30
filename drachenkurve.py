# Drachenkurve

import turtle

t = turtle.Turtle()

def side(l):
    return (l**2/2)**2

def dragon(l, n, turn='right'):
    if n == 0:
        t.forward(l)
        return False

    if turn == 'right':
        t.rt(45)
    else:
        t.lt(45)

    dragon(side(l), n-1, turn='right')

    if turn == 'right':
        t.rt(90)
    else:
        t.lt(90)

    dragon(side(l), n-1, turn='left')

    if turn == 'right':
        t.rt(45)
    else:
        t.lt(45)

t.speed('fastest')

dragon(550, 3)

turtle.Screen().exitonclick()