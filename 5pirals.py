import turtle
import math

screen = turtle.Screen()
screen.title('5 Spirals - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2)

colors = [ 'red', 'orange', 'green', 'blue', 'purple' ]
def draw_spiral(x,y,r,direction):
    if r < 10: return
    d = direction
    r_ratio = math.cos(math.radians(36))/math.cos(math.radians(36-alpha))
    d_ratio = math.sin(math.radians(36))-r_ratio*math.sin(math.radians(36-alpha))
    for i in range(5):
        px = x + r*math.cos(math.radians(d))
        py = y + r*math.sin(math.radians(d))
        turtle.color(colors[i])
        turtle.up()
        turtle.goto(px,py)
        turtle.down()
        turtle.seth(d+180-54)
        dist = r*d_ratio
        r2 = r
        while dist > 0.1:
            turtle.fd(dist)
            r2 = r2*r_ratio
            dist = r2*d_ratio
            turtle.left(alpha)
        d += 360/5
       
alpha = 5
draw_spiral(0,0,900,90)