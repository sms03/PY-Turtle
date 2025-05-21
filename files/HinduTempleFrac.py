import turtle
import math

screen = turtle.Screen()
screen.title('Hindu Temple Fractal - PythonTurtle.Academy')
screen.setup(800,800)
screen.setworldcoordinates(-10000,-10000,10000,10000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def draw_circle(x,y,r):
    turtle.up()
    turtle.goto(x,y-r)
    turtle.seth(0)
    turtle.down()
    turtle.circle(r)
    
def temple(x,y,r,direction):
    if r < 40: return
    draw_circle(x,y,r)

    temple(x+r*1.5*math.cos(math.radians(direction)),y+r*1.5*math.sin(math.radians(direction)),0.5*r,direction)
    temple(x+r*1.5*math.cos(math.radians(direction-90)),y+r*1.5*math.sin(math.radians(direction-90)),0.5*r,direction-90)
    temple(x+r*1.5*math.cos(math.radians(direction+90)),y+r*1.5*math.sin(math.radians(direction+90)),0.5*r,direction+90)
    
temple(0,-2000,3000,90)

screen.update()
a=input()