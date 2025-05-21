import turtle
screen = turtle.Screen()
screen.title('T-square Fractal - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
screen.bgcolor('white')
turtle.hideturtle()
turtle.pencolor('white')

def stacksquares(x,y,length,n):
    if n==0: return
    stacksquares(x-length/2,y-length/2,length/2,n-1)
    stacksquares(x+length/2,y+length/2,length/2,n-1)
    stacksquares(x-length/2,y+length/2,length/2,n-1)
    stacksquares(x+length/2,y-length/2,length/2,n-1)
    
    turtle.up()
    turtle.goto(x-length/2,y-length/2)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)
    turtle.end_fill()

turtle.up()
turtle.goto(-800,-800)
turtle.begin_fill()
turtle.fillcolor('black')
for _ in range(4):
    turtle.fd(1600)
    turtle.left(90)
turtle.end_fill()
turtle.fillcolor('white')
stacksquares(0,0,800,7)
screen.update()