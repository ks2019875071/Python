import turtle as t

position = [[0,0, "blue"], [-120,0, "purple"], [60,60, "red"], [-180,60, "green"], [-60,60, "yellow"]]

for x, y, c in position :
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c, c)
    t. begin_fill()
    t.circle(30)
    t.end_fill()
    
