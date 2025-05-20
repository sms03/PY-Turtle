import turtle
import random

turtle.speed(0)
turtle.bgcolor("black")

colors = ["#FF69B4", "#7FFFD4", "#FFFF00", "#00FFFF", "#FFD700", "#EE82EE", "#7B68EE", "#FF4500"]

for i in range(144):
    turtle.pencolor(random.choice(colors))
    turtle.fillcolor(random.choice(colors))
    turtle.begin_fill()
    for j in range(6):
        turtle.circle(80)
        turtle.right(60)
    turtle.end_fill()
    turtle.right(2.5)

turtle.done()