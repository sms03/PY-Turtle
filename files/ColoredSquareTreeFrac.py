import turtle
import colorsys

screen = turtle.Screen()
screen.title('Squares Tree Colored - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def squaretree(x,y,length,tilt,n):
    if n==0: return       
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt)
    turtle.begin_fill()
    c=colorsys.hsv_to_rgb(0.4*(N-n)/N,1,0.7)
    turtle.color(c)
    turtle.fd(length)
    turtle.left(90)
    turtle.fd(length)
    x1,y1 = turtle.xcor(), turtle.ycor()
    turtle.left(90)
    turtle.fd(length)
    x2,y2 = turtle.xcor(), turtle.ycor()
    turtle.left(90)
    turtle.fd(length)
    turtle.left(90)
    turtle.end_fill()
    
    squaretree(x2,y2,length/2**0.5,tilt+45,n-1)
    turtle.up()
    turtle.goto(x1,y1)
    turtle.seth(tilt+135)
    turtle.fd(length/2**0.5)
    squaretree(turtle.xcor(),turtle.ycor(),length/2**0.5,tilt-45,n-1)

N=14    
squaretree(-150,-600,300,0,N)
screen.update()