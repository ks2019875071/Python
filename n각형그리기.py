import turtle as t
t.shape("turtle")

l = int(t.textinput("","크기는 얼마로 할까요?"))
n = int(t.textinput("","몇각형을 원하시나요?:"))

for i in range(n) :
    t.forward(l)
    t.left(360/n)
