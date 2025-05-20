import turtle
screen = turtle.Screen()
screen.title('Stacked Squares - PythonTurtle.Academy')
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor('indigo')
turtle.fillcolor('white')
turtle.pensize(2)

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
    
stacksquares(0,0,800,1)
screen.update()