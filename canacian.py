import turtle
t=turtle.Turtle()
t.shape("turtle")

color_list = ["red","green","red"]


t.fillcolor(color_list[0])
t.begin_fill()
t.pencolor(color_list[2])

##꽃 아래쪽
t.left(80)
t.forward(100)
t.right(60)
t.forward(20)
length=30
i=0
r=30

##꽃봉오리
while i<=8 :
    t.circle(20)
    t.left(r)
    t.forward(length)
    t.speed(10)
    i += 1
    r += 1

##꽃 아래쪽
t.forward(5)
t.right(5)
t.right(50)
t.forward(100)
t.end_fill()

##줄기
t.pencolor(color_list[1])
t.speed(1)
t.width(5)
t.right(5)
t.forward(200)
