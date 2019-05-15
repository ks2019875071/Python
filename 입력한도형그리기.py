import turtle
t= turtle.Turtle()
t.shape ("turtle")

shape = turtle.textinput("","도형을 입력 하시오: ")

if shape == "사각형" :
    shape = turtle.textinput("","가로: ")
    width = int(shape) ##int는 정수로 바꾸라는 뜻.
    shape = turtle.textinput("","세로: ")
    height = int(shape)
    t.forward (width)
    t.left(90)
    t.forward (height)
    t.left(90)
    t.forward (width)
    t.left(90)
    t.forward (height)

if shape == "삼각형" :
    shape = turtle.textinput("","변의 길이: ")
    size = int(shape)
    t.forward (size)
    t.left(120)
    t.forward (size)
    t.left(120)
    t.forward (size)

if shape == "원" :
    shape = turtle.textinput("","반지름")
    size = int(shape)
    t.circle (size)
