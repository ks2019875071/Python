import turtle as t
t.shape("turtle")

import random


times = random.randint(1,50)
drunk = random.choice([True,False])

if drunk :
    
    t.write("The Turtle got drunk.")
    for i in range(times) :
        length = random.randint(-100,100)
        angle = random.randint(-360,360)
        speed = random.randint(1,50)
        t.forward (length)
        t.left(angle)

else :
    t.write("The Turtle is okay.")

    length = random.randint(0,100)
    t.forward(length)
