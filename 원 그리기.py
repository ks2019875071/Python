import turtle as t

r = int(input("원의 갯수를 입력 하시오."))
color_list = ["red"]

for i in range(r) :
    t.speed(0)
    t.fillcolor(color_list[0])
    t.begin_fill()
    t.circle(100)
    t.left(360/r)
    t.end_fill()
