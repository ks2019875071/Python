import turtle
t=turtle.Turtle()
t.shape("turtle")


print ("a=좌\nd=우\nw=앞\ns=뒤\nq=종료\n")

while True :
    command = turtle.textinput ("방향 입력","명령을 입력하시오.")
    if command == "a" :
        t.left(90)
        t.forward(100)
    if command == "d" :
        t.right(90)
        t.forward(100)
    if command == "w" :
        t.forward(100)
    if command == "s" :
        t.backward(100)
    if command == "q" :
        break
