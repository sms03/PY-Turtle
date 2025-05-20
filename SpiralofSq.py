import turtle
import math

screen = turtle.Screen()
screen.title('Spiral of Squares - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def draw_square(x,y,length):
    turtle.up()
    turtle.goto(x-length/2,y-length/2)
    turtle.seth(0)
    turtle.down()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)
        
def spiral_squre(x,y,direction,length):
    if length<1:
        return
    draw_square(x,y,length)
    px = x + length*1.5*math.cos(math.radians(direction))
    py = y + length*1.5*math.sin(math.radians(direction))

    spiral_squre(px,py,direction-30,length*0.93)

spiral_squre(500,-700,180,300)