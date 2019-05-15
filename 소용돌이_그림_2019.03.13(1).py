print ('Hello','world!')


import turtle
colors=['green','blue','red','orange','yellow','purple']
t=turtle.Turtle()
t.shape('turtle')
t.color('white')

turtle.bgcolor('black')
t.speed(0)
t.width(3)
length=10

while length<500:
	t.forward(length)
	t.pencolor(colors[length%6])
	t.right(89)
	length+=10

