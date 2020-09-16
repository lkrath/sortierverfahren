import turtle

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(1.5, 1.5, 1.5)
t.fillcolor('green')

def muschel(color):
    turtle.bgcolor('blue')
    t.pencolor(color)
    t.speed(11)
    t.penup()
    t.goto(0, -50)
    t.pendown()

    for i in range(150):
        t.circle(i)
    t.circle(100)

def muster1():
    colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    turtle.bgcolor('black')
    t.pensize(3)
    j = 0
    t.rt(50)
    for i in range(400):
        t.pencolor(colours[j])
        j += 1
        if j == 6:
            j = 0
        t.lt(52)
        t.forward(i)

def muster2():
    colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    turtle.bgcolor('black')
    t.speed(13)
    j = 0
    t.rt(50)
    for i in range(800):
        t.pencolor(colours[j])
        t.fillcolor(colours[j])
        j += 1
        if j == 6:
            j = 0
        t.lt(50)
        t.begin_fill()
        t.circle(i)
        t.end_fill()
        t.penup()
        t.forward(i*2)
        t.pendown()

def muster3():
    colours = ['blue', 'green', '#FF3188']
    j = 0
    turtle.bgcolor('black')
    t.speed(11)
    t.pensize(2)
    t.rt(60)
    for i in range(400):
        t.pencolor(colours[j])
        j += 1
        if j == 3:
            j = 0
        t.forward(i*5)
        t.lt(125)

def muster4():
    colours = ['red', 'orange', 'yellow']
    j = 0
    turtle.bgcolor('black')
    t.speed(11)
    t.pensize(2)
    t.rt(60)
    for i in range(400):
        t.pencolor(colours[j])
        j += 1
        if j == 3:
            j = 0
        t.forward(i*5)
        t.lt(122)

muster4()

turtle.Screen().exitonclick()