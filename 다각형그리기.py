import turtle
t=turtle.Turtle()
t.shape('turtle')

size=int(input('도형의 크기는 얼마로 할까요?'))
n=int(input('몇각형을 그리시겠어요?'))

for i in range(n):
      t.forward(size)
      t.left(360/n)
