import turtle
import random

screen = turtle.Screen()
front = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37-32\\front.png"
back = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37-32\\back.jpeg"

screen.addshape(front)
screen.addshape(back)

t1 = turtle.Turtle()

print ("동전 던지기 게임을 시작합니다.\n")
coin=random.randrange(2)

if coin==0:
    t1.shape(front)
    t1.stamp()

if coin ==1:
    t1.shape(back)
    t1.stamp()

