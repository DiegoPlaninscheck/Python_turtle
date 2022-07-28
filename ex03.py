import turtle
from random import randint

turtle.bgcolor('black')
tar1 = turtle.Pen()
tar2 = turtle.Pen()
tar3 = turtle.Pen()
chegada = turtle.Pen()

def configTartaruga():
    tar1.speed(2)
    tar1.color('green')
    tar2.speed(2)
    tar2.color('yellow')
    tar3.speed(2)
    tar3.color('red')
    tar1.shape('turtle')
    tar2.shape('turtle')
    tar3.shape('turtle')

def arrumarTartaruga():
    tar1.up()
    tar2.up()
    tar3.up()
    tar1.setpos(-250, 50)
    tar2.setpos(-250, 0)
    tar3.setpos(-250, -50)

def linhaChegada():
    chegada.color('white')
    chegada.up()
    chegada.setpos(300, 200)
    chegada.down()
    chegada.right(90)
    chegada.forward(350)

configTartaruga()
arrumarTartaruga()
linhaChegada()

def velocidade():
    tar1.forward(randint(0,2))
    tar2.forward(randint(0,2))
    tar3.forward(randint(0,2))
    tar1.speed(randint(0,2))
    tar2.speed(randint(0,2))
    tar3.speed(randint(0,2))

def comeco():
    ganhou = False
    while (ganhou == False):
        velocidade()
        if tar1.pos()[0] == chegada.pos()[0]:
            ganhou = True
            print("tar1 ganhou!")
        elif tar2.pos()[0] == chegada.pos()[0]:
            ganhou = True
            print("tar2 ganhou!")
        elif tar3.pos()[0] == chegada.pos()[0]:
            ganhou = True
            print("tar3 ganhou!")
comeco()