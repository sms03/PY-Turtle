import turtle
import math

screen = turtle.Screen()
screen.title('Dodecagon Spiral - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def draw_spiral(x,y,r,direction):
    if r < 10: return
    d = direction
    r2 = r*math.cos(math.radians(360/24))/math.cos(math.radians(360/24-alpha))
    dist = r*math.sin(math.radians(360/24))-r2*math.sin(math.radians(360/24-alpha))
    turtle.up()
    px = x + r*math.cos(math.radians(d))
    py = y + r*math.sin(math.radians(d))
    turtle.goto(px,py)
    turtle.color((1-r/900,1-r/900,1-r/900))
    turtle.down()
    d += 360/12
    for _ in range(12):
        px = x + r*math.cos(math.radians(d))
        py = y + r*math.sin(math.radians(d))
        turtle.goto(px,py)
        d += 360/12
    draw_spiral(x,y,r2,direction+alpha)
    
    
alpha = 3
draw_spiral(0,0,900,90)