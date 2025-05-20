import turtle
import math

screen = turtle.Screen()
screen.title('Octaflake Fractal - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
turtle.fillcolor('royal blue')
turtle.pencolor('steel blue')
screen.tracer(0,0)

def octagon(x,y,r): #x,y is the center
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(90)
    turtle.fd(r)
    turtle.left(180-135/2)
    turtle.down()
    turtle.begin_fill()
    for _ in range(8):
        turtle.fd(2*r*math.sin(math.radians(45/2)))
        turtle.left(45)
    turtle.end_fill()

    
def octaflake(x,y,r,n):
    if r<10:
        octagon(x,y,r)
        return
    r2 = r/(1+1/math.tan(math.radians(45/2)))   
    octaflake(x,y,r-2*r2,n-1)
    direction = 90
    for _ in range(8):
        turtle.up()
        turtle.goto(x,y)
        turtle.seth(direction)
        turtle.fd(r-r2)
        octaflake(turtle.xcor(),turtle.ycor(),r2,n-1)
        direction += 45

octaflake(0,0,900,3)
screen.update()
a=input()