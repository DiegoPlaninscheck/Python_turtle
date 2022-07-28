import turtle;
turtle.bgcolor('black')

pen = turtle.Pen()
pen.color('#8a2be2')
pen.speed(5)

def triangulo():
    for i in range(2):
        pen.left(120)
        pen.forward(100)

for i in range(4):
    pen.right(90)
    pen.forward(100)

triangulo()