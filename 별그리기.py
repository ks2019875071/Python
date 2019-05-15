from turtle import *
color ('red','yellow')
begin_fill()
while True:
    speed(50)
    forward(300)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()
