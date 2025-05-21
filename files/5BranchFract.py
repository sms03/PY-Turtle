import turtle
import colorsys

screen = turtle.Screen()
screen.title('Five Branch Fractal Tree - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def fivebranchtree(x,y,length,direction,n):
    if n==0: return
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(direction)
    turtle.pensize(length/100)
    turtle.fd(length)
    px,py = turtle.xcor(), turtle.ycor()
    fivebranchtree(px,py,length*0.445,direction,n-1)
    fivebranchtree(px,py,length*0.445,direction+360/7,n-1)
    fivebranchtree(px,py,length*0.445,direction+2*360/7,n-1)
    fivebranchtree(px,py,length*0.445,direction-2*360/7,n-1)
    fivebranchtree(px,py,length*0.445,direction-360/7,n-1)

L=1000    
fivebranchtree(0,-900,L,90,8)
screen.update()