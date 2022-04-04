import turtle

BGMI = turtle.Turtle()
turtle.bgcolor("yellow")
BGMI.color("red")
#pubg.speed(0)

def rect(): # length 340 # breadh 182
    BGMI.pensize(9)
    BGMI.forward(170)
    BGMI.left(45)
    BGMI.forward(6)
    BGMI.left(45)
    BGMI.forward(170)
    BGMI.left(45)
    BGMI.forward(6)
    BGMI.left(45)
    BGMI.forward(330)
    BGMI.left(45)
    BGMI.forward(6)
    BGMI.left(45)
    BGMI.forward(170)
    BGMI.left(45)
    BGMI.forward(6)
    BGMI.left(45)
    BGMI.forward(170)

def four_corner_lines():
    BGMI.pensize(12)
    BGMI.penup()
    BGMI.forward(180)
    BGMI.left(90)
    BGMI.forward(35)
    BGMI.left(90)
    BGMI.pendown()
    BGMI.forward(12)
    BGMI.penup()
    BGMI.forward(344)
    BGMI.pendown()
    BGMI.forward(17)
    BGMI.penup()
    BGMI.right(90)
    BGMI.forward(105)
    BGMI.right(90)
    BGMI.pendown()
    BGMI.forward(17)
    BGMI.penup()
    BGMI.forward(344)
    BGMI.pendown()
    BGMI.forward(12)

def B():
    BGMI.penup()
    BGMI.left(180)
    BGMI.forward(280)
    BGMI.pendown()
    BGMI.forward(40)
    BGMI.left(90)
    BGMI.forward(100)
    BGMI.left(180)
    BGMI.forward(52)
    BGMI.right(90)
    BGMI.forward(40)
    BGMI.left(90)
    BGMI.forward(47)

def G():
    BGMI.penup()
    BGMI.right(90)
    BGMI.forward(32)
    BGMI.right(90)
    BGMI.pendown()
    BGMI.forward(98)
    BGMI.left(90)
    BGMI.forward(40)
    BGMI.left(90)
    BGMI.forward(98)

def M():
    BGMI.penup()
    BGMI.right(90)
    BGMI.forward(35)
    BGMI.pendown()
    BGMI.forward(45)
    BGMI.right(90)
    BGMI.forward(43)
    BGMI.right(45)
    BGMI.forward(5)
    BGMI.right(45)
    BGMI.forward(40)
    BGMI.left(90)
    BGMI.forward(5)
    BGMI.left(90)
    BGMI.forward(40)
    BGMI.right(45)
    BGMI.forward(5)
    BGMI.right(45)
    BGMI.forward(40)
    BGMI.right(90)
    BGMI.forward(45)
    BGMI.right(90)
    BGMI.forward(96)

def I():
    BGMI.penup()
    BGMI.right(180)
    BGMI.forward(53)
    BGMI.left(90)
    BGMI.forward(98)
    BGMI.pendown()
    BGMI.forward(25)
    BGMI.right(90)
    BGMI.forward(45)
    BGMI.right(90)
    BGMI.forward(45)
    BGMI.right(90)
    BGMI.forward(95)
    BGMI.right(90)
    BGMI.forward(40)

rect()
four_corner_lines()
B()
G()
M()
I()

turtle.done()