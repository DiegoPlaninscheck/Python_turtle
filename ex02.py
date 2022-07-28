import turtle

turtle.bgcolor('black')

pen = turtle.Pen()

pen.color('#8a2be2')

cores =['red', 'yellow', 'green']

def quadrado():
    for i in range(4):
        pen.forward(100)
        pen.right(90)

def desenhar():
    for i in range(3):
        pen.color(cores[i])
        quadrado()
        pen.up()
        pen.forward(110)
        pen.down()

desenhar()