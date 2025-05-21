import turtle
import math

turtle.color('red')
d = 500
r = d/math.tan(math.radians(67.5))
turtle.up()
turtle.goto(0,-600)
turtle.seth(45)
turtle.down()
turtle.fd(d)
turtle.circle(r,225)
turtle.left(180)
turtle.circle(r,225)
turtle.fd(d)


turtle.color('red')
d = 500
r = d/math.tan(math.radians(67.5))
turtle.up()
turtle.goto(0,-600)
turtle.seth(45)
turtle.begin_fill()
turtle.down()
turtle.fd(d)
turtle.circle(r,225)
turtle.left(180)
turtle.circle(r,225)
turtle.fd(d)
turtle.end_fill()