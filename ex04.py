import turtle

turtle.bgcolor("black")

c = turtle.Turtle()

c.pencolor("#8a2be2")

def triforce(lado):

    for j in range(3):
        c.forward(lado)
        c.left(120)
        c.forward(lado)

    for j in range(4):
        c.forward(lado)
        c.left(120)
        c.forward(lado)

    for j in range(3):
        c.forward(lado)
        c.left(120)

triforce(100)