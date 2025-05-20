import turtle
screen = turtle.Screen()
screen.title('Colored Fractal Pythagoras Tree - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2)

def squaretree(x,y,length,tilt,n):
    if n==0: return
    if n<6:
        turtle.color('forest green')
    else:
        turtle.color('saddle brown')
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.seth(tilt)
    turtle.fd(length)
    turtle.left(90)
    turtle.fd(length)
    turtle.left(45)
    turtle.fd(length/2**0.5)
    x1,y1 = turtle.xcor(), turtle.ycor()    
    turtle.left(90)
    turtle.fd(length/2**0.5)
    x2,y2 = turtle.xcor(), turtle.ycor()
    turtle.left(45)
    turtle.fd(length)
    turtle.left(90)
    turtle.end_fill()

    squaretree(x1,y1,length/2**0.5,tilt-45,n-1)
    squaretree(x2,y2,length/2**0.5,tilt+45,n-1)
    
squaretree(-150,-600,300,0,13)
screen.update()